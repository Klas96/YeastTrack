import cv2
import numpy as np
from Segmentation.cellInstance import cellInstance
from Segmentation.getWHI5Activity import getWHI5Activity
#import getWHI5Activity
#from main import Frame

#OstuBinarization
#Pre: Frame As defined in main
#Ret1: keyPoints for each cell
#Ret2: Frame With segmentation for each Cell
def OtsuBinarization(frame):
    optFrame = frame.getScaledOptChan()
    floFrame = frame.getScaledFloChan()
    maskFrame = getMaskFrame(optFrame)
    keyPoints = blobDetection(maskFrame)
    cellInstanses = conectedCompontents(maskFrame,floFrame)
    return(maskFrame,keyPoints,cellInstanses)

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

    # create an empty black image
    drawing = np.zeros((frame.shape[0], frame.shape[1], 3), np.uint8)

    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # green - color for contours
        color = (255, 0, 0) # blue - color for convex hull
        # draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)

    for i in range(len(contours)):
        drawing = cv2.fillPoly(drawing, pts =[hull[i]], color=(255,255,255))

    return(drawing)
    #cv2.imshow("ConvexHull",drawing)
    #cv2.waitKey(0)

#Pre: frame with cells isolated in white
#Ret: KeyPoints for each cell.
def blobDetection(frame):
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    #Filter by size
    params.filterByArea = True
    params.minArea = 2
    params.maxArea = 100000

    #Filter by color
    params.filterByColor = True;
    params.blobColor = 255;

    # Filter by Circularity
    #params.filterByCircularity = True
    #params.minCircularity = 0.1

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
    	detector = cv2.SimpleBlobDetector(params)
    else :
    	detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(frame)

    return(keypoints)

def conectedCompontents(frame,floFrame):
    #Frame to CV_8UC1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);

    conectedCompontents, hirearchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cellInstanses = []
    for cnt in conectedCompontents:
        moments = cv2.moments(cnt)
        #TOOD Byt till funktioner ist??
        cx = int(moments['m10']/moments['m00'])
        cy = int(moments['m01']/moments['m00'])
        position = (cx,cy)
        area = moments['m00']
        whi5Activ = getWHI5Activity(cnt,floFrame)
        #area = cv2.contourArea(cnt)
        cellInstans = cellInstance(position,area,whi5Activ)
        cellInstanses.append(cellInstanses)

    return(cellInstanses)

def otsuThreshold(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #apply thresholding
    gotFrame, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(thresh)
