import cv2 as cv
# source: https://solarianprogrammer.com/2018/04/21/python-opencv-show-video-tkinter-window/
# code is modified

class VideoCapture:
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