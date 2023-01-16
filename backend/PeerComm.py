"""
Author: Bharadwaj Prabhala (BP)
Module: This module contains the methods to communicate between peers.
"""
import requests
import configparser

class PeerComm:
    def __init__(self):
        config = configparser.RawConfigParser()
        config.readfp(open(r'config.txt'))
        #Dummy peering servers. 
        self.peers = [config.get('peers', 'peer1_hostname'), config.get('peers', 'peer2_hostname'), config.get('peers', 'peer3_hostname')]

        print(self.peers)
        self.valid = []

    #Sending the new transactions to the peers to update at their end
    def sendToPeers(self, block):
        for peer in self.peers:
            self.valid.append(requests.post(peer+"verify_new_transaction", json={"id": block[0], "prev_block_hash": block[1], "curr_block_hash": block[2], "transaction_details": block[3]}).json()['response'])

        if(False in self.valid):
            self.valid = []
            return False
        else:
            return True

    #Sending the transaction updates to the peers to validate the changes
    def sendChangeToPeers(self, block):
        for peer in self.peers:
            self.valid.append(requests.post(peer+"verify_change", json={"id": block[0], "prev_block_hash": block[1], "curr_block_hash": block[2], "transaction_details": block[3]}).json()['response'])

        if(False in self.valid):
            self.valid = []
            return False
        else:
            return True

    #If the peers validate a change, sending them a signal to update the transactions at their end
    def updateChange(self, block):
        for peer in self.peers:
            requests.post(peer+"update_change", json={"id": block[0], "prev_block_hash": block[1], "curr_block_hash": block[2], "transaction_details": block[3]}).json()['response']