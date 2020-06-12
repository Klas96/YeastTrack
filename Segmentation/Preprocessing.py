from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import exposure
import cv2
import numpy as np

#Preprossesing of image using rescaling meanfiltering with sigma estimator and histogram equalization
#Pre: image Raw
#Ret: preprocessed image
def preprocess(img):
    #Rescaling
    #img = rescale_frame(img, percent=1000)
    #Decreasing noise
    img = cv2.fastNlMeansDenoising(img)
    #increasing contrast
    #img = cv2.equalizeHist(img)
    return(img)

def preprocessFloImg(img):
    img = cv2.fastNlMeansDenoising(img)
    #img = rescale_frame(img, percent=1000)
    return(img)

#Rescale for optimal analysis size
#Pre1: Image as numpy array
#Pre2:
#Ret:
def rescale_frame(image, percent=1000):
    width = int(image.shape[1] * percent/100)
    height = int(image.shape[0] * percent/100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
