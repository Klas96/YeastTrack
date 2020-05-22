import os


def convertLifToTif(inPath, OutPath):
    cleanWorking = "rm ./VideoData/WorkingData/*"
    os.system(cleanWorking)

    series = 3
    channel = 1
    zoomLevel = 3
    filePath = inPath
    comand = "./bftools/bfconvert -nolookup"
    seriesFlag = " -series " + str(series)
    channelFlag = " -channel " + str(channel)
    zoomFlag = " -z " + str(zoomLevel)
    cropFlag = " -crop 0,0,512,512"
    filePath = " " + filePath
    tifPath = " " + OutPath

    #cmd = comand + seriesFlag + cropFlag + channelFlag + zoomFlag + filePath + tifPath
    cmd = comand + seriesFlag + filePath + tifPath

    os.system(cmd)
