import cv2
import numpy as np
from Segmentation.cellInstance import cellInstance
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.FilterDetection import filterDetections
from Segmentation.getThreshold import getTherholdImage
from Segmentation.Rescaling import rescaleImage
from Segmentation.ConvexHull import convexHull


#OstuBinarization
#Pre: Frame As defined in main
#Ret: CellInstances in
def OtsuBinarization(frame):
    optImg = frame.getOptImage()
    floImg = frame.getFloImage()
    optImg = rescaleImage(optImg,10)
    floImg = rescaleImage(floImg,10)
    maskImg = getMaskFrame(optImg)
    maskImg = rescaleImage(maskImg,0.1)
    cellInstanses = conectedCompontents(maskImg,floImg)
    cellInstanses = filterDetections(cellInstanses)
    return(cellInstanses)

#Pre: VideoFrame
#Ret: White on black maskFrame
def getMaskFrame(img):
    img = otsuThreshold(img)
    maskImg = convexHull(img)
    return(maskImg)

"""
#Pre: takes An binary image
#Ret: Returns Image with conexHull filled of all wite separated images
def convexHull(img):
    # Finding contours for the thresholded image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #im2, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # create hull array for convex hull points
    hull = []
    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))

    #Create an empty black image
    img = np.zeros((img.shape[0], img.shape[1]), np.uint8)

    for i in range(len(contours)):
        img = cv2.fillPoly(img, pts =[hull[i]], color=(255))

    return(img)
"""

def conectedCompontents(img,floFrame):
    conectedCompontents, hirearchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floFrame)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)
    return(cellInstanses)

def otsuThreshold(img):
    #apply thresholding
    gotFrame, thresh = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(thresh)
