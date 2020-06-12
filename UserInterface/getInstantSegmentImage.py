import cv2
import numpy as np
from UserInterface.getMaskImage import getMaskImage

#color all the blobs with individual colors
#Text size for all cells
def getCellInstImage(listOfCellInstances,sizeX,sizeY):
    colorSet =  [(0,7,100),(32,107,203),(237, 120, 255),(255, 170,0),(100,2,100)]

    drawing = np.zeros((sizeX,sizeY, 3), np.uint8)

    for cellInstances in listOfCellInstances:
        cnt = cellInstances.getContour()
        convexHull = cv2.convexHull(cnt, False)
        col = colorSet[trackedCell.getCellID() % len(colorSet)]
        drawing = cv2.fillPoly(drawing, pts =[convexHull], color=col)

    return(drawing)
