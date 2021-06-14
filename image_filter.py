from tkinter import *
from builtins import input
import tkinter as tk
from tkinter import ttk
import numpy as np
import cv2
import tkinter.font as font
import tkinter.filedialog
from tkinter import messagebox

# create a tkinter window
output = ""
flag=0
y=0
r=""
file1=""
value=0
thresh1=""
k= cv2.waitKey(0)
bright_image=""
contrast_image1=""
data1=""
previous_image = ""
dark=""
beta=0
alpha=1
image_path = Tk()
main_window = Tk()
main_window .title("Welcome")
main_window.geometry('300x100+500+250')
second_window = Tk()
frame1 = ttk.Frame(second_window)
frame1.config(width=500,height=200,relief="groove")
frame1.pack()
#frame2 = ttk.Frame(second_window)
#frame2.pack()
#frame2.config(width=500, height=350, relief=RIDGE)
#######################################################

########################################




frame3= ttk.Frame(second_window)
frame3.pack()
frame3.config(width=700, height=50)
w = tk.Label(frame1, text="Open Cv Image Editor ",font=('ms serif', 30),fg='#4893FB')
w.pack(pady="40")

lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def Dragging(event):
    x, y = event.x - lastClickX + image_path.winfo_x(), event.y - lastClickY + image_path.winfo_y()
    image_path.geometry("+%s+%s" % (x , y))


image_path.title("Enter Image")
image_path.overrideredirect(True)
image_path.bind('<B1-Motion>', Dragging)
image_path.bind('<Button-1>', SaveLastClickPos)



image_path.withdraw()
second_window.withdraw()


def open_image():
    global data1
    image_path.deiconify()
    image_path.geometry('410x150+500+250')
    e=Entry(image_path,borderwidth=5,width="30")
    data1 =e.get()
    e.grid(row=1,column=1,sticky = W,padx=5)
    l=Label(image_path,text="Enter Image Path:",font=('ms serif', 12),fg='#4893FB').grid(row=1,column=0,pady= 30,sticky = W,padx=5)
    image_button1= Button(image_path,text="Open",pady=5,width="8",command=lambda:show_image(),font=('ms serif', 10),fg='#4893FB',bg='white',bd=2).grid(row=1,column=2)
    image_button= Button(image_path,text="X",pady=5,width="3",command=lambda:close(),font=('serif',8),fg='white',bg='red',bd=2).grid(row=0,column=2,sticky=tk.SE)

def close():
   image_path.withdraw()

def open_second():
    second_window.deiconify()
    second_window.geometry('520x340+400+150')
    second_window.title("Editing")
    main_window.withdraw()
    messagebox.showinfo("Hint ", "When You Finish Editing You Can Save Image After That")


def des_img():
    image_path.withdraw()
def store_image(data):
    global data1
    data1=data

def bright(x):
    global output
    global data1
    global bright_image
    global previous_image
    global beta
    global y
    global alpha
    global flag
    flag = 0
    beta=x
    cv2.createTrackbar('Threshold', 'image', 0, 1, thresholding)
    cv2.createTrackbar('bit Plane', 'image', 0, 7, bit_wise)
    output = cv2.convertScaleAbs(data1, alpha=alpha, beta=beta)

    #intensity_matrix = np.ones(contrast_image1.shape, dtype="uint8") * x
    #output = cv2.add(contrast_image1, intensity_matrix)
    bright_image=output
    previous_image = output
    cv2.imshow("image", bright_image)
def GreyLevel():
    pass



def show_image():
    global output,bright_image,contrast_image1,k
    save_image['state'] = tk.NORMAL
    des_img()
    file1=tk.filedialog.askopenfilenames(title ='Select Image')

    joined_string = "".join(file1)
    second_window.withdraw()

    while(1):


      img = cv2.imread(joined_string,0)
      scale_percent = 10
      width = int(img.shape[1] * scale_percent / 10)
      height = int(img.shape[0] * scale_percent / 10)
      resize = (width, height)
      output = cv2.resize(img, resize, interpolation=cv2.INTER_LINEAR)
      bright_image=output
      contrast_image1=output
      store_image(output)
      cv2.namedWindow('image',cv2.WINDOW_NORMAL)
      cv2.resizeWindow('image', 500, 655)
      switch = '0 : OFF : ON'
      cv2.createTrackbar('Brightness', 'image', 0, 255, bright)
      cv2.createTrackbar('Contrast', 'image', 0, 10, contrast_image)
      cv2.createTrackbar('Threshold', 'image', 0, 1, thresholding)
      cv2.createTrackbar('bit Plane', 'image', 0, 7, bit_wise)
      #cv2.createTrackbar(switch, 'image', 0, 1,GreyLevel)



      cv2.imshow("image", output)
      if cv2.waitKey(0):
           second_window.deiconify()
           print("hello")
           break

    cv2.destroyAllWindows()


def thresholding(x):
    global output
    global previous_image
    global thresh1
    global flag
    cv2.createTrackbar('bit Plane', 'image', 0, 7, bit_wise)

    if(x==1):
         flag=1
         ret, thresh1 = cv2.threshold(output, 127, 255, cv2.THRESH_BINARY)
         cv2.imshow("image",thresh1)
    if(x==0):
        flag=0
        cv2.imshow("image", output)



def contrast_image(x):
    global output
    global beta
    global y
    global alpha
    global bright_image
    global contrast_image1,data1
    global previous_image
    global flag
    flag=0

    alpha=x-.8

    if x==0:
        alpha = float(x+1)
    elif x==1:
        alpha = float(x -.2)
    print(alpha)
    output = cv2.convertScaleAbs(data1,alpha=alpha, beta=beta)
    contrast_image1=output
    previous_image=output
    cv2.createTrackbar('Threshold', 'image', 0, 1, thresholding)
    cv2.createTrackbar('bit Plane', 'image', 0, 7, bit_wise)

    print(x)
    cv2.imshow("image", output)




def bit_wise(z):
    global output
    global flag
    global r
    global value
    value=z
    cv2.createTrackbar('Threshold', 'image', 0, 1, thresholding)
    flag=2
    if(flag==1):
        output=thresh1
    r, c = output.shape
    x = np.zeros((r, c, 8), dtype=np.uint8)
    for i in range(8):
        x[:, :, i] = 2 ** i
    r = np.zeros((r, c, 8), dtype=np.uint8)
    for i in range(8):
        r[:, :, i] = cv2.bitwise_and(output, x[:, :, z])
        mask = r[:, :, z] > 0
        r[mask] = 255
        cv2.imshow("image", r[:, :, z])


def save_image():
    global output, file1
    if (messagebox.askyesno("Save", "Do you want to save it !")):
             if (flag == 1):
                 output = thresh1
                 cv2.imwrite("NEwimage.jpg", output)
             elif (flag == 2):
                 cv2.imwrite("NEwimage.jpg", r[:, :, value])
                 print("hello3")
             else:
                 print("hello2")
                 cv2.imwrite("NEwimage.jpg", output)
             messagebox.showinfo("Saving","Saved !")


################################################################3
btn = Button(main_window, text="Let's Start", bd='8',width="50",height="35",
             command=open_second,bg="white",fg="#4893FB",font=('ms serif', 14)).pack(padx=20,pady=30)

font1 = font.Font(family='Serif', weight='bold')
open_image= Button(frame3,text="Open Image",command=show_image,width="20",height="8",bg='#4893FB',font=('ms serif', 14),fg='#ffffff')
open_image.grid(row=2,column=0, pady=10)
save_image= Button(frame3,text="Save Image",command=save_image,width="20",height="8",bg='#ffffff',font=('ms serif', 14),fg='#4893FB',state=tk.DISABLED)
save_image.grid(row=2,column=3, pady=10)

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        second_window.destroy()

second_window.protocol("WM_DELETE_WINDOW", on_closing)
################################################################3

########bright image





main_window.mainloop()