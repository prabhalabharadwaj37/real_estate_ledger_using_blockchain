"""
Author: Bharadwaj Prabhala (BP)
Module: This module contains the logic to add or retrieve data from the Postgres DB.
"""
import psycopg2
from datetime import datetime
import configparser

class ConnectToDB:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.readfp(open(r'config.txt'))

        #Retrieve these from the configuration once the postgres db is setup
        self.conn = psycopg2.connect(host=config.get('db', 'db_hostname'),database=config.get('db', 'db_name'),user=config.get('db', 'db_username'),password=config.get('db', 'db_pass'))

    #Method to get the connection object
    def getConn(self):
        return self.conn

    # Get the last block from the ledger
    def getLastBlock(self, table_name = 'golden_transaction_ledger'):
        cur = self.conn.cursor()
        cur.execute("select curr_block_hash from {} order by transaction_id desc".format(table_name))
        hash = cur.fetchone()
        if(hash == None):
             hash = ("init", )
        
        cur.close()
        return hash[0]

    # Write the transaction to the database. If it's a new transaction, then transType will be insert, else if it's an update, then transType will be update.
    def saveToDB(self, block, table_name = 'golden_transaction_ledger', transType='insert'):
        cur = self.conn.cursor()
        prev_block_hash = block[1]
        curr_block_hash = block[2]
        
        query = ""
        if(transType == "insert"):
            query = "insert into {} values({}, '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(table_name, block[0], prev_block_hash, curr_block_hash, block[3]['buyer_name'], block[3]['seller_name'], block[3]['address'], block[3]['area'], block[3]['price_per_sft'], block[3]['total_price'], block[3]['gst'], datetime.strptime(block[3]['transaction_date'], "%Y-%m-%d"), block[3]['registration_number'], block[3]['litigations'], block[3]['entrance_facing'], block[3]['survey_number'], block[3]['north_survey_number'], block[3]['south_survey_number'], block[3]['east_survey_number'], block[3]['west_survey_number'], block[3]['verified_by'])
        
        #For update, we have to delete the existing rows and recreate them. 
        elif(transType == "update"):
            cur.execute("delete from {} where transaction_id={}".format(table_name, block[0]))
            self.conn.commit()
            #Call the method again to insert the updated transaction
            self.saveToDB(block, table_name, "insert")

        try:
            if(query != ""):
                cur.execute(query)
                self.conn.commit()
                print("Successfully added a new block")
            else:
                print("Empty query")
                cur.close()
        except Exception as e:
            print(e)
            cur.close()
            print("Failed to add a new block")

    #Get an individual transaction details
    def getTransactionDetails(self, transaction_id, table_name = 'golden_transaction_ledger'):
        cur = self.conn.cursor()

        query = "select * from {} where transaction_id={}".format(table_name, transaction_id)
        cur.execute(query)

        transaction_details = cur.fetchone()
        cur.close()
        return transaction_details

    #Get all the transactions after the transaction that has updated.
    def getAllSubsequentTransactions(self, transaction_id, table_name = 'golden_transaction_ledger'):
        cur = self.conn.cursor()

        query = "select * from {} where transaction_id>{}".format(table_name, transaction_id)
        cur.execute(query)

        subsequent_transactions = cur.fetchall()
        cur.close()
        return subsequent_transactions