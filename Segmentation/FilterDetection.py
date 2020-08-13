import cv2
import numpy as np

#Pre: detections
#Ret: Filtered Detections
def filterDetections(cellInstances):
    maxSize = 210
    minSize = 15
    filterdList = []
    for cellInst in cellInstances:
        size = cellInst.getSize()
        if size < maxSize and size > minSize:
            filterdList.append(cellInst)
    return(filterdList)
