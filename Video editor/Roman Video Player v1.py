#author: rokon-uz-zaman roman
#Blank and white image converter

import tkinter as tk
import cv2
from tkinter import filedialog
import numpy as np
import pyautogui 





########## Front End##############
root=tk.Tk()
root.geometry("400x300") #window size

label1=tk.Label(root,text='Roman Video Player',width=40)
label1.grid(row=1,column=1)


button1=tk.Button(root,text='Select a video file to play ',width=30,command=lambda:fileUpload())
button1.grid(row=2,column=1)


def fileUpload():
    uploaded=filedialog.askopenfilename()
    #img=cv2.imread(uploaded,0)
    #cv2.imshow('blank and white image',img)
    print(uploaded)
    #cap = cv2.VideoCapture("video1.MP4")
    url=f'{uploaded}'
    print(url)
    #cap = cv2.VideoCapture("C:/Users/Roman/PycharmProjects/video player/video1.mp4")
    cap = cv2.VideoCapture(url)
    #cap.set(3,60)
    #cap.set(4,100)
    #cap.set(10,100)
    while True:
        check,img=cap.read()
        print(img)
        #print(check)
        #img2 = img.copy()
        if cv2.waitKey(100) & 0XFF== ord('g'):
         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         img=cv2.putText(img,' This is Gray ',(300,150),font ,2,(0,0,255),10)
        if cv2.waitKey(100) & 0XFF== ord('h'):
         img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
         img=cv2.putText(img,' This is HSV ',(300,150),font ,2,(0,0,255),10)
        if cv2.waitKey(100) & 0XFF== ord('s'):
         cv2.waitKey(1000000)
         img=cv2.putText(img,' This is Slow motion ',(300,150),font ,2,(0,0,255),10) 
        
         
        #img = cv2.line(img, (0, 0), (500, 500), (250, 0, 0), 10)
        #img = cv2.circle(img, (400,300), 180, (250, 0, 0), 15)
        #img = cv2.rectangle(img, (50, 50), (700, 600), (0, 200, 250), 10)
        #print(img.shape)
        #pyautogui.press('w') 
        
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        img=cv2.putText(img,'Roman video player',(5,50),font ,2,(0,0,255),10)
        img=cv2.putText(img,' Q  quit video',(1,500),font ,2,(0,0,255),10)
        img=cv2.putText(img,' G  Gray ',(1,600),font ,2,(0,0,255),10)
        img=cv2.putText(img,' H  HSV',(1,700),font ,2,(0,0,255),10)
        cv2.imshow('Roman Video Player',img)
        
        #cv2.imshow('this is gray version j ', img2)

        #cv2.waitKey(100)  # 1sec= 1k milisec
        #if cv2.waitKey(100) & 0XFF== ord('q'):
            #break
        if cv2.waitKey(100) & 0XFF== ord('q'):
            cv2.destroyAllWindows()
            break
       


    

    
    
#cv2.destroyAllWindows()
root.mainloop()




    

    
    




