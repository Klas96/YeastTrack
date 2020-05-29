#Yeast Track Main
import cv2
import numpy as np
from matplotlib import pyplot as plt
from UserInterface.videoClass import Video
from UserInterface.LoadData.LoadData import getVideo
from UserInterface.LoadData.LoadtifFile import imortTiftoVideoNew
from Anlysis.plotFunctions import plotFunction

#global variables
currentFrame = 1
currentBlend = 0

#TODO Pixel to micron ratio

#TODO Frame to sectond ratio

showMaskFrame = False
showCellID = True
showLinagesTree = True
showOptChan = True
showWHI5ActivFrame = False

def loadChannels(filePathC1,filePathC2):
    #Get File Paths
    #Get video Capture
    vidC1 = cv2.VideoCapture(filePathC1)
    vidC2 = cv2.VideoCapture(filePathC2)
    return(vidC1,vidC2)

#Pre: frame
#ret: Frame with higer intesity
def incFloIntens(frame,intens):
    intens = int(intens/10)
    #maxIntens = np.amax(frame)
    #frame = frame*intens
    # create an empty black image
    #Check number of colors
    numCol = 3
    if 2 == len(frame.shape):
        numCol = 1

    intensFrame = np.zeros((frame.shape[0], frame.shape[1], numCol), np.uint8)
    for i in range(intens):
        intensFrame = cv2.add(intensFrame,frame)

    #if value is higher that 255 floor to 255
    #frame[frame > 255] = 255
    return(intensFrame)

def increasIntens(image):
    global currentBlend
    image = incFloIntens(image,currentBlend)
    #blendedFrame = cv2.add(frame1, frame2)
    #return(blendedFrame)
    return(image)

#Update Frame Does scaling and adds all visual effect
#Pre
#Ret
def updateFrame():
    global currentFrame
    frame = video.getFrame(currentFrame)
    vidImage = frame.getScaledOptChan()
    floImage = frame.getScaledFloChan()
    classFrame = frame.getClassificationFrame()
    #Scale Frame
    #vidFrame = getVideoFrame()
    #vidFrame = rescale_frame(vidFrame, percent=1000)
    #floFrame = getFlorFrame()
    #floFrame = rescale_frame(floFrame, percent=1000)
    finalFrame = increasIntens(floImage)

    sizeX = finalFrame.shape[0]
    sizeY = finalFrame.shape[1]

    if showOptChan:
        finalFrame = cv2.add(finalFrame,vidImage)
    if showMaskFrame:
        finalFrame = cv2.add(finalFrame,classFrame)
    if showCellID:
        finalFrame = cv2.add(frame.idFrame,finalFrame)
    if showWHI5ActivFrame:
        finalFrame = cv2.add(finalFrame,frame.getWHI5ActivFrame())
    #finalFrame = floFrame
    #finalFrame = cv2.add(finalFrame,textFrame)

    #finalFrame = rescale_frame(finalFrame, percent=1000)
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

def plotTrackCell(trackedCells):
    printMotherDoghuther(trackedCells)
    cellToPlot = [0,5,12,3]
    #cellToPlot = [6,13]
    for trackedCell in trackedCells:
        cellID = trackedCell.getCellID()
        if any(cellID == i for i in cellToPlot):
            whi5Trace = trackedCell.getWhi5Trace()
            dicovFrame = trackedCell.getDetectionFrameNum()
            plt.plot(range(dicovFrame, dicovFrame+len(whi5Trace)),whi5Trace, label="ID " + str(cellID))

    plt.ylabel('WHI5 Activity')
    plt.xlabel('Frame Number')
    plt.title("WHI5 intesity")
    plt.legend()
    plt.show()

def printMotherDoghuther(trackedCells):
    for trackedCell in trackedCells:
        doughterID = trackedCell.getCellID()
        motgherID = trackedCell.getMotherCell()
        relatabelityFactor = trackedCell.getRelatabelityFactor()
        print("M: " + str(motgherID) + " --> " + "D: " + str(doughterID))
        print("RelFactor: " + str(relatabelityFactor))

#Main
#Paths to Channels
#filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP3C1Z4.avi"
#filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP3C2Z2.avi"

filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C1Z4.avi"
#filePathC1 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/WorkingData/working.tif"
filePathC2 = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/vidP4C2Z2.avi"

lifFilePath = "./VideoData/Experiment13h_050619/Experiment13h_050619.lif"
tifFilePath = "./VideoData/WorkingData/working.tif"

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
        showMaskFrame = not showMaskFrame
        print("showMaskFrame is now " + str(showMaskFrame))
        updateFrame()
    if(key == ord("o")):
        showOptChan = not showOptChan
        print("showOptChan is now " + str(showOptChan))
        updateFrame()
#import pandas as pdFrame()
    if(key == ord("i")):
        showCellID = not showCellID
        print("showCellID is now " + str(showCellID))
        updateFrame()
    if(key == ord("w")):
        showWHI5ActivFrame = not showWHI5ActivFrame
        print("showWHI5ActivFrame is now " + str(showWHI5ActivFrame))
        updateFrame()
    if(key == ord("l")):
        trackedCells = video.getTrackedCells()
        printMotherDoghuther(trackedCells)
    if(key == ord("p")):
        trackedCells = video.getTrackedCells()
        plotFunction(0,video.getTrackedCells())
