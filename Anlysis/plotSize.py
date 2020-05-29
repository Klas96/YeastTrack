from matplotlib import pyplot as plt
#from Anlysis.plotSize import plotTrackCellSizeBudToMother
from Anlysis.FitExponential import fitExponential
from Anlysis.FitExponential import plotDataWithExpo

def plotTrackCellSizeBudToMother(cellToPlot, trackedCells):
    #add to Mother trace
    #return mother trace
    for mother in trackedCells:
        cellID = mother.getCellID()
        #find Doughter cells
        if any(cellID == i for i in cellToPlot):
            #Get Mother Trace
            motherSizeTrace = mother.getSizesTrace()
            dicovFrame = mother.getDetectionFrameNum()
            #Get doughters
            doughters = findDoughetCells(mother, trackedCells)
            doughters = [6,13]
            #loopThrough all doughters
            for doughter in trackedCells:
                dougherID = doughter.getCellID()
                #find Doughter cells
                if any(dougherID == i for i in doughters):
                    #Get Doughter trace cuted
                    dougherDiscovFrame = doughter.getDetectionFrameNum()
                    motherSizeTrace = addBudtoMother(motherSizeTrace,doughter)
            #plt.plot(range(dicovFrame, dicovFrame+len(motherSizeTrace)),motherSizeTrace, label="ID " + str(cellID))
            plotDataWithExpo(motherSizeTrace)

    #PlotDoughters
    for doughter in trackedCells:
        dougherID = doughter.getCellID()
        #find Doughter cells
        if any(dougherID == i for i in doughters):
            #Get Doughter trace cuted
            dicovFrame = doughter.getDetectionFrameNum()
            sizeTrace = doughter.getSizesTrace()
            #plt.plot(range(dicovFrame, dicovFrame+len(sizeTrace)),sizeTrace, label="ID " + str(dougherID))


    #plt.ylabel('Growth Curves')
    #plt.xlabel('Time')
    #plt.title("Size")
    #plt.xticks([])
    #plt.yticks([])
    #plt.legend()
    #plt.show()


def addBudToMother(mother,trackedCells,idOfBuds):
    motherCellTrace = mother.getSizesTrace()
    for trCell in trackedCells:
        cellID = trCell.getCellID()
        if any(cellID == i for i in idOfBuds):
            motherCellTrace = addBudtoMother(mother,trCell)
    return(motherCellTrace)

def findDoughandAddBudToMother(mother,trackedCells):
    motherCellTrace = mother.getSizesTrace()
    daugthers = findDoughetCells(mother, trackedCells)
    for trCell in trackedCells:
        cellID = trCell.getCellID()
        if any(cellID == i for i in daugthers):
            motherCellTrace = addBudtoMother(mother,trCell)
    plt.show()
    return(motherCellTrace)

def findDoughetCells(mother, trackedCells):
    motherID = mother.getCellID()
    doughters = []
    for trCell in trackedCells:
        if motherID == trCell.getMotherCell():
            doughters.append(trCell.getCellID())
    return(doughters)

def addBudtoMother(motherTrace,doughter):
    deviInst = getDevisionInst(doughter)
    doughterSizeTrace = doughter.getSizesTrace()[:deviInst]
    for dSzI in range(len(doughterSizeTrace)):
        dSz = doughterSizeTrace[-dSzI]
        motherTrace[deviInst-dSzI] = motherTrace[deviInst-dSzI] + dSz
    #param = fitExponential(motherTrace[(deviInst-len(doughterSizeTrace)):deviInst])
    return(motherTrace)


#Returnsfirst Whi5 activation
def getDevisionInst(doughter):
    thresh = 0.30
    cellWhi5Trace = doughter.getWhi5Trace()
    index = 0
    finalIndex = doughter.getDetectionFrameNum()
    for whi5 in cellWhi5Trace:
        index = index + 1
        if whi5 > thresh:
            finalIndex = index+finalIndex
            plt.axvline(x=finalIndex, color=colorsd, linestyle='--')
            break
    return(finalIndex)
