import numpy as np
import cv2
#Pre: frame
#ret: Frame with higer intesity
def incFloIntens(img,intens):
    intens = int(intens/10)
    #Check number of colors
    numCol = 3

    intensImg = np.zeros((img.shape[0], img.shape[1], numCol), np.uint8)
    for i in range(intens):
        intensImg = cv2.add(intensImg,img)
    return(intensImg)

#Merge
def increasIntens(img,currentBlend):
    img = incFloIntens(img,currentBlend)
    return(img)
