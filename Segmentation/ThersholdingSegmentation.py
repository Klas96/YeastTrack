from Segmentation.Preprocessing import preprocess
from Segmentation.Preprocessing import preprocessFloImg
import cv2
from matplotlib import pyplot as plt
import numpy as np
from Segmentation.cellInstance import cellInstance
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.FilterDetection import filterDetections
from Segmentation.ConvexHull import convexHull
from Segmentation.ConectedComponents import conectedCompontents
#Pre: Frame
#Ret: CellInstances
def segementThreshold(frame):
    #Get Image
    optImg = frame.getOptImage()
    floImg = frame.getFloImage()
    #Apply Preprocessing
    optImg = preprocess(optImg)
    floImg = preprocessFloImg(floImg)
    #Segment Edges with thresholding
    binImg = thesholdEdges(optImg)
    #Erode Here To avoid conecting cells??


    #cv2.imshow("binimgEdges",binImg)

    binImg = convexHull(binImg)

    #Threshold floImg
    binImgFlo = thesholdFlorecense(floImg)

    #grayThr = thresholdGray(optImg)

    #Intersection of Thresholds
    binImg = cv2.bitwise_and(binImg, binImgFlo)

    #cv2.imshow("binimgFinal",binImg)
    #cv2.waitKey(0)
    cellInstanses= conectedCompontents(binImg,floImg)
    cellInstanses = filterDetections(cellInstanses)
    return(cellInstanses)

#Pre: image of cells with clear edges
#Ret: Binary image Edges White not edge black
def thesholdEdges(img):
    #Threshold values
    thrLow = 85
    thrHigh = 255
    #cv2.imshow("img",img)
    gotImg, thresh = cv2.threshold(img,thrLow,thrHigh,cv2.THRESH_BINARY)
    return(thresh)

def thresholdGray(img):
    #Threshold
    thrLow = 65
    thrHigh = 255
    gotImg, thresh = cv2.threshold(img,thrLow,thrHigh,cv2.THRESH_BINARY)
    kernel = np.ones((2,2), np.uint8)
    thresh = cv2.erode(thresh, kernel, iterations=1)
    cv2.imshow("img",thresh)
    cv2.waitKey(0)

    #Remove Largest
    #Find largest contour in intermediate image
    cnts, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = max(cnts, key=cv2.contourArea)
    #Fill largest with Black
    cv2.drawContours(thresh, [cnt], -1, 0, cv2.FILLED)

    return(thresh)

def thesholdFlorecense(img):
    #Threshold values
    thrLow = 20
    thrHigh = 255
    #cv2.imshow("img",img)
    gotImg, thresh = cv2.threshold(img,thrLow,thrHigh,cv2.THRESH_BINARY)
    return(thresh)

#Pre: Binary Image
#Ret: Binary img with convex hull
def cellInstasConvexHull(img,floImg):
    # Finding contours for the thresholded image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #im2, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # create hull array for convex hull points

    cellInstanses = []
    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull = (cv2.convexHull(contours[i], False))
        whi5Activ = getWHI5Activity(hull,floImg)
        cellInstans = cellInstance(hull,whi5Activ)
        cellInstanses.append(cellInstans)

    return(cellInstanses)


def conectedCompontents(binImg,floImg):

    conectedCompontents, hirearchy = cv2.findContours(binImg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floImg)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)

    return(cellInstanses)
