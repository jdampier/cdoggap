import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LpcheckbuttonComponent } from './lpcheckbutton.component';

describe('LpcheckbuttonComponent', () => {
  let component: LpcheckbuttonComponent;
  let fixture: ComponentFixture<LpcheckbuttonComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ LpcheckbuttonComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LpcheckbuttonComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
