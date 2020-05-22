def getSigmaEdegeToEdge(doughter,mother):
    distMD = getEdgeToEdgeDist(doughter,mother)
    #relatabelityFactor higher The closer the distance is to cellRadius
    slopeFactor = 1.3
    midPoint = 140
    sigmaDist = 1-1/(1+slopeFactor**(midPoint-distMD))
    return(sigmaDist)

def getEdgeToEdgeDist(doughter,mother):
    doughterDiscovFrame = doughter.getDetectionFrameNum()
    #Get Dist between cells att discovery moment
    dContour = doughter.getContour(pos = doughterDiscovFrame)
    mContour = mother.getContour(pos = doughterDiscovFrame)

    #Make Distance betven all points in countours

    minDist =  float('inf')
    for pnt1 in dContour:
        pnt1 = pnt1[0]
        for pnt2 in mContour:
            pnt2 = pnt2[0]
            distPnts = (pnt1[0]-pnt2[0])**2
            distPnts = distPnts + (pnt1[1]-pnt2[1])**2
            distPnts = distPnts ** 0.5
            if(distPnts < float('inf')):
                minDist = distPnts

    return(minDist)
