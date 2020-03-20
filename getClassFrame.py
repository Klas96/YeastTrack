import cv2
import numpy as np
from getMaskFrame import getMaskFrame
from detectCell import blobDetection

#color all the blobs with individual colors
#Text size for all cells
def getClassFrame(keyPoints,maskFrame):
    #loop Through all keypoints
    for keyP in keyPoints:
        #color the blob at keyP a sertain color
        pass

    #get size of frame
    skape = maskFrame.shape[0]
    textFrame = getTextFrame(keyPoints,maskFrame.shape[0],maskFrame.shape[1])
    return(maskFrame)



def getTextFrame(keyPoints,sizeX,sizeY):

    #im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # create an empty black image
    classFrame = np.zeros((sizeX,sizeY, 3), np.uint8)

    #Font pararm
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (255, 255, 255)
    thickness = 1

    for keyP in keyPoints:
        (orgX,orgY) = keyP.pt
        orgX = int(orgX)
        orgY = int(orgY)
        size = keyP.size
        size = int(size)
        #write the size in frame
        # Using cv2.putText() method
        classFrame = cv2.putText(classFrame, str(size), (orgX,orgY), font, fontScale, color, thickness, cv2.LINE_AA)

    return(classFrame)

#Test method
#frame = cv2.imread('ImageData/VidEamp.png')
#maskFrame = getMaskFrame(frame)
#keyPoints = blobDetection(maskFrame)
#classFrame = getClassFrame(keyPoints,maskFrame)

#cv2.imshow('classFrame',classFrame)
#cv2.waitKey(0)
