# emotion2rec

-A project on Personalization and targeted recommendations using computer vision.

## Dependencies:

-Install tensorflow gpu on your cmd to install the dependencies

- Python 3.9.12
- dlib
- numpy
- cv2
- Pillow
- os
- Tkinter
- flask
- requests

## Procedure

-Clone the repository https://github.com/narulanavya3/Emotion2rec.git

-Run on terminal 'flask run' and leave it running 

-On another terminal run the command 'python gui.py'

-click on the option Add new face and type in an id and click on submit.
  Wait for the camera to click images.
  
   <img src= 'https://user-images.githubusercontent.com/74983170/170884666-7517b9c1-8b81-4a23-9189-e521d5522791.png' width='600px'>
   
   Yow will see the images are being stored in the dataset
   
   <img src= 'https://user-images.githubusercontent.com/74983170/170884787-ee7f10a9-4ce3-4b27-bede-c589c5d0adba.png' width = '200px'>

-Click on Train face recognition model and wait for the model to train the images in the dataset.

<img src='https://user-images.githubusercontent.com/74983170/170884979-586bdf2d-245f-4315-ba30-e697a0ca8715.png' width = '600px'>

-After training is complete, click on Run application, the camera window will open for about 10 seconds to recognize face and emotions.

<img src= 'https://user-images.githubusercontent.com/74983170/170885201-fb814686-03d3-4e2f-b9fa-f81da877ddb9.png' width = '600px'>

  After 10 seconds, the dominant emotion will be sent to the flask-server which was running on the terminal
  flask will process it and return a specific recommendation for a playlist and a new pop window will automatically open pre-loading 
  that playlist designed especially  for the user.
  
  <img src='https://user-images.githubusercontent.com/74983170/170885258-9694d323-3c25-44b6-9432-25170200d60d.png' width ='600px'>

## Vote of Thanks
-Orriaga/face classification for providing the source to a pre-trained CNN-based emotion model
the link for the same is given below
(https://github.com/oarriaga/face_classification/blob/master/trained_models/emotion_models/simple_CNN.530-0.65.hdf5)

  


