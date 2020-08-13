from UserInterface.videoClass import Video
import cv2

def loadThreeZoomLevel():
    zom0Path = "VideoData/tileScan2/tileScan2OptZ0.avi"
    zom1Path = "VideoData/tileScan2/tileScan2OptZ1.avi"
    zom2Path = "VideoData/tileScan2/tileScan2OptZ2.avi"
    flo1Path = "VideoData/tileScan2/tileScan2Flo.avi"

    zom0Cap = cv2.VideoCapture(zom0Path)
    zom1Cap = cv2.VideoCapture(zom1Path)
    zom2Cap = cv2.VideoCapture(zom2Path)
    flo1Cap = cv2.VideoCapture(flo1Path)

    return Video(zom0Cap,zom1Cap,zom2Cap,flo1Cap)
