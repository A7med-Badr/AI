import cv2
import os 
from datetime import datetime
import FaceRecognitionModule as frm 
import FirebaseModule as fbm 

import LedModule as lm 
from time import sleep

frameWidth = 640
frameHeight= 480
## for Raspberry Pi V2 Camera 
flip =  0
camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(frameWidth)+', height='+str(frameHeight)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
cap = cv2.VideoCapture(camSet)
encodeList, classNames = frm.findEncodings("ImagesAttendance")
myLed = lm.ledRBG(17,27,22)
myLed.color('off')


def markAttendance(name):
    myLed.color('green')

    with open('Attendance.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'{name},{dtString}\n')
            fbm.postData(name,dtString)

while True:
    sccuess, img = cap.read()
    imgFaces, names = frm.recognizeFaces(img, encodeList, classNames,0.2)
    for name in names:
        if name == "unknown":
            myLed.color('red')
            sleep(0.2)
        else:
            markAttendance(name)
    myLed.color('off')
    #cv2.imshow("Image",imgFaces)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break