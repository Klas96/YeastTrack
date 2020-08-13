import cv2
from Segmentation.getWHI5Activity import getWHI5Activity
from Segmentation.cellInstance import cellInstance

def conectedCompontents(maskImg,floImg):
    conectedCompontents, hirearchy = cv2.findContours(maskImg, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    cellInstanses = []
    for cnt in conectedCompontents:
        whi5Activ = getWHI5Activity(cnt,floImg)
        cellInstans = cellInstance(cnt,whi5Activ)
        cellInstanses.append(cellInstans)
    return(cellInstanses)
