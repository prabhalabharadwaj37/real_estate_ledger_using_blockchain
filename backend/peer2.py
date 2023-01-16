"""
Author: Bharadwaj Prabhala (BP)
Module: One of the peers in the network that has the capability to authorize a transaction.
"""
from flask import Flask
from flask import request, abort, make_response, jsonify
import json
from db import ConnectToDB
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# Default endpoint
@app.route('/')
def index():
    return "Welcome to the Real Estate Ledger on Peer 2!"

# Verify Transaction
@app.route("/verify_new_transaction", methods=['POST'])
def add_transaction():
    conn = ConnectToDB()

    new_block = request.json
    latest_block_hash = conn.getLastBlock(table_name="peer2_ledger")

    #Checking if the current ledger's previous block's hash is same as what is sent by the golden.
    if(new_block['prev_block_hash'] == latest_block_hash):
        conn.saveToDB((new_block['id'], new_block['prev_block_hash'], new_block['curr_block_hash'], new_block['transaction_details']), table_name="peer2_ledger")
        return {"response": True}
    else:
        return {"response": False}

# Verify Transaction Update
@app.route("/verify_change", methods=['POST'])
def verify_change():
    #The supporting documentation for the change need to be manually verified by peers and then the appropriate response must be sent. Since that is not possible for this PoC, we're using a random number to determine the response validity.
    rand = random.randint(0, 11)

    #This will always yield true. Change condition to test when the response is False.
    if(rand % 2 != 7):
        return {"response": True}
    else:
        return {"response": False}

# Update change
@app.route("/update_change", methods=['POST'])
def update_change():
    conn = ConnectToDB()

    new_block = request.json
    
    conn.saveToDB((new_block['id'], new_block['prev_block_hash'], new_block['curr_block_hash'], new_block['transaction_details']), table_name="peer2_ledger", transType="update")
    
    return {"response": "Successfully updated in Peer 2."}
    
if __name__ == '__main__':
    app.run(debug=True, port="5002")