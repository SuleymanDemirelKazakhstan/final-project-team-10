## Machine learning part:
Adilbek Karmanov and Maxim Kolesnikov
- Refactor the video conversion code for our API (continue)


## Frontend Part
Kirichenko Sergey
- I took out the processing of photos on the client's side, because as it turned out, this does not require any power at all. Now when a user uploads a photo, we immediately convert it to base64 format.
- Solved the problem with uploading multiple photos at once. Turned out the problem was Mongodb. Now that the logic has been moved to the client side, the problem is resolved

Next step:
- Need to create UI




## Backend part:
Myrzabek Darkhan
- Completely overhauled the old backend because it didn't work for us. Now we can save photos in mongodb in base64 format, send them for processing, receive new photos, save them to the database and send them to the user by mail

Next step:
- It is necessary to add information content, because now it is not entirely clear which of their methods worked correctly and which one with an error.
- We need to move all services into separate methods, because now it looks like spaghetti code
