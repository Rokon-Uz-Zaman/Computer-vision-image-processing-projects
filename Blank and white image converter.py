#author: rokon-uz-zaman roman
#Blank and white image converter

import tkinter as tk
import cv2
from tkinter import filedialog

root=tk.Tk()
root.geometry("400x300") #window size

label1=tk.Label(root,text='Black & White Image Converter ',width=40)
label1.grid(row=1,column=1)


button1=tk.Button(root,text='Upload an image ',width=30,command=lambda:fileUpload())
button1.grid(row=2,column=1)

def fileUpload():
    uploaded=filedialog.askopenfilename()
    img=cv2.imread(uploaded,0)
    cv2.imshow('blank and white image',img)

root.mainloop()    
    

    
    




