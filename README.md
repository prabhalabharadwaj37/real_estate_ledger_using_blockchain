# Real Estate Ledger using Blockchain 

## Background
There are thousands of real estate transactions that happen every day across India. Most of them involve transfer of land ownership. However, due to poor oversight and missing or falsified link documents, many of the land owners face litigations due to no fault of their own. It's suprising to see how easily land papers are modified to suit the a particular individual and allow for illegal occupation. 

## Solution
The solution to this problem requires a system that records every transantion and ensures integrity without manual intervention. As a result, I've tried to solve this problem by using Blockchain. The agents input their data via the UI and submit the transaction. Once the transaction is submitted, any alteration to the property details will result in a new hash being created, thereby enabling us to identify any malicious intent. 

## Technical Aspects
## UI: Angular 11.2
## Backend: Python 3.6
## Database: Postgres

#Running the application
## Create DB and tables
- Create a postgres DB with 4 tables using backend/dbCreate.sql (Change name if needed in the code. Peer ledgers should be running on different DB instances.)
    - golden_transaction_ledger
    - peer1_ledger
    - peer2_ledger
    - peer3_ledger

## Start the servers
- cd ui/
- ng serve
- cd ..
- python3 api.py
- python3 peer1.py
- python3 peer2.py
- python3 peer3.py

## Navigating
- By default the UI loads the add_transaction route
- Enter all the details and submit
    - This should make an entry in all the ledgers with the transaction_id and hashes created. If any new details need to be added, changes must be done to the DB, UI, API layers. 
- Click on Update Transaction and query by the transaction_id. 
- Once fetched, edit the required details and submit. This should update the DB if all peers validate the change. 
