from UserInterface.frameClass import Frame
#from Segmentation.cellInstance import  cellInstance
import cv2
import numpy as np
from Tracking.centroidTracker import CentroidTracker
from UserInterface.getIDImage import getIDImage
from UserInterface.getClassImage import getClassImage
from Tracking.findLineage import findLineage
from Tracking.filterTracking import filterTrackedCells

class Video:
    #variables
    frames = []
    tracker = 0
    numFloFrames = 0
    maxDisappeared = 50
    #Constructor
    def vidCapInit(self,optImgCap,floImgCap):

        self.numZoom = 1
        self.numVidFrames = int(optImgCap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.numFloFrames = int(optImgCap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.tracker = CentroidTracker()

        for i in range(self.numVidFrames):
            #Read Images
            hasFrame,optImg = optImgCap.read()
            hasFrame,floImg = floImgCap.read()
            #Convert Images
            optImg = cv2.cvtColor(optImg, cv2.COLOR_BGR2GRAY)
            floImg = cv2.cvtColor(floImg, cv2.COLOR_BGR2GRAY)

            frame = Frame(optImg,floImg,i)
            self.frames.append(frame)

    #Init Object With List of mats with frames
    def matListInit(self, mats):
        self.numFrames = len(mats)
        print("Loadling "+str(self.numFrames)+" Frames")
        self.tracker = CentroidTracker()
        for frameNum in range(self.numFrames):
            print("Loading Frame Number: " + str(frameNum))
            #frameArr = mats[frameNum]
            #Channels
            optImg = mats[frameNum][0]
            #floImage = floArr[1]
            floImg = mats[frameNum][1]
            frame = Frame(optImg,floImg,frameNum)
            self.frames.append(frame)
        del mats

    #Pre: captureVideo, captureFlo
    #Ret: Video object
    def __init__(self,arg1,arg2 = -1):
        if(arg2 == -1):
            self.matListInit(arg1)
        else:
            self.vidCapInit(arg1,arg2)
        self.xSz = self.frames[0].getUserOptImage().shape[0]
        self.ySz = self.frames[0].getUserOptImage().shape[1]

    #Methods
    def getNumFrmes(self):
        return(len(self.frames))

    #Pre: frameNum nuber of the frame being retrived
    #Ret: Frame of given number
    def getFrame(self,frameNum):
        return(self.frames[frameNum])

    def getTrackedCells(self):
        return(self.trackedCells)

    def runTracking(self):
        #loop through frames in video
        for frame in self.frames:
            cellInstanses = frame.cellInstanses
            self.trackedCells = self.tracker.updateCellInst(cellInstanses)
            frame.idImg = getIDImage(self.trackedCells,frame)
            frame.classImg = getClassImage(self.trackedCells,frame.xSz,frame.ySz)

        #self.trackedCells = filterTrackedCells(self.trackedCells)
        #TODO: Make ID frame and Segmentation Frame Here after filtering
        #for frame in self.frames:
            #frame.idFrame = getIDFrameNY(self.trackedCells,frame)
            #frame.classFrame = getClassFrameNY(self.trackedCells,frame.xScaleSz,frame.yScaleSz)

        self.findLineage()

    def findLineage(self):
        findLineage(self.trackedCells)
