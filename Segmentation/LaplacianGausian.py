import cv2
from Segmentation.cellInstance import cellInstance
import numpy as np
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.FilterDetection import filterDetections
#from frameClass import rescale_frame

#LAP MEthoth for segmentation of yeast cells.
def laplacianGausian(frame):
    optFrame = frame.getOptChan()
    floFrame = frame.getFloChan()
    kernelSize = 3;
    scale = 1;
    delta = 0;
    ddepth = cv2.CV_16S;
    gaussian = cv2.GaussianBlur(optFrame, (3, 3), 0)
    gaussianShow = rescale_frame(gaussian,1000)
    cv2.imshow("gaussian", gaussianShow)
    cv2.waitKey(0)
    #cv2.imwrite("gaussian", gaussianShow)
    gaussian = cv2.cvtColor(gaussian, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gaussian, ddepth, ksize=kernelSize)
    laplacian = cv2.convertScaleAbs(laplacian)
    laplacianShow = rescale_frame(laplacian,1000)
    cv2.imshow("Laplacian", laplacianShow)
    cv2.waitKey(0)
    #cv2.imwrite("Laplacian", laplacianShow)

    return([])


def rescale_frame(frame, percent=75):
    width = int(frame.shape[1] * percent/100)
    height = int(frame.shape[0] * percent/100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation =cv2.INTER_AREA)
