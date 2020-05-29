posList = []

def onMouse(event, x, y, flags, param):
   global posList
   if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

def getCropCoordinates(mats):
    #Get last image
    #Import Image Crop
    cv2.imshow("SelectCropPos",mats[-2])
    cv2.setMouseCallback("SelectCropPos",onMouse)
    print(posList)
