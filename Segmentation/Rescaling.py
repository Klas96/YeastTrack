import cv2
#Rescale for optimal analysis size
#What is this size??
def rescaleImage(img,portion):
    width = int(img.shape[1] * portion)
    height = int(img.shape[0] * portion)
    dim = (width, height)
    return cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
