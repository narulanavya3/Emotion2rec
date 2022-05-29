import os 
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create() 
path = 'dataset1'
def getImagesWithID(path):
	'''Get images from the dataset
       recognizer trains all the images 
	   make a yml file'''
	imagepaths = [os.path.join(path,f) for f in os.listdir(path)] 
	faces = []
	IDs = []
	for imagePath in imagepaths:
		faceimg = Image.open(imagePath).convert('L') 
		faceNp = np.array(faceimg,'uint8')       
		ID = int(os.path.split(imagePath)[-1].split('.')[1]) 
		faces.append(faceNp)
		print (ID)
		IDs.append(ID)
		cv2.imshow("training",faceNp)
		cv2.waitKey(10)
	return IDs,faces
IDs,faces = getImagesWithID(path)
recognizer.train(faces,np.array(IDs))
recognizer.save('recognizer/trainingData2.yml')  
cv2.destroyAllWindows()

