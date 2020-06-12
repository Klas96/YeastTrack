
#TODO Make this the control class
def controls():
    #List With comand chars and coresponding function
    listOfComandsChars = ["q", "s", "o", "i", "w", "l","p"]
    listOfComandsFunctions = ["quit", "Show Segmentation", "show Opt Chan", "show cell ID", "show WHI5 Activ Threshold", "Print Lineage","Plot Data"]
    while(True):
        print("Options:")
        for i in range(0,len(listOfComandsChars)):
            print(listOfComandsChars[i] + " = " + listOfComandsFunctions[i])

        key = cv2.waitKey(0)
        #input = str(input())
        print("Your input: " + chr(key))
        if(key == ord('q')):
            break
        if(key == ord('s')):
            showMaskImg = not showMaskImg
            print("showMaskImage is now " + str(showMaskImg))
            updateFrame()
        if(key == ord("o")):
            showOptImg = not showOptImg
            print("showOptImage is now " + str(showOptImg))
            updateFrame()
        if(key == ord("i")):
            showCellID = not showCellID
            print("showCellID is now " + str(showCellID))
            updateFrame()
        if(key == ord("w")):
            showWHI5ActivImg = not showWHI5ActivImg
            print("showWHI5ActivFrame is now " + str(showWHI5ActivImg))
            updateFrame()
        if(key == ord("l")):
            trackedCells = video.getTrackedCells()
            printMotherDoghuther(trackedCells)
            PlotLinageTree(trackedCells)
        if(key == ord("p")):
            trackedCells = video.getTrackedCells()
            plotFunction(video.getTrackedCells())
