import cv2
import numpy as np

def getIDFrame(listOfObjects,frame):
    sizeX = frame.xScaleSz
    sizeY = frame.yScaleSz
    numCol = 3
    if 2 == len(frame.getOptChan().shape):
        numCol = 1
    idFrame = np.zeros((sizeX,sizeY, numCol), np.uint8)
    
    # loop over the tracked objects
    for trackedCell in listOfObjects:
        # draw both the ID of the object and the centroid of the
        # object on the output frame
        idText = "ID " + str(trackedCell.getCellID())

        (centerX,centerY) = trackedCell.getCentroid()

        cv2.putText(idFrame, idText, (centerX-10,centerY-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(idFrame, (centerX,centerY), 4, (0, 255, 0), -1)

    return(idFrame)


def getIDFrameNY(listOfObjects, frame):
    sizeX = frame.getScaledOptChan().shape[0]
    sizeY = frame.getScaledOptChan().shape[1]

    #Check num colers
    numCol = 3
    if 2 == len(frame.getScaledOptChan().shape):
        numCol = 1
    print(numCol)
    idFrame = np.zeros((sizeX,sizeY, numCol), np.uint8)

    # loop over the tracked objects
    for trackedCell in listOfObjects:
        # draw both the ID of the object and the centroid of the
        # object on the output frame
        if(trackedCell.getDetectionFrameNum() <= frame.getFrameNum()):
            idText = "ID " + str(trackedCell.getCellID())
            (centerX,centerY) = trackedCell.getCentroid(frame.getFrameNum())

            cv2.putText(idFrame, idText, (centerX-10,centerY-10),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            cv2.circle(idFrame, (centerX,centerY), 4, (0, 255, 0), -1)

    return(idFrame)
