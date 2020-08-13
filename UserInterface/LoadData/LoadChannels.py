import cv2
from UserInterface.videoClass import Video

def loadChannels():
    filePathOpt = "VideoData/tileScan2/tileScan2OptZ2.avi"
    filePathFlo = "VideoData/tileScan2/tileScan2Flo.avi"

    filePathOpt = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/tileScan1/130419opt.avi"
    filePathFlo = "/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/VideoData/tileScan1/130419flo.avi"

    filePathOpt = "VideoData/Experiment13h_050619/vidP4C1Z4.avi"
    filePathFlo = "VideoData/Experiment13h_050619/vidP4C2Z2.avi"

    #Get video Capture
    vidOpt = cv2.VideoCapture(filePathOpt)
    vidFlo = cv2.VideoCapture(filePathFlo)
    video = Video(vidOpt,vidFlo)
    return(video)
