import numpy as np
import cv2
from tkinter import *
from builtins import input
import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import math
from tkinter import messagebox

img = cv2.imread('185713473_3076160609371123_7804861620009490860_n.png', cv2.IMREAD_COLOR)

joined_string = ""


def open1():
    global joined_string
    file1 = tk.filedialog.askopenfilenames(title='Select Image')
    joined_string = "".join(file1)
    read()


def triangle(a, image):
    cv2.drawContours(image, [a], -1, (76, 177, 34), 3)
    cv2.fillPoly(image, pts=[a], color=(76, 177, 34))

    pass




def square(a, image):
    xx=cv2.contourArea(a)
    x, y, w, h = cv2.boundingRect(a)
    s = float(w)
    R = xx / (w*h)
    r=h/w
    if (R >= 0.82 and  R < 1.05  or r==1):
        r = h / w
        cv2.drawContours(image, [a], -1, (204, 72, 63), 3)
        cv2.fillPoly(image, pts=[a], color=(204, 72, 63))

    else:
        print(R)
        cv2.drawContours(image, [a], -1, (0, 0, 0), 3)
        cv2.fillPoly(image, pts=[a], color= (0, 0, 0))

def none(a, image):
    cv2.drawContours(image, [a], -1, (0, 0, 0), 3)
    cv2.fillPoly(image, pts=[a], color=(0, 0, 0))

    pass

def circle(c, image,a):
    (x, y), radius = cv2.minEnclosingCircle(c)
    radius = radius*radius
    area1=cv2.contourArea(c)
    area2=radius*math.pi
    if( .94<=area1/area2<=1.15):
            cv2.fillPoly(image, pts=[a], color=(0, 0, 255))
def read():
    main_window.withdraw()

    image = cv2.imread(joined_string)

    # Convert to grayscale.
    blur = cv2.GaussianBlur(image, (7, 7),-1)
    img = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
    r, t = cv2.threshold(img, 235, 255, cv2.CHAIN_APPROX_NONE)
    cv2.imshow('',t)
    arr, charcta = cv2.findContours(t, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in arr:
        a = cv2.approxPolyDP(c, 0.01 * cv2.arcLength(c, True), True)
        mm=(cv2.contourArea(c) * 4) / cv2.arcLength(c, True)
        circl = cv2.arcLength(c, True) / (mm)
        c2=circl / math.pi


        if 0.7 <= c2 and c2 <= 1.13:
            cv2.drawContours(image, [a], -1, (0, 0, 255), 3)
            if(len(a)!=8):
                cv2.fillPoly(image, pts=[a], color=(0, 0, 255))
            else:
                cv2.drawContours(image, [a], -1, (0, 0, 0), 3)
                cv2.fillPoly(image, pts=[a], color=(0, 0, 0))


        else:
            s = cv2.approxPolyDP(c, 0.03* cv2.arcLength(c, True), True)
            if len(s) == 3:
                triangle(a, image)

            elif len(a) == 4:
                square(a, image)

            else:
                none(a, image)
                pass
            #circle(c, image, a)


    cv2.imshow('Shapes', image)


main_window = Tk()
main_window.title("Welcome")
main_window.geometry('300x100+500+250')
btn = Button(main_window, text="Open", width="10", height="10",
             command=open1, bg="white", fg="#4893FB", font=('ms serif', 14)).pack(padx=20, pady=30)

cv2.waitKey(0)
main_window.mainloop()
cv2.destroyAllWindows()