# **NAME: PRIYANKA YEOLE**

# **Coding: utf-8

# **Problem Statement - Object Detection**


# Importing Required Libraries


import cv2
import imutils
import time
import numpy as np


# Loading Pre-Trained Data Set


net = cv2.dnn.readNetFromCaffe("MobileNetSSD_deploy.prototxt.txt","MobileNetSSD_deploy .caffemodel")
confThresh = 0.6


# Defining Object classes


classLabels =  ["background","aeroplane","bicycle","bird", "boat", "bottle", "bus", "car", "cat", "chair", "diningtable","wall", "horse","motorbike","person", "person", "pottedplant", "sheep", "sofa", "train", "monitor display"]
COLORS = np.random.uniform(0, 255, size=(len(classLabels),3 ))  


# Performing Detection


vs = cv2.VideoCapture("Video.mp4") 
while True:
    _,frame = vs.read()
    frame = imutils.resize(frame, width = 1000) 
    (h,w) = frame.shape[:2] 
    imResize = cv2.resize(frame, (300,300)) 
    blob = cv2.dnn.blobFromImage(imResize, 0.007843, (300,300), 127.5) 
    
    net.setInput(blob)
    detections = net.forward()
    
    detShape = detections.shape[2]
    for i in np.arange(0,detShape):
        confidence = detections[0, 0, i, 2]
        if confidence > confThresh:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            
            label = "{} : {:.2f}%".format(classLabels[idx],
                                          confidence * 100)
            cv2.rectangle(frame, (startX, startY), (endX, endY),
                         COLORS[idx], 2)
            if startY - 15 >15:
                y = startY - 15
            else:
                y = startY + 15
            cv2.putText(frame, label, (startX, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
    cv2.imshow("Detection Video", frame)
    if cv2.waitKey(1) & 0xFF == ord('e'):  
        break
    
vs.release()
cv2.destroyAllWindows()


# Thank You
