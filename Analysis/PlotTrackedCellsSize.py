from matplotlib import pyplot as plt
from Anlysis.getDevisionFrameNum import getDevisionFrameNum
def plotTrackedCellsSize(trackedCells):
    for trCell in trackedCells:
        deviNum = getDevisionFrameNum(trCell)
        trace = trCell.getSizesTraceFromBegining()[0:deviNum]
        plt.plot(range(len(trace)),trace)
