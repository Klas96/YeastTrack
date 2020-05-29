import cv2
import numpy as np

def filterDetections(cellInstances):
    maxSize = 10000
    minSize = 100
    filterdList = []
    for cellInst in cellInstances:
        size = cellInst.getSize()
        if size < maxSize and size > minSize:
            filterdList.append(cellInst)
    return(filterdList)
