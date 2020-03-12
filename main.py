#Yeast Track Main
import cv2
import numpy as np
#import pandas as pd
from matplotlib import pyplot as plt
from detectCell import detectCells
from getClassFrame import getTextFrame

#global variables
currentFrame = 1
currentBlend = 0

#classes
class Frame:
    #Constructor
    def __init__(self,vidChan,floChan):
        self.vidChan = vidChan
        self.floChan = floChan

    #Methods
    def getVidChan(self):
        return(self.vidChan)

    def getFloChan(self):
        return(self.floChan)

    def showFrame(self):
        cv2.imshow("vidChan",self.vidChan)
        cv2.imshow("floChan",self.floChan)

    def analyseFrame(self):
        #TODO
        pass


class Video:
    #variables
    frames = []
    #Constructor
    #Pre: captureVideo, captureFlo
    #Ret: Video object
    def __init__(self,vidChanCap,floChanCap):
        hasVidFrame = True
        hasFloFrame = True
        frameNum = 0
        numVidFrames = int(vidChanCap.get(cv2.CAP_PROP_FRAME_COUNT))
        for i in range(numVidFrames):
            hasFrame,vidFrame = vidChanCap.read()
            hasFrame,floFrame = floChanCap.read()
            frame = Frame(vidFrame,floFrame)
            self.frames.append(frame)

    #Methods
    #pre frameNum nuber of the frame being retrived
    def getFrame(self,frameNum):
        return(self.frames[frameNum])

def loadChannels():
    #Get File Paths
    filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C1Z4.avi"
    filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C2Z2.avi"
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

#Pre: frame
#ret: Frame with higer intesity
def incFloIntens(frame,intens):
    maxIntens = np.amax(frame)
    frame = frame*intens
    #if value is higher that 255 floor to 255
    frame[frame > 255] = 255
    return(frame)

def blendFrames(frame1,frame2):
    global currentBlend
    frame1 = incFloIntens(frame1,currentBlend)
    blendedFrame = cv2.add(frame1, frame2)
    return(blendedFrame)

def updateFrame():
    vidFrame = getVideoFrame()
    vidFrame = rescale_frame(vidFrame, percent=1000)
    floFrame = getFlorFrame()
    floFrame = rescale_frame(floFrame, percent=1000)
    finalFrame = blendFrames(floFrame,vidFrame)

    sizeX = finalFrame.shape[0]
    sizeY = finalFrame.shape[1]

    tracking = True
    if tracking:
        keyPoints = detectCells(vidFrame)
        textFrame = getTextFrame(keyPoints,sizeX,sizeY)
    #finalFrame = floFrame
    finalFrame = cv2.add(finalFrame,textFrame)
    cv2.imshow('CellTracker', finalFrame)
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

#Rescaling

def make_1080p():
    cap.set(3, 1920)
    cap.set(4, 1080)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)


#Main
vidC1,vidC2 = loadChannels()

cv2.namedWindow('CellTracker')

sliderPos = 0
numFrames = int(vidC1.get(cv2.CAP_PROP_FRAME_COUNT))

cv2.createTrackbar("Frame",'CellTracker',sliderPos,numFrames,changeFrame)
cv2.createTrackbar("Channel",'CellTracker',0,100,changeChanell)
updateFrame()

testVideo = Video(vidC1,vidC2)
frameFromVid = testVideo.getFrame(100)
frameFromVid.showFrame()
cv2.waitKey(0)

while(True):

    char = cv2.waitKey(33)
    if( char == 33 ):
        break;

vidC1.release()
vidC2.release()
