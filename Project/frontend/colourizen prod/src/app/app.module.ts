import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';


import { AppComponent } from './app.component';
import { LandingComponent } from './landing/landing.component';
import {PreloadAllModules, RouterModule, Routes} from "@angular/router";

const appRoutes: Routes = [
  {
    path: '/test',
    component: LandingComponent
  }

];

@NgModule({
  declarations: [
    AppComponent,
    LandingComponent
  ],
  imports: [
    BrowserModule,
    RouterModule.forRoot(appRoutes, {
      initialNavigation: 'enabled',
      preloadingStrategy: PreloadAllModules,
    }),
  ],
  exports: [RouterModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
