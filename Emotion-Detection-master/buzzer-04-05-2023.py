'''
PyPower Projects
Emotion Detection Using AI
'''
import time
# import max30100
import time #import time for creating delay 
import Adafruit_DHT #Import DHT Library for sensor

#buzz
from gpiozero import Buzzer
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(26,GPIO.OUT)
buzzer = Buzzer(12)


from twilio.rest import Client 
 
import time
import subprocess



import RPi.GPIO as GPIO          
from time import sleep
in1 = 24
in2 = 23
en = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,1000)
p.start(50)
GPIO.output(24,GPIO.HIGH)
GPIO.output(23,GPIO.LOW)



#USAGE : python test.py
import tensorflow
from tensorflow.keras.models import load_model
from time import sleep
from tensorflow.keras.preprocessing.image import img_to_array
#from tensorflow.keras.utils import img_to_array
from tensorflow.keras.preprocessing import image
import cv2
import numpy as np

import os
from twilio.rest import Client

face_classifier = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
classifier =load_model('/home/pi/Desktop/mudassir/Emotion-Detection-master/Emotion_Detection.h5')

class_labels = ['pain','Happy','Neutral','pain','pain']

cap = cv2.VideoCapture(0)



while True:
    # Grab a single frame of video
    ret, frame = cap.read()
    labels = []
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_gray = cv2.resize(roi_gray,(48,48),interpolation=cv2.INTER_AREA)


        if np.sum([roi_gray])!=0:
            roi = roi_gray.astype('float')/255.0
            roi = img_to_array(roi)
            roi = np.expand_dims(roi,axis=0)

        # make a prediction on the ROI, then lookup the class

            preds = classifier.predict(roi)[0]
            print("\nprediction = ",preds)
            label=class_labels[preds.argmax()]
            print("\nprediction max = ",preds.argmax())
            print("\nlabel = ",label)
            if label== 'pain':
               # message = client.messages.create(body='your family member has got heartattack so he needs medical health immediately',from_='+12342306695',to='+918861245226')               
                GPIO.output(26,GPIO.HIGH)
                buzzer.on()
                time.sleep(1) 
                GPIO.output(26,GPIO.LOW)
                buzzer.off()
                GPIO.output(24,GPIO.LOW)
                GPIO.output(23,GPIO.LOW)
                print("sending message")
                time.sleep(5) 
                break
            label_position = (x,y)
            cv2.putText(frame,label,label_position,cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        else:
            cv2.putText(frame,'No Face Found',(20,60),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
        print("\n\n")
    cv2.imshow('Emotion Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break;

cap.release()
cv2.destroyAllWindows()






print("this is prog2")

#dht
sensor_name = Adafruit_DHT.DHT11 #we are using the DHT11 sensor
sensor_pin = 17

#heart beat
mx30 = max30100.MAX30100()
mx30.enable_spo2()


#motor
        

#sms
# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure
#account_sid = os.environ['AC7096cb8582933a886847cde06fde11f3']
#auth_token = os.environ['d6c6d87b3402538e47b5451769966f2a']
#client = Client(account_sid, auth_token)


while 1:
    
    humidity, temperature = Adafruit_DHT.read_retry(sensor_name, sensor_pin) #read from sensor and save respective values in temperature and humidity varibale  
    print('temperature',temperature)
    
    mx30.read_sensor()
    mx30.ir, mx30.red
    hb = int(mx30.ir / 100)
    spo2 = int(mx30.red / 100)
    GPIO.output(24,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)

#    moto('r')
#    data = db.reference('hakaton').get()
#    print(data['exp'])
#    if data['exp']=='pain':
#        x=1
#    else:
#        x=0
    if(100<hb):
        print("heart attack predicted pulse=",hb);
        print("LED on")
        GPIO.output(26,GPIO.HIGH)
        buzzer.on()
        time.sleep(1) 
        GPIO.output(26,GPIO.LOW)
        buzzer.off()
        GPIO.output(24,GPIO.LOW)
        GPIO.output(23,GPIO.LOW)
        time.sleep(0)
        hb=0
#        moto('slow')
        #message = client.messages.create(body='your family member has got heartattack so he needs medical health immediately',
              #      from_='+12342306695',to='+918861245226')               
        #print(message.sid)

        
        
    else:
        print("Pulse:",hb);
        
    if mx30.red != mx30.buffer_red:
        print("SPO2:",spo2);

#    time.sleep(0.1)



