import cv2
import numpy as np

#Pre1: Keypoint All cells
#Pre2: Mask Frame With cells
#Pre3: Florecent Chanell
#Ret: Array with numberes corresponding to WHI5 Activity
def getWHI5Activity(countour, floChan):
    #convexHull = cv2.ConvexHull2(countour,orientation=CV_CLOCKWISE, return_points=0)
    convexHull = cv2.convexHull(countour, False)

    drawing = np.zeros((floChan.shape[0], floChan.shape[1], 3), np.uint8)

    drawing = cv2.fillPoly(drawing, pts =[convexHull], color=(255,255,255))

    #Take intesection floChan and convexHull
    mask_out=cv2.subtract(drawing,floChan)

    mask_out=cv2.subtract(drawing,mask_out)
    whi5Activ = cv2.sumElems(mask_out)
    return(whi5Activ[1])
