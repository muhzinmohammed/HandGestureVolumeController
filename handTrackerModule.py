import cv2
import mediapipe as mp 


class handDetector():
    def __init__(self, mode=False,maxHands=2,complexity=1,detectionCon=0.5,trackCon=0.5) :
        self.mode=mode
        self.maxHands=maxHands
        self.complexity=complexity
        self.detectionCon=detectionCon
        self.trackCon=trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.complexity,self.detectionCon,self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
        # print(result.multi_hand_landmarks)

        if self.result.multi_hand_landmarks:
            for hand in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,hand,self.mpHands.HAND_CONNECTIONS)

        return img
    
    def handDetails(self,img,handNo=0,draw=True):
        landMarks = []
        
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[handNo]
            for id,landMark in enumerate(hand.landmark):
                h,w,c = img.shape
                cx,cy = int(landMark.x*w), int(landMark.y*h)
                landMarks.append([id,cx,cy])
                if draw:
                    cv2.circle
        return landMarks

