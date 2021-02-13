from imutils.video import VideoStream
import imutils
import cv2,os,urllib.request
import numpy as np
from django.conf import settings

from .models import MyData

haar_cascade = cv2.CascadeClassifier("C://Users//Vipin Kumar//Desktop//Attendance_Management//Face_recognizer//model//haarcascade_frontalface_default.xml")
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C://Users//Vipin Kumar//Desktop//Attendance_Management//Face_recognizer//model//face_trained.yml')
people = ['Abhishek', 'Unknown', 'Vipin']
class webCamera(object):
	def __init__(self):
		self.video = cv2.VideoCapture(0)

	def __del__(self):
                #cap.release()
                cv2.destroyAllWindows()
		#self.video.release()

	def get_frame(self):
		success, image = self.video.read()
		# We are using Motion JPEG, but OpenCV defaults to capture raw images,
		# so we must encode it into JPEG in order to correctly display the
		# video stream.
		flip = cv2.flip(image,1)
		#cv.imwrite("frame%d.jpg" % count,image)     # save frame as JPG file

		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		
		faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
		for (x, y, w, h) in faces:
                        faces_roi=gray[y:y+h,x:x+w]
                        label, confidence = face_recognizer.predict(faces_roi)
                        


                        if (confidence>.6):
                                s=MyData()
                                
                                s.Student=str(people[label])
                                #print(s.Student)
                                s.save()
                                #print(s)
                                #print(s.save())
                                
                        #print(f'Label = {people[label]} with a confidence{confidence}')
			#text = "{}: {:.2f}%".format(name, proba * 100)
                        
                        
                        cv2.putText(image, str(people[label]), (x,y), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
                        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), thickness=2)
                        #cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
		#frame_flip = cv2.flip(image,1)frame_flip
		ret, jpeg = cv2.imencode('.jpg', image)
		return jpeg.tobytes()
