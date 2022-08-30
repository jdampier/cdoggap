import { Component, Injectable, OnInit } from '@angular/core';
import { MainpageComponent } from '../mainpage/mainpage.component';
import { Router } from '@angular/router';
import { ToggleRankComponent } from '../toggle-rank/toggle-rank.component';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import { application } from 'express';

@Injectable()


@Component({
  selector: 'app-lpcheckbutton',
  templateUrl: './lpcheckbutton.component.html',
  styleUrls: ['./lpcheckbutton.component.css']
})
export class LpcheckbuttonComponent implements OnInit {

  holder: any | undefined;
  fileName?: any;

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  onFileSelected(event: any) {
    const file:File = event.target.files[0];
      if (file) {
        const r = new FileReader()
        r.onload = () => {
          const array = new Uint8Array(r.result as ArrayBuffer);
        }
        r.readAsArrayBuffer(file)
        this.fileName = file.name
        console.log(file)
      }
  }

  
  redirect() {

  }
}
