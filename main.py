#Yeast Track Main
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def changeFrame(frameNum):
     vidC1.set(cv2.CAP_PROP_POS_FRAMES, frameNum)
     gotFrame,frame = vidC1.read()
     cv2.imshow('CellTracker', frame)

#Get File Paths
filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidC1Z4.avi"
filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidC2Z2.avi"

vidC1 = cv2.VideoCapture(filePathC1)
vidC2 = cv2.VideoCapture(filePathC2)

sliderPos = 0

cv2.namedWindow('CellTracker')

numFrames = int(vidC1.get(cv2.CAP_PROP_FRAME_COUNT))

print(numFrames)

cv2.createTrackbar("Frame",'CellTracker',sliderPos,numFrames,changeFrame)

while(True):

    char = cv2.waitKey(33)
    if( char == 27 ):
        break;

vidC1.release();
