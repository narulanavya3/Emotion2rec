import tkinter as tk
import os
from tkinter import *
from capture import capture
from emotion_to_html import run_emotion_to_html
import cv2
from tkinter.ttk import *
from PIL import ImageTk

root= tk.Tk()

background_root = ImageTk.PhotoImage(file = "images/bg1.png")
canvas1 = tk.Canvas(root, width = 900, height = 600)
canvas1.pack()
root.resizable(False, False)
label_root = Label(root, image = background_root)
label_root.place(x=0, y=0, relwidth = 1, relheight = 1,)

def train():
    '''loads trainer.py'''
    os.system('python trainer.py')

def open_html(file_name):
    '''opens html file'''
    os.system('start ' + f'templates/{file_name}')

def emotion():
    '''calls the run_emotion_to_html function 
    gets the dominant emotion 
    returns a recommendation for a spotify playlist'''  
    response = run_emotion_to_html()
    root3 = tk.Tk()
    canvas3 = tk.Canvas(root3, width = 400, height = 300)
    canvas3.pack()
    root3.resizable(False, False)

    recommendation = tk.Label(root3, text = "Here's my recommendation for you!", bg = "black", fg = "white", font = ("Arial", 20))
    canvas1.create_window(200, 120, window = recommendation)

    button2 = tk.Button(root3, text = "open recommendation", bg = "white", fg = "black", activebackground = "yellow", command = lambda: open_html(response))
    canvas3.create_window(200, 170, window = button2)

def run_capture(entry):
    '''gets the id from get_new_face_id function
       calls the capture function in capture.py'''
    id = entry.get()
    faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    message = capture(id, faceDetect)

def get_new_face_id():
    '''takes an id input from the user 
    calls the run_capture function'''
    root2 = tk.Toplevel()
    background_root2 = ImageTk.PhotoImage(file = "images/bg1.png")
    canvas2 = tk.Canvas(root2, width = 500, height = 400)
    canvas2.pack()
    root2.resizable(False, False)

    label_root2 = Label(root2, image = background_root2)
    label_root2.place(x=0, y=0, relwidth = 1, relheight = 1,)

    label1 = tk.Label(root2, text= "Enter Id", bg="green", fg="black", font=("Arial", 18))
    canvas2.create_window(250, 150, window=label1)

    entry1 = tk.Entry (root2) 
    canvas2.create_window(250, 200, window=entry1)

    button2 = tk.Button(root2, text = "Submit", bg = "white", fg = "black", activebackground = "blue",command = lambda: run_capture(entry1))
    canvas2.create_window(250, 250, window=button2)

    root2.mainloop()

name = tk.Label(root, text = "emotion2rec version 1.0", bg = "black", fg = "white", font = ("Arial", 20))
canvas1.create_window(450, 50, window = name)

option = tk.Label(root, text = "Choose from the following given options", bg = "black", fg = "white", font = ("Arial", 18))
canvas1.create_window(450, 150, window = option)

button1 = tk.Button(root, text ="Add new face", height = 3, width = 50, bg = "black", fg = "white", command = get_new_face_id)
canvas1.create_window(450, 230, window = button1)

button2 = tk.Button(root, text = "Train face recognition model", height = 3, width = 50, bg = "black", fg = "white", command = train)
canvas1.create_window(450, 360, window = button2)

button3 = tk.Button(root, text = "Run application", height = 3, width = 50, bg = "black", fg = "white", command = emotion)
canvas1.create_window(450, 490, window = button3)

root.mainloop()
