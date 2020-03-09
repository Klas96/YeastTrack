#Yeast Track Main
import cv2
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#global variables
currentFrame = 1
currentBlend = 0

def loadChannels():
    #Get File Paths
    filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP1C1Z4.avi"
    filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP1C2Z1.avi"
    #Get video Capture
    vidC1 = cv2.VideoCapture(filePathC1)
    vidC2 = cv2.VideoCapture(filePathC2)
    return(vidC1,vidC2)

def getVideoFrame():
    global currentFrame
    vidC1.set(cv2.CAP_PROP_POS_FRAMES, currentFrame)
    gotFrame,vidFrame = vidC1.read()
    return(vidFrame)

def getFlorFrame():
    global currentFrame
    vidC2.set(cv2.CAP_PROP_POS_FRAMES, currentFrame)
    gotFrame,floFrame = vidC2.read()
    return(floFrame)

def incFloIntens(frame,intens):
    


def blendFrames(frame1,frame2):
    global currentBlend

    blendedFrame = cv2.add(frame1*currentBlend, frame2)
    return(blendedFrame)

def updateFrame():
    vidFrame = getVideoFrame()
    floFrame = getFlorFrame()
    finalFrame = blendFrames(floFrame,vidFrame)
    #finalFrame = floFrame
    cv2.imshow('CellTracker', finalFrame)
    print("updateFrame: ")
    return()


def changeFrame(frameNum):
    global currentFrame
    currentFrame = frameNum
    updateFrame()

#Change Between Florecent And Video Channel
def changeChanell(division):
    global currentBlend
    currentBlend = division
    updateFrame()

#Main

vidC1,vidC2 = loadChannels()

cv2.namedWindow('CellTracker')

sliderPos = 0
numFrames = int(vidC1.get(cv2.CAP_PROP_FRAME_COUNT))

cv2.createTrackbar("Frame",'CellTracker',sliderPos,numFrames,changeFrame)
cv2.createTrackbar("Channel",'CellTracker',0,100,changeChanell)

while(True):

    char = cv2.waitKey(33)
    if( char == 27 ):
        break;

vidC1.release();
