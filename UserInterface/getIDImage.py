import cv2
import numpy as np
from UserInterface.rescaleImageToUser import rescaleImageToUser
from UserInterface.rescaleImageToUser import rescalePosToUser
from UserInterface.rescaleImageToUser import rescaleCounur
from Tracking.GetPositionFromContour import getPositionFromContour

#Pre1: list of objects
#Pre2: frame
def getIDImage(listOfObjects,frame):
    szX = frame.xSz
    szY = frame.ySz
    numCol = 3
    idImg = np.zeros((szX,szY, numCol), np.uint8)
    idImg = rescaleImageToUser(idImg)
    #Loop over the tracked objects
    for trackedCell in listOfObjects:
        #Draw both the ID of the object and the centroid
        idText = "ID " + str(trackedCell.getCellID())
        (centerX,centerY) = trackedCell.getCentroid()
        #contour = trackedCell.getContour()
        #contour = rescaleCounur(contour,[szX,szY])
        #(centerX,centerY) = getPositionFromContour(contour)
        (centerX,centerY) = rescalePosToUser((centerX,centerY),frame.getOptImage().shape)
        #Put Text and Cetroid
        #print(idText)
        #print((centerX,centerY))
        cv2.putText(idImg, idText, (centerX-10,centerY-25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(idImg, (centerX,centerY), 10, (0, 255, 0), -1)
        #cv2.circle(idImg, (centerX,centerY), 1, (0, 255, 0), -1)
    #idImg = rescaleImageToUser(idImg)
    #Return
    return(idImg)
