const express = require('express');
const bodyParser = require('body-parser');
const mongo = require("mongoose");
const cors = require('cors')
    // const request = require('request');
const rp = require('request-promise');
const nodemailer = require('nodemailer');
var base64Img = require('base64-img');

let toAdd;

let transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: {
        user: 'colorizenio@gmail.com',
        pass: 'DiplomaProject2021'
    }
});


const db = mongo.connect("mongodb://localhost:27017/HUETA?authSource=admin", function(err, response) {
    if (err) {
        console.log(err);
    } else {
        console.log('Connected to MongoDB');
    }
});

mongo.set('useFindAndModify', false);
mongo.set('useUnifiedTopology', true);

const app = express()
app.use(bodyParser.json({ limit: '50mb' }));
app.use(bodyParser.urlencoded({ limit: '50mb', extended: true }));

app.use(cors())

app.use(function(req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With,content-type');
    res.setHeader('Access-Control-Allow-Credentials', true);
    next();
});

const Schema = mongo.Schema;

const UsersDataSchema = new Schema({
    email: { type: String },
    data: [{}],
    readyData: [{}]
}, { versionKey: false });


const model = mongo.model('users', UsersDataSchema, 'users');

app.post("/api/newPhotoUpload", function(req, res) {
    const email = req.body.email
    const data = req.body.data
    toAdd = {
        email,
        data
    }
    const mod = new model(toAdd);

    // console.log('model', mod)

    mod.save(function(err, data) {
        if (err) {
            res.send(err);
        } else {
            res.send(data);
        }
    });

    // console.log('maxim', toAdd)

    var options = {
        method: 'POST',
        uri: 'http://192.168.1.223:8000/colorize',
        body: toAdd,
        json: true // Automatically stringifies the body to JSON
    };

    rp(options)
        .then(function(parsedBody) {
            // POST succeeded...
            console.log("Model got data, everything is great")
        })
        .catch(function(err) {
            // POST failed...
            console.log("Houston, we have problems", err)
        });

})

app.get("/api/testInfo", function(req, res) {
    data = {
        "test": 'hello world!'
    }
    res.send(data)
});


app.put("/api/photosDone/:email", function(req, res) {
    const email = req.params.email
    model.findOneAndUpdate({ email: email }, { readyData: req.body.readyData }, function(err, result) {
        if (err) {
            res.send(err);
        } else {
            model.findOne({ email: email }, function(err, result) {
                if (err) return console.log(err);
                res.send("Data is updated");
            });
        }
    });

    if (req.body.readyData != null) {
        console.log('Got data from model')
    }

    let readyForSending = []

    for (i = 0; i < req.body.readyData.length; i++) {
        const data = 'data:image/jpg;base64,' + req.body.readyData[i];
        const destpath = '';
        const filename = `${email}_new_photo_${i}`;

        base64Img.img(data, destpath, filename, (err, filepath) => {})
        readyForSending.push({ "filename": `${filename}.jpg`, "path": __dirname + `/${filename}.jpg` })
    }

    console.log('ready', readyForSending)



    let mailContent = {
        from: 'Colorizen',
        to: email,
        subject: 'Your Photos Are Ready!',
        text: 'Hi, Its me - Colorizen. Im glad to say that yours photos are ready! And they are awesome!',
        html: '',
        attachments: readyForSending
    };

    transporter.sendMail(mailContent, function(error, data) {
        if (error) {
            console.log('Unable to send mail', error);
        } else {
            console.log('Email send successfully', email);
        }
    });

})



app.listen(8080, function() {

    console.log('Colorizen HERE! Port: 8080')
})