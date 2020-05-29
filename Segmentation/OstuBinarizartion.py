import cv2
import numpy as np
from Segmentation.cellInstance import cellInstance
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.FilterDetection import filterDetections
from Segmentation.getThreshold import getTherholdImage
#import getWHI5Activity
#from main import Frame

#OstuBinarization
#Pre: Frame As defined in main
#Ret1: keyPoints for each cell
#Ret2: Frame With segmentation for each Cell
def OtsuBinarization(frame):
    optFrame = frame.getScaledOptChan()
    floFrame = frame.getScaledFloChan()
    #getTherholdImage(frame)
    #optFrame = cv2.GaussianBlur(optFrame, (3, 3), 0)
    #cv2.imshow("optFrame",optFrame)
    #cv2.waitKey(0)
    maskFrame = getMaskFrame(optFrame)
    cellInstanses = conectedCompontents(maskFrame,floFrame)
    cellInstanses = filterDetections(cellInstanses)
    return(cellInstanses)

#Pre: VideoFrame
#Ret: White on black maskFrame
def getMaskFrame(frame):
    frame = otsuThreshold(frame)
    maskFrame = convexHull(frame)
    return(maskFrame)

#Pre: takes An binary image
#Ret: Returns Image with conexHull filled of all wite separated images
def convexHull(frame):
    # Finding contours for the thresholded image

    contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #im2, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # create hull array for convex hull points
    hull = []
    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))

    #Create an empty black image
    drawing = np.zeros((frame.shape[0], frame.shape[1], 3), np.uint8)

    #Draw contours
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        #Draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)

    for i in range(len(contours)):
        drawing = cv2.fillPoly(drawing, pts =[hull[i]], color=(255,255,255))

    return(drawing)
    #cv2.imshow(area = "ConvexHull",drawing)
    #cv2.waitKey(0)

def conectedCompontents(frame,floFrame):
    #Frame to CV_8UC1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    conectedCompontents, hirearchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floFrame)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)

    return(cellInstanses)

def otsuThreshold(image):
    try:
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    except:
        gray = image

    #apply thresholding
    gotFrame, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(thresh)
