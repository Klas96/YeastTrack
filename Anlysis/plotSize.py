from matplotlib import pyplot as plt
#from Anlysis.plotSize import plotTrackCellSizeBudToMother
from Anlysis.FitExponential import fitExponential
from Anlysis.FitExponential import plotDataWithExpo
from Anlysis.AddBudsToMother import addBudsToMother
from Anlysis.PlotTrackedCellsSize import plotTrackedCellsSize

#Pre1: List of number with cells to be ploted
#Pre2:
def plotTrackCellSizeBudToMother(cellToPlot, trackedCells):
    szTrc = []
    #add to Mother trace
    #return mother trace
    for mother in trackedCells:
        szTrc = []
        cellID = mother.getCellID()
        #find Doughter cells
        if any(cellID == i for i in cellToPlot):
            #Get doughters
            doughters = findDoughetCells(mother, trackedCells)
            #doughters = []
            szTrc = addBudsToMother(mother,doughters)
            plotTrackedCellsSize(doughters)

            #plt.show()
            plt.plot(range(len(szTrc)),szTrc, label="ID " + str(cellID))
            plt.ylabel('Growth Curves')
            plt.xlabel('Time')
            plt.title("Size")
            plt.xticks([])
            plt.yticks([])
            plt.legend()
            plt.show()


def addBudToMother(mother,trackedCells,idOfBuds):
    motherCellTrace = mother.getSizesTrace()
    for trCell in trackedCells:
        cellID = trCell.getCellID()
        if any(cellID == i for i in idOfBuds):
            motherCellTrace = addBudtoMother(mother,trCell)
    return(motherCellTrace)

def findDoughetCells(mother, trackedCells):
    motherID = mother.getCellID()
    doughters = []
    for trCell in trackedCells:
        if motherID == trCell.getMotherCell():
            doughters.append(trCell)
    return(doughters)


def addBudtoMotherOOOLD(motherTrace,doughter):
    deviInst = getDevisionInst(doughter)
    deviInst = 157
    doughterSizeTrace = doughter.getSizesTrace()
    doughterDetectFrame = 157 - len(doughterSizeTrace)
    startIt = doughterDetectFrame-(157-len(motherTrace))
    #print(startIt)
    for dSzI in range(len(doughterSizeTrace)):
        dSz = doughterSizeTrace[dSzI]
        motherTrace[startIt+dSzI] = motherTrace[startIt+dSzI] + dSz
    #param = fitExponential(motherTrace[(deviInst-len(doughterSizeTrace)):deviInst])
    return(motherTrace)

def addBudtoMother(motherTrace,doughter):
    deviInst = getDevisionInst(doughter)
    doughterSizeTrace = doughter.getSizesTrace()[:deviInst]
    for dSzI in range(len(doughterSizeTrace)):
        dSz = doughterSizeTrace[-dSzI]
        motherTrace[deviInst-dSzI] = motherTrace[deviInst-dSzI] + dSz
    #param = fitExponential(motherTrace[(deviInst-len(doughterSizeTrace)):deviInst])
    return(motherTrace)

#Returnsfirst Whi5 activation Index
def getDevisionInst(doughter):
    thresh = 0.30
    cellWhi5Trace = doughter.getWhi5Trace()
    index = 0
    for whi5 in cellWhi5Trace:
        index = index + 1
        if whi5 > thresh:
            index = index+doughter.getDetectionFrameNum()
            colorsd = 'C1'
            plt.axvline(x=index, color=colorsd, linestyle='--')
            break
    return(index)
