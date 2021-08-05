import cv2
import numpy as np


cap = cv2.VideoCapture("video1.MP4")
cap.set(3,60)
cap.set(4,100)
cap.set(10,100)



while True:
    check,img=cap.read()
    #print(frame)
    print(check)
    img2 = img.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = cv2.line(img, (0, 0), (500, 500), (250, 0, 0), 10)
    img = cv2.circle(img, (400,300), 180, (250, 0, 0), 15)
    img = cv2.rectangle(img, (50, 50), (700, 600), (0, 200, 250), 10)
    print(img.shape)


    font = cv2.FONT_HERSHEY_SIMPLEX
    img=cv2.putText(img,'hi bangladesh ',(10,500),font ,4,(0,0,255),10)


    cv2.imshow('this is gray version ',img)
    cv2.imshow('this is gray version j ', img2)

    #cv2.waitKey(100)  # 1sec= 1k milisec
    if cv2.waitKey(1) & 0XFF== ord('q'):
        break

cv2.destroyAllWindows()



