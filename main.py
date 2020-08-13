#Yeast Track Main
import cv2
#from UserInterface.videoClass import Video
from UserInterface.LoadData.LoadData import getVideo
from UserInterface.LoadData.LoadtifFile import imortTiftoVideoNew
from UserInterface.Controls import Controls
from UserInterface.LoadData.ImportThreeZoomLevel import loadThreeZoomLevel
from UserInterface.LoadData.LoadChannels import loadChannels

#video = loadThreeZoomLevel()
video = loadChannels()

video.runTracking()

cntrl = Controls(video)

cntrl.startControls()
