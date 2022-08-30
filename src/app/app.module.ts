import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { MainpageComponent } from './mainpage/mainpage.component';
import { MatButtonModule } from '@angular/material/button';
import { LpcheckbuttonComponent } from './lpcheckbutton/lpcheckbutton.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatCardModule} from '@angular/material/card';
import { ToggleRankComponent } from './toggle-rank/toggle-rank.component';


@NgModule({
  declarations: [
    AppComponent,
    MainpageComponent,
    LpcheckbuttonComponent,
    ToggleRankComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    MatButtonModule,
    BrowserAnimationsModule,
    MatCardModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
