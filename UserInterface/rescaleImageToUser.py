import cv2

#Scale image For Visual Apropriate Size
#Pre: image
#Ret: Scaled image
def rescaleImageToUser(img):
    prop = getScaleProprtion(img.shape)
    szX = int(img.shape[1]/prop)
    szY = int(img.shape[0]/prop)
    dim = (szX, szY)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    return(img)

#Pre1: Centroid
#Pre2: frame
#Ret: REscaled cetroid
def rescalePosToUser(centroid,imgShape):
    prop = getScaleProprtion(imgShape)
    (centerX,centerY) = centroid
    #print(centroid)
    centerX = int(centerX/prop)
    centerY = int(centerY/prop)
    centroid = (centerX,centerY)
    #print(centroid)
    return(centroid)

def rescaleCounur(contour,imgShape):
    scaledCnt = []
    for cntPt in contour:
        cntPt = cntPt[0]
        cntPt = rescalePosToUser(cntPt,imgShape)
        scaledCnt.append(cntPt)
    return(scaledCnt)


#Gives Scale proportion
#Pre: image shape
#Ret: Proportion to scale to get good visual
def getScaleProprtion(imgSape):
    userSzX = 1200
    userSzY = 800
    xSzProp = imgSape[1]/userSzX
    ySzProp = imgSape[0]/userSzY
    prop = max(xSzProp,ySzProp)
    return(prop)
