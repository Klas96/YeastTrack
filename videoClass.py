from frameClass import Frame
from Segmentation.cellInstance import  cellInstance
import cv2
import numpy as np
from centroidTracker import CentroidTracker
from getIDFrame import getIDFrame
from getIDFrame import getIDFrameNY
from getClassFrame import getClassFrame
from findLineage import findLineage
from filterTracking import filterTrackedCells

class Video:
    #variables
    frames = []
    tracker = 0
    numVidFrames = 0
    numFloFrames = 0
    maxDisappeared = 50
    #Constructor
    def vidCapInit(self,optChanCap,floChanCap):

        self.numZoom = 1
        self.numVidFrames = int(optChanCap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.numFloFrames = int(optChanCap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.tracker = CentroidTracker()

        for i in range(self.numVidFrames):
            hasFrame,vidFrame = optChanCap.read()
            hasFrame,floFrame = floChanCap.read()
            frame = Frame(vidFrame,floFrame,i)
            self.frames.append(frame)

    def matListInit(self, mats):
        self.numFrames = len(mats)
        print("Loadling "+str(self.numFrames)+" Frames")
        self.tracker = CentroidTracker()
        for frameNum in range(self.numFrames):
            print("Loading Frame Number: " + str(frameNum))
            frameArr = mats[frameNum]
            #Channels
            optArr = frameArr[0]
            floArr = frameArr[1]
            #Zoom Levels
            optImage = optArr[3]
            optImage = mats[frameNum][0][3]
            floImage = floArr[1]
            floImage = mats[frameNum][1][1]
            frame = Frame(optImage,floImage,frameNum)
            self.frames.append(frame)


    #Pre: captureVideo, captureFlo
    #Ret: Video object
    def __init__(self,arg1,arg2 = -1):
        if(arg2 == -1):
            self.matListInit(arg1)
        else:
            self.vidCapInit(arg1,arg2)
        self.xSz = self.frames[0].getScaledOptChan().shape[0]
        self.ySz = self.frames[0].getScaledOptChan().shape[1]



    #Methods
    def getNumFrmes(self):
        return(self.numFrames)

    #pre frameNum nuber of the frame being retrived
    def getFrame(self,frameNum):
        return(self.frames[frameNum])

    def getTrackedCells(self):
        return(self.trackedCells)

    def runTracking(self):
        #loop through frames in video
        for frame in self.frames:
            cellInstanses = frame.cellInstanses
            self.trackedCells = self.tracker.updateCellInst(cellInstanses)
            frame.idFrame = getIDFrame(self.trackedCells,frame.xScaleSz,frame.yScaleSz)
            frame.classFrame = getClassFrame(self.trackedCells,frame.xScaleSz,frame.yScaleSz)

        self.trackedCells = filterTrackedCells(self.trackedCells)
        #TODO: Make ID frame and Segmentation Frame Here after filtering
        #for frame in self.frames:
            #frame.idFrame = getIDFrameNY(self.trackedCells,frame)
            #frame.classFrame = getClassFrameNY(self.trackedCells,frame.xScaleSz,frame.yScaleSz)

        self.findLineage()

    def findLineage(self):
        findLineage(self.trackedCells)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/ 100)
    height = int(frame.shape[0] * percent/ 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
