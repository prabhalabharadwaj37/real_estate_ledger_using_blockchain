import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { UpdateTransactionComponent } from 'src/app/update-transaction/update-transaction.component';
import { AppComponent } from 'src/app/app.component';
import { AddTransactionComponent } from 'src/app/add-transaction/add-transaction.component';

const routes: Routes = [
  {path: '', redirectTo: '/add_transaction', pathMatch: 'full'},
  {path: 'add_transaction', component: AddTransactionComponent},
  {path: 'update_transaction', component: UpdateTransactionComponent}
 ]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {

  
}
