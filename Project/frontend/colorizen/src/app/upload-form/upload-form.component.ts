import {Component, OnInit} from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';
import {MatDialog} from '@angular/material/dialog';


@Component({
  selector: 'app-upload-form',
  templateUrl: './upload-form.component.html',
  styleUrls: ['./upload-form.component.scss']
})


export class UploadFormComponent implements OnInit {

  imageCount;
  userEmail;
  arrayOfImages: any[] = []
  // @ts-ignore
  form: FormGroup

  // @ts-ignore


  constructor(private http: HttpClient, private dialog:MatDialog, private formBuilder: FormBuilder) { }

  ngOnInit(): void {


    this.form = this.formBuilder.group({
      emailInput: ['', Validators.required],
      imageInput: ['', Validators.required]
    })
  }

  resetForm() {
    this.form.reset()
  }


  handleUpload(event) {
    console.log(event.target.files)
    this.imageCount = event.target.files.length

    var p = 0
    var i;
    for (i = 0; i < event.target.files.length; i++) {
      const reader = new FileReader();
      reader.readAsDataURL(event.target.files[i]);
      reader.onload = () => {
        // @ts-ignore
        let base64result = reader.result.split(',')[1];
        this.arrayOfImages.push({ 'id': p++, "image": base64result })
        console.log(this.arrayOfImages)
      };
    }
  }

  getHello() {
    this.http.get('http://localhost:8080/api/testInfo').subscribe(data=>{
      console.log(data)
    })
    setTimeout(()=>{
      this.form.reset()
      this.imageCount = false
    }, 2000)
  }

  sendNudes() {
    let body = this.arrayOfImages

    this.http.post('http://localhost:8080/api/newPhotoUpload', {
      "email": this.userEmail,
      "data": this.arrayOfImages
    }).subscribe(data=>{
      console.log(data)
    })
    console.log('типа отправил')
    this.resetForm()
  }


}




