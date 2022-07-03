import cv2
from tkinter import *
import tkinter.font as tkFont

root = Tk()

fontStyle = tkFont.Font(family="Lucida Grande", size=20)

input_label = Label(root, text="Enter Complete Image Path :", font=fontStyle)
image_path_input = Entry(root, font=fontStyle)

def Submit () :

    global image_path
    image_path = image_path_input.get()

    image_path_input.delete(0, END)

    Detect()

def Demo () :

    global image_path
    image_path = "DemoFacePic.jpeg"

    Detect()

root.title("Face Detection")

submit_button = Button(root, text="Submit", command=Submit, font=fontStyle)
demo_button = Button(root, text="Try Demo Pic", command=Demo, font=fontStyle)

input_label.grid(row=0, column=0)
image_path_input.grid(row=1, column=0)
submit_button.grid(row=2, column=0)
demo_button.grid(row=3, column=0)


def Detect () :

    global image_path

    if image_path != "" :

        image = cv2.imread(image_path, cv2.IMREAD_COLOR)

        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        trained_data = cv2.CascadeClassifier("frontalface.xml")

        face_cordinates = trained_data.detectMultiScale(gray_image)

        for (x,y,w,h) in face_cordinates:
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

        cv2.imshow("Face Detection", image)

        cv2.waitKey()

root.mainloop()

print("Code Completed")