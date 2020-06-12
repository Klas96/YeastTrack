import cv2
from Segmentation.getWHI5Activity import getWHI5Activity

def conectedCompontents(img,floFrame):
    conectedCompontents, hirearchy = cv2.findContours(img, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floFrame)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)
    return(cellInstanses)
