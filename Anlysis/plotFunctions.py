from matplotlib import pyplot as plt
from Anlysis.plotSize import plotTrackCellSizeBudToMother

def plotFunction(trackedCells):
    cellToPlot = range(len(trackedCells))
    plotTrackCellSizeBudToMother(cellToPlot, trackedCells)
    #plotTrackCellWhi5(cellToPlot, trackedCells)

#Pre1: ID number for cell
#Pre2: List of tracked cells.
def plotSizeLineage(cellID,trackedCells):
    cellsInLinage = [cellID]
    for trackCell in trackedCells:
        if(trackCell.getMotherCell() == cellID):
            cellsInLinage.append(trackCell.getCellID())
    cellsInLinage = [0,6,13]
    plotTrackCellSize(cellsInLinage, trackedCells)
    plotTrackCellWhi5(cellsInLinage, trackedCells)


def plotTrackCellSize(cellToPlot, trackedCells):
    for trackedCell in trackedCells:
        cellID = trackedCell.getCellID()
        if any(cellID == i for i in cellToPlot):
            whi5Trace = trackedCell.getSizesTrace()
            dicovFrame = trackedCell.getDetectionFrameNum()
            plt.plot(range(dicovFrame, dicovFrame+len(whi5Trace)),whi5Trace, label="ID " + str(cellID))

    plt.ylabel('Growth Curves')
    plt.xlabel('Time')
    plt.title("Size")
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()

def plotTrackCellWhi5(cellToPlot, trackedCells):
    for trackedCell in trackedCells:
        cellID = trackedCell.getCellID()
        if any(cellID == i for i in cellToPlot):
            whi5Trace = trackedCell.getWhi5Trace()
            dicovFrame = trackedCell.getDetectionFrameNum()
            plt.plot(range(dicovFrame, dicovFrame+len(whi5Trace)),whi5Trace, label="ID " + str(cellID))

    plt.ylabel('Whi5 Activity')
    plt.xlabel('Time')
    plt.title("Whi5 Activity")
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()


def plotPositions(cellToPlot, trackedCells):
    for trackedCell in trackedCells:
        cellID = trackedCell.getCellID()
        if any(cellID == i for i in cellToPlot):
            xPosTrace,yPosTrace = trackedCell.getPosTrace()
            plt.plot(xPosTrace,yPosTrace)#, label="ID " + str(cellID))

    plt.ylabel('y Position')
    plt.xlabel('x Position')
    plt.title("Position Trace")
    plt.xticks([])
    plt.yticks([])
    plt.legend()
    plt.show()
