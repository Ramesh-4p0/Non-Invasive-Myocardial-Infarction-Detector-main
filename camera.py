

import cv2
import numpy as np
import dlib
from math import hypot
from imutils import face_utils

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    cv2.imshow("demo", frame)
    cv2.waitKey(1)    

