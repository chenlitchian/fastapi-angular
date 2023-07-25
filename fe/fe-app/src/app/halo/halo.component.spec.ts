import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HaloComponent } from './halo.component';

describe('HaloComponent', () => {
  let component: HaloComponent;
  let fixture: ComponentFixture<HaloComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [HaloComponent]
    });
    fixture = TestBed.createComponent(HaloComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
