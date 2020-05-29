import cv2
from Segmentation.FilterDetection import filterDetections
import numpy as np

#Threshold Image that
#Pre: Frame objecet
#Ret: Threshold Image
def getTherholdImage(frame):
    optFrame = frame.getScaledOptChan()
    floFrame = frame.getScaledFloChan()

    gaussian = cv2.GaussianBlur(optFrame, (3, 3), 0)

    gray = cv2.cvtColor(gaussian,cv2.COLOR_BGR2GRAY)
    gotFrame, thresh = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
    #Remove background
    thresh = removeLargestConected(thresh)
    #cv2.imshow("Thresh",thresh)
    #cv2.waitKey(0)
    return(thresh)


def removeLargestConected(image):
    conectedCompontents, hirearchy = cv2.findContours(image, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    drawing = np.zeros((image.shape[0], image.shape[1], 3), np.uint8)
    cellSize = 4500
    sizeThreshold = cellSize*10

    for cnt in conectedCompontents:
        #check Size

        if(sizeThreshold > cv2.contourArea(cnt)):
            #drawing = cv2.fillPoly(drawing, pts =cnt[0], color=(255,255,255))
            #drawing = cv2.drawContours(drawing, [cnt], 0, (0,255,0), 3)
            drawing = cv2.fillPoly(drawing, pts =[cnt], color=(255,255,255))
    return(drawing)


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
    #cv2.imshow("ConvexHull",drawing)
    #cv2.waitKey(0)
