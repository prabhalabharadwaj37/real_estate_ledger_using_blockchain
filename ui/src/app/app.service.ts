import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';


@Injectable()
export class ConfigService {
  constructor(private http: HttpClient) { }

  //Add a transaction in the ledger
  postFormData(formData): Observable<any> {
    const url = "http://localhost:5000/add_transaction"
    let headers = new HttpHeaders({'Content-Type': 'application/json'});
    let options = {headers: headers}
    return this.http.post<any>(url, formData, options)
  }

  //Find the transaction in the ledger using transaction ID
  findTransaction(transaction_id): Observable<any> {
    const url = "http://localhost:5000/find_transaction_by_id"
    let headers = new HttpHeaders({'Content-Type': 'application/json'});
    let options = {headers: headers}
    return this.http.post<any>(url, {"transaction_id": transaction_id}, options)
  }

  //Update the transaction in the ledgers after peer authorization which is handled in the backend
  updateTransaction(transaction_id, changed_columns, changed_values): Observable<any> {
    const url = "http://localhost:5000/update_transaction"
    let headers = new HttpHeaders({'Content-Type': 'application/json'});
    let options = {headers: headers}
    return this.http.post<any>(url, {"transaction_id": transaction_id, "changed_columns": changed_columns, "changed_values": changed_values}, options)
  }
}