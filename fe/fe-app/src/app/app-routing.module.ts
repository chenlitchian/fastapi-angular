import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HaloComponent } from './halo/halo.component';
import { TestComponent } from './test/test.component';

const routes: Routes = [
  { path: 'new-page', component: HaloComponent }, // New route for your new page
  { path: 'home', component: TestComponent }, // Example: Existing route
  { path: '', redirectTo: '/home', pathMatch: 'full' }, // Default route
  { path: '**', redirectTo: '/home', pathMatch: 'full' }, // Redirect all other unknown routes to the home page
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
