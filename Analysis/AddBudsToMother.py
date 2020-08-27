from Anlysis.getDevisionFrameNum import getDevisionFrameNum

#Pre1: Mother Tracked CellTrackel
#Pre2: list Doughters
def addBudsToMother(mother,doughters):
    sizeTrace = mother.getSizesTraceFromBegining()
    for dought in doughters:
        deviNum = getDevisionFrameNum(dought)
        dughtSzTrc = dought.getSizesTraceFromBegining()[0:deviNum]
        for i in range(min(len(sizeTrace),len(dughtSzTrc))):
            sizeTrace[i] += dughtSzTrc[i]
    return(sizeTrace)
