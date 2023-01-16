/**
 * Author: Bharadwaj Prabhala (BP)
 * Description: This component contains the fields that are required to add any real estate transaction to the ledger.
 */
import { Component, OnChanges, OnInit } from '@angular/core';
import {Transaction} from './../transaction';
import {ConfigService} from './../app.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-add-transaction',
  templateUrl: './add-transaction.component.html',
  styleUrls: ['./add-transaction.component.css']
})
export class AddTransactionComponent{
  transaction = new Transaction();
  formCompleted = false 
  configService: ConfigService
  apiResponse = ""

  constructor(configService: ConfigService, private router: Router){
    this.configService = configService
  }

  //Submit the transaction after verifying all the required fields are filled.
  submitTransaction(){
    if(this.transaction.buyer_name == "" || this.transaction.seller_name == "" || this.transaction.address == "" || this.transaction.area == 0 || this.transaction.price_per_sft == 0 || this.transaction.total_price == 0 || this.transaction.registration_number == "" || this.transaction.transaction_date == "" || this.transaction.entrance_facing == "" || this.transaction.survey_number == "" || this.transaction.north_survey_number == "" || this.transaction.south_survey_number == "" || this.transaction.east_survey_number == "" || this.transaction.west_survey_number == "" || this.transaction.gst == 0 || this.transaction.verified_by == ""){
      this.formCompleted = false
    }
    else{
      this.formCompleted = true
      this.configService.postFormData(this.transaction).subscribe((response: any) => {
        this.apiResponse = response["response"]
      })
    }
  }

  //Clear the form
  resetTransaction(){
    this.transaction = new Transaction();
    this.formCompleted = false 
    this.apiResponse = ""
  }

  //Go to the transaction update route.
  updateTransaction(){
    this.router.navigate(['/update_transaction']);
  }
}
