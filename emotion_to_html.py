from statistics import mode
import dlib
import cv2
from keras.models import load_model
import numpy as np
import time
import requests

from utils.datasets import get_labels
from utils.inference import draw_text
from utils.inference import draw_bounding_box
from utils.inference import apply_offsets
from utils.preprocessor import preprocess_input

def rect_to_bb(rect):
    '''take a bounding predicted by dlib 
    convert it to the format (x, y, w, h) 
    return the tuple'''
    x = rect.left()
    y = rect.top()
    w = rect.right() - x
    h = rect.bottom() - y
    return (x, y, w, h)

def run_emotion_to_html():
    '''takes the yml file as input
       capture real-time video and predict emotion
       return the dominant emotion response to flask-server'''

    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # emotion_model_path = './trained_models/emotion_models/fer2013_mini_XCEPTION.102-0.66.hdf5'
    emotion_model_path = 'trained_models\emotion_models\simple_CNN.530-0.65.hdf5'
    rec = cv2.face.LBPHFaceRecognizer_create()
    rec.read("recognizer/trainingData2.yml")
    id = 0
    emotion_labels = get_labels('fer2013')

    frame_window = 10
    emotion_offsets = (20, 40)

    face_detection = dlib.get_frontal_face_detector()
    emotion_classifier = load_model(emotion_model_path, compile=False)
  
    emotion_target_size = emotion_classifier.input_shape[1:3]
    
    emotion_window = []

    cv2.namedWindow('window_frame')
    video_capture = cv2.VideoCapture(0)

    timer = time.time()
    response = "Null"

    while True:
        bgr_image = video_capture.read()[1]
        gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
        rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
        faces =  face_detection(gray_image, 1)
        start = 0

        for face_coordinates in faces:
            face_coordinates = rect_to_bb(face_coordinates)
            x1, x2, y1, y2 = apply_offsets(face_coordinates, emotion_offsets)
            gray_face = gray_image[y1:y2, x1:x2]
            id,conf = rec.predict(gray_image[face_coordinates[1]:face_coordinates[1]+face_coordinates[3],face_coordinates[0]:face_coordinates[0]+face_coordinates[2]])
            
            if id == 1:
                id = 'Navya'
            if id == 2:
                id = 'Pummy'
            try:
                gray_face = cv2.resize(gray_face, (emotion_target_size))
            except:
                continue

            gray_face = preprocess_input(gray_face, True)
            gray_face = np.expand_dims(gray_face, 0)
            gray_face = np.expand_dims(gray_face, -1)
            emotion_prediction = emotion_classifier.predict(gray_face)
            emotion_probability = np.max(emotion_prediction)
            emotion_label_arg = np.argmax(emotion_prediction)
            emotion_text = emotion_labels[emotion_label_arg]
            emotion_window.append(emotion_text)

            if len(emotion_window) > frame_window:
                start += 1
            try:
                emotion_mode = mode(emotion_window[start:])
            except:
                continue
            
            if emotion_text == 'angry':
                color = emotion_probability * np.asarray((255, 0, 0))
            elif emotion_text == 'sad':
                color = emotion_probability * np.asarray((0, 0, 255))
            elif emotion_text == 'happy':
                color = emotion_probability * np.asarray((255, 255, 0))
            elif emotion_text == 'neutral':
                color = emotion_probability * np.asarray((0, 255, 255))
            else:
                color = emotion_probability * np.asarray((0, 255, 0))
        
            color = color.astype(int)
            color = color.tolist()

            draw_bounding_box(face_coordinates, rgb_image, color)
            draw_text(face_coordinates, rgb_image, str(id)+' is '+str(emotion_mode),
                    color, 0, -45, 1, 1)
        
        if time.time() > timer + 10:
            most_common_emotion =  mode(emotion_window)
            emo_dict = {"emotions" : most_common_emotion}
            send_response = requests.get(url = 'http://127.0.0.1:5000/emotion', json = emo_dict)
            if send_response.ok:
                response = send_response.text
                break

        bgr_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2BGR)
        cv2.imshow('window_frame', bgr_image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
    video_capture.release()
    return(response)

if __name__ == '__main__':
    run_emotion_to_html()


