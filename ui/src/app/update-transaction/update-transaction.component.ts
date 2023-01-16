/**
 * Author: Bharadwaj Prabhala (BP)
 */
import { Component } from '@angular/core';
import {Router} from '@angular/router';
import {ConfigService} from './../app.service';

@Component({
  selector: 'app-update-transaction',
  templateUrl: './update-transaction.component.html',
  styleUrls: ['./update-transaction.component.css']
})
export class UpdateTransactionComponent {
  configService: ConfigService
  fetch_transaction_id = ""
  formCompleted = false

  original_transaction = {}
  updated_transaction = {}
  apiResponse = ""

  constructor(configService: ConfigService, private router: Router){
    this.configService = configService
  }

  findTransaction() {
    this.configService.findTransaction(this.fetch_transaction_id).subscribe((response: any) => {
      this.updated_transaction = response['response']
      this.original_transaction = JSON.parse(JSON.stringify(this.updated_transaction))
    })

    
  }

  addTransaction() {
    this.router.navigate(['/add_transaction']);
  }

  submitUpdate(){
    if(this.updated_transaction['buyer_name'] == "" || this.updated_transaction['seller_name'] == "" || this.updated_transaction['address'] == "" || this.updated_transaction['area'] == 0 || this.updated_transaction['price_per_sft'] == 0 || this.updated_transaction['total_price'] == 0 || this.updated_transaction['registration_number'] == "" || this.updated_transaction['transaction_date'] == "" || this.updated_transaction['entrance_facing'] == "" || this.updated_transaction['survey_number'] == "" || this.updated_transaction['north_survey_number'] == "" || this.updated_transaction['south_survey_number'] == "" || this.updated_transaction['east_survey_number'] == "" || this.updated_transaction['west_survey_number'] == "" || this.updated_transaction['gst'] == 0 || this.updated_transaction['verified_by'] == ""){
      this.formCompleted = false
    }
    else{
      this.formCompleted = true
      var changed_columns = []
      var changed_values = []
      var cols = ['buyer_name', 'seller_name', 'address', 'area', 'price_per_sft', 'total_price', 'registration_number', 'transaction_date', 'entrance_facing', 'survey_number', 'north_survey_number', 'south_survey_number', 'east_survey_number', 'west_survey_number', 'gst', 'verified_by', 'litigations', 'transaction_date']

      for(var col of cols){
        if(this.updated_transaction[col] != this.original_transaction[col]){
          changed_columns.push(col)
          changed_values.push(this.updated_transaction[col])
        }
      }
      
      this.configService.updateTransaction(this.fetch_transaction_id, changed_columns, changed_values).subscribe((response: any) => {
        this.apiResponse = response["response"]
      })

    }
  }

  resetTransaction(){
    this.updated_transaction = this.original_transaction
  }

  isDataFetched(){
    if(Object.keys(this.updated_transaction).length == 0){
      return false 
    }
    return true
  }
  
}
