
def printMotherDoghuther(trackedCells):
    for trackedCell in trackedCells:
        doughterID = trackedCell.getCellID()
        motgherID = trackedCell.getMotherCell()
        relatabelityFactor = trackedCell.getRelatabelityFactor()
        print("M: " + str(motgherID) + " --> " + "D: " + str(doughterID))
        print("RelFactor: " + str(relatabelityFactor))
