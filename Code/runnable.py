# Author Sean Benson
from cv2 import cv2 as cv
import time
import tkinter as tk
import threading
import tkinter
from tkinter import Canvas
import PIL.Image
import PIL.ImageTk
import numpy as np

#######################################################################################
# CONFIGURATION PARAMETERS
input_video = '../../data/train.mp4'
#######################################################################################
# Methods and start

# source: https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
#code is modified


class App:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.video_source = input_video

        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(
            window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(
            window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 50
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        
        if ret:
            cv.imwrite("./snapshots/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") +
                       ".jpg", cv.cvtColor(frame, cv.COLOR_RGB2BGR))

    #source: https://docs.opencv.org/trunk/d1/d89/tutorial_py_orb.html
    def process_frame(self, frame):
        # Initiate ORB detector
        orb = cv.ORB_create()
        # find the keypoints with ORB
        kp = orb.detect(frame, None)
        # compute the descriptors with ORB
        kp, des = orb.compute(frame, kp)
        # draw only keypoints location,not size and orientation
        output_frame = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=0)

        #for point in kp:
         #   x,y = map(lambda x: int(round(x)), point.pt)

        return output_frame

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        frame = self.process_frame(frame)

        if ret:
            self.photo = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)

# source: https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
#code is modified

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:                
                # Return a boolean success flag and the current frame converted to BGR
                img2 = (ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB))
                
                return img2
            else:
                return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")

