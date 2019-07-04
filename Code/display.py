# Author Sean Benson
from cv2 import cv2 as cv
import time
import tkinter
import PIL.Image
import PIL.ImageTk
from Analize_Car_Video.Code.extractor import Extractor
from Analize_Car_Video.Code.video_capture import VideoCapture

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
        self.vid = VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tkinter.Canvas(
            window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Button that lets the user take a snapshot
        self.btn_snapshot = tkinter.Button(
            window, text="Snapshot", width=50, command=self.snapshot)
        self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 50 #this is 20fps
        self.update()

        self.window.mainloop()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            cv.imwrite("../../snapshots/frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") +
                       ".jpg", cv.cvtColor(frame, cv.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            extractor = Extractor(frame)
            frame = extractor.process_frame()
            self.photo = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tkinter.NW)

        self.window.after(self.delay, self.update)
