import cv2
import numpy as np
from UserInterface.getMaskImage import getMaskImage
from UserInterface.rescaleImageToUser import rescaleImageToUser

#color all the blobs with individual colors
#Text size for all cells
def getClassImage(listOfObjects,sizeX,sizeY):
    colorSet =  [(0,7,100),(32,107,203),(237, 120, 255),(255, 170,0),(100,2,100)]

    classImg = np.zeros((sizeX,sizeY, 3), np.uint8)

    for trackedCell in listOfObjects:
        cnt = trackedCell.getContour()
        convexHull = cv2.convexHull(cnt, False)
        col = colorSet[trackedCell.getCellID() % len(colorSet)]
        classImg = cv2.fillPoly(classImg, pts =[convexHull], color=col)

    classImg = rescaleImageToUser(classImg)

    return(classImg)
