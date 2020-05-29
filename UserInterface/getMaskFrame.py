import cv2
import numpy as np

#Pre: VideoFrame
#Ret: White on black maskFrame
def getMaskFrame(frame):
    frame = otsuThreshold(frame)
    maskFrame = convexHull(frame)
    return(maskFrame)

def otsuThreshold(frame):
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #apply thresholding
    gotFrame, thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    return(thresh)

#Pre: takes An image Black and white
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
