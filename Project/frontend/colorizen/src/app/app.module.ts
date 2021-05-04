import { BrowserModule } from '@angular/platform-browser';
import {CUSTOM_ELEMENTS_SCHEMA, NgModule} from '@angular/core';

import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {UploaderAllModule} from '@syncfusion/ej2-angular-inputs';
import {CheckBoxAllModule} from '@syncfusion/ej2-angular-buttons';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatDialogModule} from '@angular/material/dialog';
import {UploadFormComponent} from './upload-form/upload-form.component';





@NgModule({
  declarations: [
    AppComponent,
    UploadFormComponent,

  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    UploaderAllModule,
    CheckBoxAllModule,
    BrowserAnimationsModule,
    MatDialogModule

  ],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
