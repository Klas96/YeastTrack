import os

def convertLifToTif(inPath, OutPath):
    cleanWorking = "rm ./VideoData/WorkingData/*"
    os.system(cleanWorking)

    series = 3
    channel = 1
    zoomLevel = 3
    filePath = inPath
    #Cropping Coordinates
    ulx,uly = (0,0)
    drx,dry = (512,512)

    #Convering -lif file with bioformats
    #Using nolookup option
    comand = "./bftools/bfconvert -nolookup"
    seriesFlag = " -series " + str(series)
    channelFlag = " -channel " + str(channel)
    zoomFlag = " -z " + str(zoomLevel)
    cropFlag = " -crop "+str(ulx)+","+str(uly)+","+str(drx)+","+str(dry)
    filePath = " " + filePath
    tifPath = " " + OutPath

    #cmd = comand + seriesFlag + cropFlag + channelFlag + zoomFlag + filePath + tifPath
    cmd = comand + seriesFlag + cropFlag + filePath + tifPath

    os.system(cmd)


def convertLifToTifNew(inPath, OutPath):
    cleanWorking = "rm ./VideoData/WorkingData/*"
    os.system(cleanWorking)

    series = 3
    channel = 1
    zoomLevel = 3
    filePath = inPath
    #Cropping Coordinates
    ulx,uly = (0,0)
    drx,dry = (10,10)

    #Convering -lif file with bioformats
    #Using nolookup option
    comand = "./bftools/bfconvert -nolookup"
    seriesFlag = " -series " + str(series)
    channelFlag = " -channel " + str(channel)
    zoomFlag = " -z " + str(zoomLevel)
    cropFlag = " -crop "+str(ulx)+","+str(uly)+","+str(drx)+","+str(dry)
    filePath = " " + filePath
    tifPath = " " + OutPath

    #cmd = comand + seriesFlag + cropFlag + channelFlag + zoomFlag + filePath + tifPath
    cmd = comand + seriesFlag + cropFlag + zoomFlag + filePath + tifPath

    os.system(cmd)
