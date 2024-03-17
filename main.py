import cv2
import numpy as np
import os 
import pickle
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-system-7861d-default-rtdb.firebaseio.com/",
    'storageBucket' : "face-attendance-system-7861d.appspot.com"
})

bucket=storage.bucket()


recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
font = cv2.FONT_HERSHEY_SIMPLEX

id = 0

names = ['None', 'Arijit','Abhishek','Elon Musk'] 

cam = cv2.VideoCapture(0)
cam.set(3, 640) 
cam.set(4, 480) 

minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
         
        if (confidence < 100):
                                                                                          
            confidence = "  {0}%".format(round(100 - confidence))
            studentInfo=db.reference(f'Students/{id}').get()
           
            datetimeObject=datetime.strptime(studentInfo['last_attendance_time'],
                                                "%Y-%m-%d %H:%M:%S")
            secondsElapsed= (datetime.now()-datetimeObject).total_seconds()

            if secondsElapsed> 30:
                ref=db.reference(f'Students/{id}')
                studentInfo['total_attendance']+=1
                ref.child('total_attendance').set(studentInfo['total_attendance'])
                ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                
                

            # else:
            #     cv2.putText(
            #         img, 
            #         str('Already Marked'), 
            #         (x+5,y-5+h), 
            #         font, 
            #         1, 
            #         (255,255,255), 
            #         2
            #     )    


        
        
        cv2.putText(
                    img, 
                    str(names[id]), 
                    (x+5,y-5), 
                    font, 
                    1, 
                    (255,255,255), 
                    2
                   )
        
    
    cv2.imshow('camera',img) 
    k = cv2.waitKey(10) & 0xff 
    if k == 27:
        break

print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()