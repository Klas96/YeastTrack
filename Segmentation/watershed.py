import numpy as np
import cv2
from matplotlib import pyplot as plt

#watershed
#Pre: Frame As defined in main
#Ret1: keyPoints for each cell
#Ret2: Frame With segmentation for each Cell
def watershed(frame):
    optFrame = frame.getScaledOptChan()
    floFrame = frame.getScaledFloChan()

    gray = cv2.cvtColor(floFrame,cv2.COLOR_BGR2GRAY)

    #Thresolding
    ret, thresh = cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)

    # sure background area
    sureBG = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    distTransform = cv2.distanceTransform(opening,cv2.DIST_L2,3)
    ret, sureFG = cv2.threshold(distTransform,0.70*distTransform.max(),255,0)

    cv2.imshow("distTrans",distTransform)
    cv2.imshow("sureFG",sureFG)

    # Finding unknown region
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG,sureFG)

    # Marker labelling
    ret, markers = cv2.connectedComponents(sureFG)

    # Finding unknown region
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG,sureFG)

    # Now, mark the region of unknown with zero
    markers[unknown==255] = 0

    markers = cv2.watershed(floFrame,markers)
    floFrame[markers == -1] = [255,0,0]

    #TODO Find Keypoints

    cv2.imshow("floFrame",floFrame)
