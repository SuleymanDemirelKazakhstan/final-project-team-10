## Machine learning part:
Adilbek Karmanov and Maxim Kolesnikov
- Refactor the image conversion code for our API
- Configure servers on Docker
- Try our model on CPU perfomance


## Frontend Part
Sergey Kirichenko
- Created confirm modal, when user entered all data correctly (like email, image upload and etc)
- Now client part can understand when images delivered to user via email
- Refactored BASE64Converter service

Next step:
- Finalize UI
- Set Angulars specs, like CORS, zone.js

## Backend part:
Myrzabek Darkhan
- Returned for REQUEST, but now request.js fully rewritten
- Connected with Atlas, now we store all images in Cloud and that's great!

Next step:
- Set res.send statuses, because for now, client not fully understand if image was transferred or we have some troubles
- Create email-send service, for sending emails
