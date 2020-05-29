from UserInterface.videoClass import Video
import cv2

def imortTiftoVideo(filePath):
    numChan = 2
    numZoomLevles = 4
    etval, mats = cv2.imreadmulti(filePath)
    #8 images for each frame
    #TODO Generalize
    allFrames = []
    for matIndex in range(0,len(mats),8):
        frame = []
        optChan = []
        #optChan.append(mats[matIndex])
        #optChan.append(mats[matIndex+1])
        #optChan.append(mats[matIndex+2])
        optChan.append(mats[matIndex+3])
        floChan = []
        #floChan.append(mats[matIndex+4])
        floChan.append(mats[matIndex+5])
        #floChan.append(mats[matIndex+6])
        #floChan.append(mats[matIndex+7])
        frame.append(optChan)
        frame.append(floChan)
        allFrames.append(frame)
    video = Video(allFrames)
    del mats
    return(video)


def imortTiftoVideoNew(filePath):
    numChan = 2
    numZoomLevles = 4
    etval, mats = cv2.imreadmulti(filePath)
    #8 images for each frame
    #TODO Generalize
    allFrames = []
    for matIndex in range(0,len(mats)-1,2):
        frame = []
        frame.append(mats[matIndex])
        frame.append(mats[matIndex+1])
        allFrames.append(frame)

    video = Video(allFrames)
    del mats
    return(video)
