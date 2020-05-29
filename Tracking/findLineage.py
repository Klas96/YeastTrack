from scipy.spatial import distance as dist
import numpy as np
from matplotlib import pyplot as plt
from Tracking.getEdgeToEdgeDist import getSigmaEdegeToEdge

def findLineage(trackedCells):

    for doughter in trackedCells:
        maxRelFactor = 0.0
        for mother in trackedCells:
            relFactor = getRelatabelityFactor(doughter,mother)
            if relFactor > maxRelFactor:
                maxRelFactor = relFactor
                doughter.setMotherCell(mother.getCellID(),relFactor)
    #anlyseRelatabelityFactor()

#Pre: Two TrackedCell objects
#Ret: number between 0 and 1 reflecting how likely they are to be related
def getRelatabelityFactor(doughter,mother):
    relatabelityFactor = -1

    doughterDetectFrame = doughter.getDetectionFrameNum()
    motherDetectFrame = mother.getDetectionFrameNum()

    #Number of frames must have exsisted befor being abale to be mother
    buddFrameNum = 10

    if motherDetectFrame+buddFrameNum > doughterDetectFrame:
        return(relatabelityFactor)

    if doughter.getCellID() == mother.getCellID():
        return(relatabelityFactor)

    #distFactorOLD = getDistFacorSigma(doughter,mother)
    distFactor = getSigmaEdegeToEdge(doughter,mother)

    whi5Factor = getWHI5Factor(doughter,mother)

    #print("D: " + str(doughter.getCellID()) + " M: " + str(mother.getCellID()))
    #print("distFactor: " + str(distFactorNEW))
    #print("whi5Factor: " + str(whi5Factor))

    distWeight = 1.5
    whi5Weight = 1
    relatabelityFactor = ((distFactor**distWeight)*(whi5Factor**whi5Weight))
    return(relatabelityFactor)


def getDistFacorSigma(doughter,mother):
    doughterDiscovFrame = doughter.getDetectionFrameNum()
    #Get Dist between cells att discovery moment
    (douX,douY) = doughter.getCentroid(doughterDiscovFrame)
    (motX,motY) = mother.getCentroid(doughterDiscovFrame)
    distMD = (douX-motX)*(douX-motX)
    distMD = distMD + (douY-motY)*(douY-motY)
    distMD = distMD ** 0.5
    #relatabelityFactor higher The closer the distance is to cellRadius
    slopeFactor = 1.3
    midPoint = 140
    sigmaDist = 1-1/(1+slopeFactor**(midPoint-distMD))
    return(sigmaDist)

#Ret: portion of anlyse frames in which cell whi5 over threshold.
#pre1: DoughterTrackedCell
#pre2: MotherTrackdeCell
def getWHI5Factor(doughter,mother):
    analysisSpan = 50
    intensThreshold = 0.30
    binaryFactor = 0

    #Extract traces
    whi5Mother = mother.getWhi5Trace()

    doughterDetectFrame = doughter.getDetectionFrameNum()
    motherDetectFrame = mother.getDetectionFrameNum()

    #Take 50 elements after doughter cell have been detected.
    #If 50 elements are not availibal take elements to end.

    startMotherWhi5arr = motherDetectFrame-doughterDetectFrame

    if len(whi5Mother) < (startMotherWhi5arr+analysisSpan):
        whi5Mother = whi5Mother[startMotherWhi5arr:startMotherWhi5arr+analysisSpan]
    else:
        whi5Mother = whi5Mother[startMotherWhi5arr:-1]

    whi5Factor = 0
    for whi5 in whi5Mother:
        if(whi5 > intensThreshold):
            whi5Factor = whi5Factor + 1

    #Dont want to compleatly exclude the onece with 0 whi5
    baseConsidFactor = 0.1
    whi5Factor = max(whi5Factor/len(whi5Mother),0.1)
    return(whi5Factor)


def findWHI5BothPeak(doughter,mother):
    analysisSpan = 50

    #Extract traces
    whi5Doughter = doughter.getWhi5Trace()
    whi5Mother = mother.getWhi5Trace()

    doughterDetectFrame = doughter.getDetectionFrameNum()
    motherDetectFrame = mother.getDetectionFrameNum()
    #Take 50 elements after doughter cell have been detected.
    #If 50 elements are not availibal take elements to end.
    if len(whi5Doughter) < analysisSpan:
        whi5Doughter = whi5Doughter[:analysisSpan]
    else:
        whi5Doughter = whi5Doughter[:-1]

    startMotherWhi5arr = motherDetectFrame-doughterDetectFrame

    if len(whi5Mother) < (startMotherWhi5arr+analysisSpan):
        whi5Mother = whi5Mother[startMotherWhi5arr:startMotherWhi5arr+analysisSpan]
    else:
        whi5Mother = whi5Mother[startMotherWhi5arr:-1]

    meanIntensDoughter = sum(whi5Doughter)/len(whi5Doughter)
    meanIntensMother = sum(whi5Mother)/len(whi5Mother)
    maxIntensDoughter = max(whi5Doughter)
    maxIntensMother = max(whi5Mother)

    bothPeakFactor = maxIntensDoughter*maxIntensMother

    return(bothPeakFactor)

def findWHI5Correlation(doughter,mother):
    analysisSpan = 50

    #Extract traces
    whi5Doughter = doughter.getWhi5Trace()
    whi5Mother = mother.getWhi5Trace()

    doughterDetectFrame = doughter.getDetectionFrameNum()
    motherDetectFrame = mother.getDetectionFrameNum()

    #Take 50 elements after doughter cell have been detected.
    #If 50 elements are not availibal take elements to end.
    if len(whi5Doughter) < analysisSpan:
        whi5Doughter = whi5Doughter[:analysisSpan]
    else:
        whi5Doughter = whi5Doughter[:-1]

    startMotherWhi5ardistFactorr = motherDetectFrame-doughterDetectFrame
    if len(whi5Mother) < (startMotherWhi5arr+analysisSpan):
        whi5Mother = whi5Mother[startMotherWhi5arr:startMotherWhi5arr+analysisSpan]
    else:
        whi5Mother = whi5Mother[startMotherWhi5arr:-1]

    #Check if same length else cut to shortest.
    if len(whi5Mother) < len(whi5Doughter):
        whi5Doughter = whi5Doughter[:len(whi5Mother)]
    if len(whi5Doughter) < len(whi5Mother):
        whi5Mother = whi5Mother[:len(whi5Doughter)]

    whi5correlation = np.correlate(whi5Mother,whi5Doughter)
    return(whi5correlation)
