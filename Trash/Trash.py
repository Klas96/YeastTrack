def findDoughandAddBudToMother(mother,trackedCells):
    motherCellTrace = mother.getSizesTrace()
    daugthers = findDoughetCells(mother, trackedCells)
    for trCell in trackedCells:
        cellID = trCell.getCellID()
        if any(cellID == i for i in daugthers):
            motherCellTrace = addBudtoMother(mother,trCell)
    plt.show()
    return(motherCellTrace)


#Pre: frame with cells isolated in white
#Ret: KeyPoints for each cell.
def blobDetection(frame):
    # Setup SimpleBlobDetector parameters.
    params = cv2.SimpleBlobDetector_Params()

    #Filter by size
    params.filterByArea = True
    params.minArea = 2
    params.maxArea = 100000

    #Filter by color
    params.filterByColor = True;
    params.blobColor = 255;

    # Filter by Circularity
    #params.filterByCircularity = True
    #params.minCircularity = 0.1

    # Create a detector with the parameters
    ver = (cv2.__version__).split('.')
    if int(ver[0]) < 3 :
    	detector = cv2.SimpleBlobDetector(params)
    else :
    	detector = cv2.SimpleBlobDetector_create(params)

    # Detect blobs.
    keypoints = detector.detect(frame)

    return(keypoints)


def getTextFrame(keyPoints,sizeX,sizeY):

    #im2, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # create an empty black image
    classFrame = np.zeros((sizeX,sizeY, 3), np.uint8)

    #Font pararm
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.2
    color = (0, 255, 0)
    thickness = 1

    for keyP in keyPoints:
        (orgX,orgY) = keyP.pt
        orgX = int(orgX)
        orgY = int(orgY)
        size = keyP.size
        size = int(size)
        #write the size in frame
        # Using cv2.putText() method
        classFrame = cv2.putText(classFrame, str(size), (orgX,orgY), font, fontScale, color, thickness, cv2.LINE_AA)

    return(classFrame)
