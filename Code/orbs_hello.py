#source:https://pysource.com/2018/03/21/feature-detection-sift-surf-obr-opencv-3-4-with-python-3-tutorial-25/
#source: https://docs.opencv.org/trunk/d1/d89/tutorial_py_orb.html
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
image_file = '../../data/image.jpg'

def process_frame(img):
    img = cv.imread(img,0)
    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints with ORB
    kp = orb.detect(img,None)
    # compute the descriptors with ORB
    kp, des = orb.compute(img, kp)
    # draw only keypoints location,not size and orientation
    img2 = cv.drawKeypoints(img, kp, None, color=(0,255,0), flags=0)
    return img2

img_out = process_frame(image_file)
plt.imshow(img_out), plt.show()
