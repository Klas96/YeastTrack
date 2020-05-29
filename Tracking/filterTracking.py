#Pre: List of trackedCells
#Ret: Filterd list with trackedCells
def filterTrackedCells(trackedCells):

    trackedCells = filterByOpserLen(trackedCells)
    trackedCells = filterByMeanSize(trackedCells)
    return(trackedCells)


def filterByOpserLen(trackedCells):
    filterdList = []
    #Filter by observation length
    observationThreshold = 10
    for tracked in trackedCells:
        exsistingLength = len(tracked.getSizesTrace())
        if exsistingLength > observationThreshold:
            filterdList.append(tracked)
    return(filterdList)

def filterByMeanSize(trackedCells):
    filterdList = []
    #Filter by mean size
    cellSize = 4500
    cellThreshold = 0.2*cellSize
    for tracked in trackedCells:
        meanSizeCell = sum(tracked.getSizesTrace())/len(tracked.getSizesTrace())
        if  meanSizeCell > cellThreshold:
            filterdList.append(tracked)

    return(filterdList)
