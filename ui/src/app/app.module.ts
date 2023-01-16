import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { ConfigService } from 'src/app/app.service';
import { UpdateTransactionComponent } from './update-transaction/update-transaction.component';
import { RouterModule } from '@angular/router';
import { AddTransactionComponent } from './add-transaction/add-transaction.component';


@NgModule({
  declarations: [
    AppComponent,
    UpdateTransactionComponent,
    AddTransactionComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [ConfigService],
  bootstrap: [AppComponent]
})
export class AppModule { }
