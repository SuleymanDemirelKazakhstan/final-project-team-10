import { BrowserModule } from '@angular/platform-browser';
import {CUSTOM_ELEMENTS_SCHEMA, NgModule} from '@angular/core';

import { AppComponent } from './app.component';

import {AngularFileUploaderModule} from "angular-file-uploader";
import { DropzoneDirective } from './dropzone.directive';
import { UploaderComponent } from './uploader/uploader.component';


@NgModule({
  declarations: [
    AppComponent,

    DropzoneDirective,
    UploaderComponent,

  ],
    imports: [
        BrowserModule,
        AngularFileUploaderModule
    ],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
