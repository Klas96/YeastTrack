from Segmentation.cellInstance import  cellInstance
import cv2
import numpy as np
from Tracking.centroidTracker import CentroidTracker
from Segmentation.OstuBinarizartion import OtsuBinarization
from Segmentation.watershed import  watershed
from Segmentation.cellInstance import  cellInstance
from Segmentation.LaplacianGausian import laplacianGausian
from Segmentation.ThersholdingSegmentation import segementThreshold
from Segmentation.RandomForestSegmentaion import rfSegmentetion
from UserInterface.getInstantSegmentImage import getCellInstImage
from UserInterface.rescaleImageToUser import rescaleImageToUser

class Frame:
    #TODO three zoom Init???

    #variables
    #optImage
    #floImage
    #Constructor
    def __init__(self,optImage,floImage,frameNum=-1):
        #TODO load as gray images
        #variables
        self.optImg = optImage
        self.floImg = floImage
        self.frameNum = frameNum

        self.xSz = self.optImg.shape[0]
        self.ySz = self.optImg.shape[1]

        self.scaling = 1000
        #TODO MAke to factors of scaling

        #TODO
        self.pixelToMiccron = 1000

        self.classFrame = 0
        self.idFrame = 0
        self.analyseFrame()


    def addZoomLevels(self,zom0Img,zom1Img):
        self.optImgZom0 = zom0Img
        self.optImgZom1 = zom1Img

    #Methods
    #Getters
    def getOptImage(self):
        return(self.optImg)

    def getFloImage(self):
        return(self.floImg)

    def getZoom0Image(self):
        return(self.optImgZom0)

    def getZoom1Image(self):
        return(self.optImgZom1)

    def getFrameNum(self):
        return(self.frameNum)

    def getUserOptImage(self):
        #Make A Certain Size
        img = self.getOptImage()
        #make Empty image with size
        userImg = np.zeros(img.shape, np.uint8)
        #Merge two zeros and one grey
        userImg = cv2.merge([img,img,img])
        userImg = rescaleImageToUser(userImg)
        return(userImg)

    def getUserFloImage(self):
        #Make A Certain Size
        img = self.getFloImage()
        #make Empty image with size
        userImg = np.zeros(img.shape, np.uint8)
        #Merge two zeros and one grey
        userImg = cv2.merge([userImg,img,userImg])
        userImg = rescaleImageToUser(userImg)
        return(userImg)

    def getClassificationImage(self):
        return(self.classImg)

    #Ret: Image ilustrating whi5 Activation
    def getWHI5ActivImage(self):
        #Whi5Detect
        threshold = 0.30
        #CellDeteect
        #threshold = 0.175-0.0125
        #gray = cv2.cvtColor(self.getScaledfloImage(),cv2.COLOR_BGR2GRAY)
        gray = self.getUserFloImage()
        #apply thresholding
        gotFrame, thresh = cv2.threshold(gray,int(255*threshold),255,cv2.THRESH_BINARY)
        return(thresh)

    #ret: Gives Image
    def getCellInstancesImage(self):
        #self.cellInstanses
        return(getCellInstImg(self.cellInstanses))

    #ret: Image With ID at cell positions
    def getIDImage(self):
        return(self.idImg)

    #Setters
    def showFrame(self):
        cv2.imshow("optImage",self.optImage)
        cv2.imshow("floImage",self.floImage)
        cv2.waitKey(0)

    #Segmentation of frame.
    #Use the Anlysis Method selected
    def analyseFrame(self):
        self.cellInstanses = OtsuBinarization(self)
        #self.cellInstanses = segementThreshold(self)
        #self.cellInstanses = rfSegmentetion(self)
        #self.cellInstanses = watershed(self)
        #self.cellInstanses = laplacianGausian(self)
