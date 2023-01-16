"""
Author: Bharadwaj Prabhala (BP)
Module: This module contains the main APIs that add, update and fetch transactions.
"""
from flask import Flask
from flask import request, abort, make_response, jsonify
import json
from flask_cors import CORS
from block import Block
from db import ConnectToDB
from PeerComm import PeerComm

#Allowing CORS since this was done on local system. Tighter security principles should apply elsewhere.
app = Flask(__name__)
CORS(app)

# Default endpoint
@app.route('/')
def index():
    return "Welcome to the Real Estate Ledger!"

# Add a new transaction into the ledger
# This method adds the new transaction to all the peer ledgers and then updates the golden ledger table
@app.route("/add_transaction", methods=['POST'])
def add_transaction():
    blk = Block()
    conn = ConnectToDB()
    peerComm = PeerComm()

    transaction_details = request.json
    new_block = blk.generateBlock(transaction_details)

    #Send the transaction details to all the peers
    if(peerComm.sendToPeers(new_block)):
        if(new_block != None):
            conn.saveToDB(new_block)
            return {"response": "Transaction successfully added."}
        else:
            return {"response": "Transaction already exists."}
    else:
        return {"response": "Peers have not validated this transaction."}

# Fetch the transaction details from the DB using the transaction identifier
@app.route("/find_transaction_by_id", methods=['POST'])
def find_transaction_by_id():
    transaction_details = request.json

    conn = ConnectToDB()
    record = constructJSON(conn.getTransactionDetails(transaction_id = transaction_details['transaction_id']))

    return {"response": record['transaction_details']}

# Build a JSON object from the tuple
def constructJSON(record):
    return {
        "transaction_id": record[0], "prev_block_hash": record[1], "curr_block_hash": record[2], "transaction_details":{ "buyer_name": record[3], "seller_name": record[4], "address": record[5], "area": record[6], "price_per_sft": record[7], "total_price": record[8], "gst": record[9], "transaction_date": str(record[10]), "registration_number": record[11], "litigations": record[12], "entrance_facing": record[13], "survey_number": record[14], "north_survey_number": record[15], "south_survey_number": record[16], "east_survey_number": record[17], "west_survey_number": record[18], "verified_by": record[19]
        }
    }

# Used to reconstruct the transaction object during an update transaction
def reconstructObject(record, changed_columns, changed_values):
    blk = Block()

    new_block = constructJSON(record)

    for i in range(0, len(changed_columns)):
        new_block['transaction_details'][changed_columns[i]] = changed_values[i]

    new_block["curr_block_hash"] = blk.generateHash(new_block)

    return (new_block['transaction_id'], new_block['prev_block_hash'], new_block['curr_block_hash'], new_block['transaction_details'])
    
# Method to update the change to all the peers once the peers have all validated the new changes
def updateChange(block):
    conn = ConnectToDB()
    peerComm = PeerComm()
    block_obj = Block()

    current_block_transaction_id = block[0]

    #Get all the subsequent transactions from the DB since all of their hashes need to be updated.
    subsequent_transactions = conn.getAllSubsequentTransactions(current_block_transaction_id)
    next_block_prev_hash = block[2]

    #Update the current transaction in the DB
    conn.saveToDB(block, transType="update")
    peerComm.updateChange(block)

    #Update all the subsequent transactions with the new hash
    for sub in subsequent_transactions:
        blk = constructJSON(sub)
        blk['prev_block_hash'] = next_block_prev_hash
        blk['curr_block_hash'] = block_obj.generateHash(blk['prev_block_hash'] + str(blk['transaction_details']))
        next_block_prev_hash = blk['curr_block_hash']
        updated_blk = (blk['transaction_id'], blk['prev_block_hash'], blk['curr_block_hash'], blk['transaction_details'])
        conn.saveToDB(updated_blk, transType="update")
        peerComm.updateChange(updated_blk)
        

# API to update transactions by first verifying with peers
@app.route("/update_transaction", methods=['POST']) 
def update_transaction():
    req = request.json
    peerComm = PeerComm()

    transaction_id = req['transaction_id']
    changed_columns = req['changed_columns']
    changed_values = req['changed_values']

    conn = ConnectToDB()

    new_block_obj = reconstructObject(conn.getTransactionDetails(transaction_id = transaction_id), changed_columns, changed_values)

    #Send the updates to the peers for validation
    if(peerComm.sendChangeToPeers(new_block_obj)):
        if(new_block_obj != None):
            updateChange(new_block_obj)
            return {"response": "Transaction successfully updated."}
        else:
            return {"response": "Transaction cannot be updated."}
    else:
        return {"response": "Peers have not validated this transaction."}

    return {}

if __name__ == '__main__':
    app.run(debug=True)