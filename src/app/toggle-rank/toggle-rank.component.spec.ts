import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ToggleRankComponent } from './toggle-rank.component';

describe('ToggleRankComponent', () => {
  let component: ToggleRankComponent;
  let fixture: ComponentFixture<ToggleRankComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ToggleRankComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ToggleRankComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
