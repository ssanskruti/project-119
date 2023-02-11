import cv2
import time
import math

video = cv2.VideoCapture("footvolleyball.mp4")
tracker=cv2.TrackerCSRT_create()
ret,frame=video.read()
bbox=cv2.selectROI("tracking",frame,False)
tracker.init(frame,bbox)

def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3,1)
    cv2.putText(img,"Tracking",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(255,0,0),2)

while True:
    check,img = video.read() 

    success,bbox=tracker.update(img)  

    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"Lost",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
    
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



