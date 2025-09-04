import keyboard
import cv2 as cv
import numpy as np
import handTrackerModule as htm
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


running = True
cap = cv.VideoCapture(0)

detector = htm.handDetector(detectionCon=0.9)
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface,POINTER(IAudioEndpointVolume))
minVolume = volume.GetVolumeRange()[0]
maxVolume = volume.GetVolumeRange()[1]

keyboard.add_hotkey('ctrl+q+w',lambda: globals().update(running=False))

while running:
    success, img = cap.read()
    img1 = detector.findHands(img)
    landmarks = detector.handDetails(img1)
    if len(landmarks)>0:
        x1,y1 = landmarks[4][1], landmarks[4][2]
        x2,y2 = landmarks[8][1], landmarks[8][2]
        cv.circle(img1,(x1,y1),15,(255,0,255),cv.FILLED)
        cv.circle(img1,(x2,y2),15,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(100,120,100),3)
        length = math.hypot(x2-x1,y2-y1)
        vol = np.interp(length,[15,150],[minVolume,maxVolume])
        volume.SetMasterVolumeLevel(vol, None)

cap.release()
cv.destroyAllWindows()

