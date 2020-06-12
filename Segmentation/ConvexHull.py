import cv2
import numpy as np

#Pre: Binary image
#Ret: ConvexHull Binary image
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
