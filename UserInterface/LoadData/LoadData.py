import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
from UserInterface.videoClass import Video
#from Tkinter import Tk 
#from tkinter.filedialog import askopenfilename

#Displays the OME-XML metadata for a file on the console:
#showinf -omexml /path/to/file
#showinf -nopix /path/to/file
#os.popen('cat /etc/services').read()

def getVideo():
    filePath = getFilePath()

    series = choseSeries()

    cropUppLeft, cropDownRight = cropStage(filePath)

    #IF .lif file run
    convertLifToTif(lifFilePath, tifFilePath)
    video = imortTiftoVideo(tifFilePath)

    return(video)

def getFilePath():
    #Tk().withdraw()
    #filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    #print(filename)
    path = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/Experiment13h_050619/Experiment13h_050619.lif"
    return(path)

#Gets Witch series should be loded by user
def choseSeries():
    print("What series would you like to load")
    return(3)

#Gets user to crop Video
def cropStage(filePath):
    uppLeft = (100,100)
    downRight = (200,200)
    return(uppLeft,downRight)

def loadData(filePath,series,cropUppLeft = -1, cropDownRight = -1):
    matList = []
    numZoomIn = 4
    numChan = 2
    #loading channel 0
    for channel in range(numChan):
        #List containg all zoom in levels
        zoomList = []
        for zoomLevel in range(numZoomIn):
            cleanWorking = "rm ./YeastTrack/VideoData/WorkingData/*"
            os.system(cleanWorking)

            comand = "./bftools/bfconvert -nolookup"
            seriesFlag = " -series " + str(series)
            channelFlag = " -channel " + str(channel)
            zoomFlag = " -z " + str(zoomLevel)
            cropFlag = " -crop 0,0,512,512"
            filePath = " " + filePath
            tifPath = " ./YeastTrack/VideoData/WorkingData/working.tif"

            cmd = comand + seriesFlag + cropFlag + channelFlag + zoomFlag + filePath + tifPath
            os.system(cmd)
            path = "./YeastTrack/VideoData/WorkingData/working.tif"
            retval, mats = cv2.imreadmulti(path)
            zoomList.append(mats)
        matList.append(zoomList)

    return(matList)


def skrap():
    path = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/WorkingData/working.tif"

    retval, mats = cv2.imreadmulti(path)
    #retval, mats = cv2.imread(path)

    for i in range(len(mats)):
        cv2.imshow("Funka",mats[i])
        cv2.waitKey()
