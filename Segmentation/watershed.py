import numpy as np
import cv2
from matplotlib import pyplot as plt
from Segmentation.cellInstance import cellInstance
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.FilterDetection import filterDetections
from Segmentation.OstuBinarizartion import getMaskFrame
from Segmentation.getThreshold import getTherholdImage
#watershed
#Pre: Frame As defined in main
#Ret1: List of cellInstanses
def watershed(frame):
    openingThres = 25

    optFrame = frame.getScaledOptChan()
    floFrame = frame.getScaledFloChan()

    gray = cv2.cvtColor(floFrame,cv2.COLOR_BGR2GRAY)

    #Thresolding
    #ret, thresh = cv2.threshold(gray,openingThres,255,cv2.THRESH_BINARY)
    thresh = getTherholdImage(frame)

    # noise removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel, iterations = 2)
    opening = cv2.cvtColor(opening, cv2.COLOR_BGR2GRAY)
    # sure background area
    sureBG = cv2.dilate(opening,kernel,iterations=3)

    # Finding sure foreground area
    #opening = np.uint8(opening)
    #opening = cv2.convertTo(opening, CV_8UC1);

    distTransform = cv2.distanceTransform(opening,cv2.DIST_L2,5)
    ret, sureFG = cv2.threshold(distTransform,0.65*distTransform.max(),255,0)

    #Finding unknown region
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG,sureFG)

    #Marker labelling
    ret, markers = cv2.connectedComponents(sureFG)

    markers = markers+1

    #Finding unknown region
    sureFG = np.uint8(sureFG)
    unknown = cv2.subtract(sureBG,sureFG)

    #Mark unknown region with 0
    markers[unknown==255] = 0

    markers = cv2.watershed(floFrame,markers)
    #markers = cv2.watershed(distTransform,markers)

    floFrame[markers == -1] = [0,0,255]

    markersShow = np.array(markers, dtype=np.uint8)

    markersShow = cv2.cvtColor(markersShow, cv2.COLOR_GRAY2BGR)
    markersShow[markers == -1] = [255,255,255]
    markersShow = cv2.add(markersShow,floFrame)
    cv2.imshow("markers",markersShow)
    cv2.waitKey(0)
    cellInstanses = conectedCompontents(markersShow,floFrame)
    cellInstanses = filterDetections(cellInstanses)
    #print(cellInstanses)
    return(cellInstanses)

def conectedCompontents(frame,floFrame):
    #Frame to CV_8UC1
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY);
    #gray = frame
    conectedCompontents, hirearchy = cv2.findContours(gray, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floFrame)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)

    return(cellInstanses)
