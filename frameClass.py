from Segmentation.cellInstance import  cellInstance
import cv2
import numpy as np
from centroidTracker import CentroidTracker
from Segmentation.OstuBinarizartion import OtsuBinarization
from Segmentation.watershed import  watershed
from Segmentation.cellInstance import  cellInstance
from getInstantSegmentFrame import getCellInstImg
from Segmentation.LaplacianGausian import laplacianGausian


class Frame:
    #variables
    #optChan
    #floChan
    #Constructor
    def __init__(self,optChan,floChan,frameNum=-1):
        #variables
        self.optChan = optChan
        self.floChan = floChan
        self.frameNumber = frameNum

        self.xSz = self.optChan.shape[0]
        self.ySz = self.optChan.shape[1]

        self.scaling = 1000
        #TODO MAke to factors of scaling
        self.xScaleSz = self.getScaledOptChan().shape[0]
        self.yScaleSz = self.getScaledOptChan().shape[1]

        #TODO
        self.pixelToMiccron = 1000

        self.classFrame = 0
        self.idFrame = 0
        self.analyseFrame()

    #Methods
    def getOptChan(self):
        return(self.optChan)

    def getFloChan(self):
        return(self.floChan)

    def getFrameNum(self):
        return(self.frameNumber)

    def getScaledOptChan(self):
        optChanScale = rescale_frame(self.optChan, percent=1000)
        return(optChanScale)

    def getScaledFloChan(self):
        floChanScale = rescale_frame(self.floChan, percent=1000)
        return(floChanScale)

    def getClassificationFrame(self):
        return(self.classFrame)

    def getWHI5ActivFrame(self):
        #Whi5Detect
        threshold = 0.30
        #CellDeteect
        #threshold = 0.175-0.0125


        #gray = cv2.cvtColor(self.getScaledFloChan(),cv2.COLOR_BGR2GRAY)
        gray = self.getScaledFloChan()
        #apply thresholding
        gotFrame, thresh = cv2.threshold(gray,int(255*threshold),255,cv2.THRESH_BINARY)
        return(thresh)

    #<|^_^|>
    #ret: Gives Image
    def getCellInstancesImage(self):
        #self.cellInstanses
        return(getCellInstImg(self.cellInstanses))

    def showFrame(self):
        cv2.imshow("optChan",self.optChan)
        cv2.imshow("floChan",self.floChan)

    def analyseFrame(self):
        self.cellInstanses = OtsuBinarization(self)
        #self.cellInstanses = watershed(self)
        #self.cellInstanses = laplacianGausian(self)

def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/100)
    height = int(frame.shape[0] * percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
