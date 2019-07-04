import cv2 as cv
class Extractor:
    def __init__(self,frame):
        self.frame = frame

    #source: https://docs.opencv.org/trunk/d1/d89/tutorial_py_orb.html
    def process_frame(self):
        # Initiate ORB detector
        orb = cv.ORB_create()
        # find the keypoint s with ORB
        kp = orb.detect(self.frame, None)
        # compute the descriptors with ORB
        kp, des = orb.compute(self.frame, kp)
        # draw only keypoints location,not size and orientation
        output_frame = cv.drawKeypoints(self.frame, kp, None, color=(0, 255, 0), flags=0)

        for point in kp:
            x,y = map(lambda x: int(round(x)), point.pt)

        return self.frame#output_frame