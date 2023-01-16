create table public.golden_transaction_ledger(
transaction_id int primary key, prev_block_hash varchar(80), curr_block_hash varchar(80), buyer_name varchar(100), seller_name varchar(100), 
address varchar(200), area float, price_per_sft float, total_price float, gst float, transaction_date date, registration_number varchar(30), 
litigations varchar(1000), entrance_facing varchar(30), survey_number varchar(30), north_survey_number varchar(30), south_survey_number varchar(30), 
east_survey_number varchar(30), west_survey_number varchar(30), verified_by varchar(100)
);

create table public.peer1_ledger(
transaction_id int primary key, prev_block_hash varchar(80), curr_block_hash varchar(80), buyer_name varchar(100), seller_name varchar(100), 
address varchar(200), area float, price_per_sft float, total_price float, gst float, transaction_date date, registration_number varchar(30), 
litigations varchar(1000), entrance_facing varchar(30), survey_number varchar(30), north_survey_number varchar(30), south_survey_number varchar(30), 
east_survey_number varchar(30), west_survey_number varchar(30), verified_by varchar(100)
);

create table public.peer2_ledger(
transaction_id int primary key, prev_block_hash varchar(80), curr_block_hash varchar(80), buyer_name varchar(100), seller_name varchar(100), 
address varchar(200), area float, price_per_sft float, total_price float, gst float, transaction_date date, registration_number varchar(30), 
litigations varchar(1000), entrance_facing varchar(30), survey_number varchar(30), north_survey_number varchar(30), south_survey_number varchar(30), 
east_survey_number varchar(30), west_survey_number varchar(30), verified_by varchar(100)
);

create table public.peer3_ledger(
transaction_id int primary key, prev_block_hash varchar(80), curr_block_hash varchar(80), buyer_name varchar(100), seller_name varchar(100), 
address varchar(200), area float, price_per_sft float, total_price float, gst float, transaction_date date, registration_number varchar(30), 
litigations varchar(1000), entrance_facing varchar(30), survey_number varchar(30), north_survey_number varchar(30), south_survey_number varchar(30), 
east_survey_number varchar(30), west_survey_number varchar(30), verified_by varchar(100)
);