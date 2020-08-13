from Segmentation.ParmeterizeImagegs import imagesToPrameter
import pickle
import cv2
from matplotlib import pyplot as plt
from Segmentation.ConectedComponents import conectedCompontents
from Segmentation.FilterDetection import filterDetections

#Pre: Frame
#Ret: CellInstances in that frame
def rfSegmentetion(Frame):
    optImg = Frame.getOptImage()
    floImg = Frame.getFloImage()

    #Make Images To Parameters
    parm = imagesToPrameter(optImg,floImg)
    #Load Random Forest model
    rfModel = pickle.load(open("Segmentation/YeastCellRFModel", 'rb'))

    #Predic Segemt With Model
    result = rfModel.predict(parm)
    result = result.reshape((optImg.shape))

    #Grow Erode??   

    #Use Conected Components
    cellInstances = conectedCompontents(result,floImg)
    cellInstances = filterDetections(cellInstances)
    #Return Cell instance
    return(cellInstances)
