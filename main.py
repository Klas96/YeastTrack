#Yeast Track Main
import cv2
import numpy as np
from matplotlib import pyplot as plt
from UserInterface.videoClass import Video
from UserInterface.LoadData.LoadData import getVideo
from UserInterface.LoadData.LoadtifFile import imortTiftoVideoNew
from Anlysis.plotFunctions import plotFunction
from Anlysis.VisulizeLinage import PlotLinageTree
from Anlysis.PrintMotherDoughter import printMotherDoghuther

#global variables
currentFrame = 1
currentBlend = 0

#TODO Pixel to micron ratio
#TODO Frame to sectond ratio

showMaskImg = False
showCellID = True
showLinagesTree = True
showOptImg = True
showWHI5ActivImg = False

def loadChannels(filePathOpt,filePathFlo):
    #Get video Capture
    vidOpt = cv2.VideoCapture(filePathOpt)
    vidFlo = cv2.VideoCapture(filePathFlo)
    return(vidOpt,vidFlo)

#Pre: frame
#ret: Frame with higer intesity
def incFloIntens(img,intens):
    intens = int(intens/10)
    #Check number of colors
    numCol = 3

    intensImg = np.zeros((img.shape[0], img.shape[1], numCol), np.uint8)
    for i in range(intens):
        intensImg = cv2.add(intensImg,img)
    return(intensImg)

#Merge
def increasIntens(img):
    global currentBlend
    img = incFloIntens(img,currentBlend)
    return(img)

#Update Frame Does scaling and adds all visual effect
#Pre: None
#Ret: None
def updateFrame():
    global currentFrame
    frame = video.getFrame(currentFrame)
    #optImg = frame.getScaledOptImage()
    optImg = frame.getUserOptImage()
    #floImg = frame.getScaledFloImage()
    floImg = frame.getUserFloImage()
    classImg = frame.getClassificationImage()
    finalImg = increasIntens(floImg)

    szX = finalImg.shape[0]
    szY = finalImg.shape[1]

    if showOptImg:
        finalImg = cv2.add(finalImg,optImg)
    if showMaskImg:
        finalImg = cv2.add(finalImg,classImg)
    if showCellID:
        finalImg = cv2.add(frame.getIDImage(),finalImg)
    if showWHI5ActivImg:
        finalImg = cv2.add(finalImg,frame.getWHI5ActivImage())
    cv2.imshow('CellTracker', finalImg)
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
#Paths to Channels
#filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP3C1Z4.avi"
#filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP3C2Z2.avi"

#filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C1Z4.avi"
#filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/WorkingData/working.tif"
#filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C2Z2.avi"

filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/tileScan1/130419opt.avi"
filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/tileScan1/130419flo.avi"

#lifFilePath = "./VideoData/Experiment13h_050619/Experiment13h_050619.lif"
#tifFilePath = "./VideoData/WorkingData/working.tif"

vidC1,vidC2 = loadChannels(filePathC1,filePathC2)

video = Video(vidC1,vidC2)
vidC1.release()
vidC2.release()
#Video = getVideo()

#convertLifToTifNew(lifFilePath, tifFilePath)
#video = imortTiftoVideoNew(tifFilePath)

video.runTracking()

#numFrames = int(vidC1.get(cv2.CAP_PROP_FRAME_COUNT))
numFrames = video.getNumFrmes()
cv2.namedWindow('CellTracker')

sliderPos = 0

cv2.createTrackbar("Frame",'CellTracker',sliderPos,numFrames-1,changeFrame)
cv2.createTrackbar("Channel",'CellTracker',0,100,changeChanell)
updateFrame()

#List With comand chars and coresponding function
listOfComandsChars = ["q", "s", "o", "i", "w", "l","p"]
listOfComandsFunctions = ["quit", "Show Segmentation", "show Opt Chan", "show cell ID", "show WHI5 Activ Threshold", "Print Lineage","Plot Data"]
while(True):
    print("Options:")
    for i in range(0,len(listOfComandsChars)):
        print(listOfComandsChars[i] + " = " + listOfComandsFunctions[i])

    key = cv2.waitKey(0)
    #input = str(input())
    print("Your input: " + chr(key))
    if(key == ord('q')):
        break
    if(key == ord('s')):
        showMaskImg = not showMaskImg
        print("showMaskImage is now " + str(showMaskImg))
        updateFrame()
    if(key == ord("o")):
        showOptImg = not showOptImg
        print("showOptImage is now " + str(showOptImg))
        updateFrame()
    if(key == ord("i")):
        showCellID = not showCellID
        print("showCellID is now " + str(showCellID))
        updateFrame()
    if(key == ord("w")):
        showWHI5ActivImg = not showWHI5ActivImg
        print("showWHI5ActivFrame is now " + str(showWHI5ActivImg))
        updateFrame()
    if(key == ord("l")):
        trackedCells = video.getTrackedCells()
        printMotherDoghuther(trackedCells)
        PlotLinageTree(trackedCells)
    if(key == ord("p")):
        trackedCells = video.getTrackedCells()
        plotFunction(video.getTrackedCells())
