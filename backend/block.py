"""
Author: Bharadwaj Prabhala (BP)
Module: This module contains the methods required to generate blocks and their hashes
"""
import hashlib
from db import ConnectToDB

class Block:
    def __init__(self):
        self.connectToDb = ConnectToDB()
        self.conn = self.connectToDb.getConn()
    
    #Generate a hash from the entire row using SHA-256
    def generateHash(self, transaction):
        return hashlib.sha256(str(transaction).encode("utf-8")).hexdigest()

    #Block will contain the transaction_id which is an incremental number based on the max value in the DB, previous block hash (init in case it's the first block), current block hash (generated using SHA-256) and the transaction details.
    def generateBlock(self, transaction):
        cur = self.conn.cursor()
        cur.execute("select max(transaction_id) from golden_transaction_ledger")
        max_trans_id = cur.fetchone()[0]
        if(max_trans_id == None):
            max_trans_id = 0
        
        transaction_id = max_trans_id + 1
        cur.close()

        #Generate a block
        new_transaction = (transaction_id, self.connectToDb.getLastBlock(), self.generateHash(transaction), transaction)

        #If the previous hash is same as the new hash, it means no data changed so will return None.
        if(new_transaction[1] == new_transaction[2]):
            return None
        return new_transaction
