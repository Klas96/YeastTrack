import cv2
from Anlysis.plotFunctions import plotFunction
from Anlysis.VisulizeLinage import PlotLinageTree
from Anlysis.PrintMotherDoughter import printMotherDoghuther
from UserInterface.UpdateFrame import updateFrame


#TODO Make this the control class With method update
class Controls:

    def __init__(self,video):
        self.video = video
        self.currentFrame = 1
        self.currentBlend = 0
        self.showMaskImg = False
        self.showCellID = True
        self.showLinagesTree = True
        self.showOptImg = True
        self.showWHI5ActivImg = False

        cv2.namedWindow('CellTracker')
        numFrames = video.getNumFrmes()
        cv2.createTrackbar("Frame",'CellTracker',self.currentFrame,numFrames-1,self.changeFrame)
        cv2.createTrackbar("Channel",'CellTracker',0,100,self.changeChanell)


    def startControls(self):
        self.updateFrame()
        #List With comand chars and coresponding function
        listOfComandsChars = ["q", "s", "o", "i", "w", "l","p"]
        listOfComandsFunctions = ["quit", "Show Segmentation", "show Opt Chan", "show cell ID", "show WHI5 Activ Threshold", "Print Lineage","Plot Data"]
        while(True):
            #global showMaskImg,showCellID,showLinagesTree,showOptImg,showWHI5ActivImg
            print("Options:")
            for i in range(0,len(listOfComandsChars)):
                print(listOfComandsChars[i] + " = " + listOfComandsFunctions[i])

            key = cv2.waitKey(0)
            #input = str(input())
            print("Your input: " + chr(key))
            if(key == ord('q')):
                break
            if(key == ord('s')):
                self.showMaskImg = not self.showMaskImg
                print("showMaskImage is now " + str(self.showMaskImg))
                #updateFrame(video)
            if(key == ord("o")):
                self.showOptImg = not self.showOptImg
                print("showOptImage is now " + str(self.showOptImg))
                #updateFrame(video)
            if(key == ord("i")):
                self.showCellID = not self.showCellID
                print("showCellID is now " + str(self.showCellID))
                #updateFrame(video)
            if(key == ord("w")):
                self.showWHI5ActivImg = not self.showWHI5ActivImg
                print("showWHI5ActivFrame is now " + str(self.showWHI5ActivImg))
                #updateFrame(video)
            if(key == ord("l")):
                trackedCells = self.video.getTrackedCells()
                printMotherDoghuther(trackedCells)
                PlotLinageTree(trackedCells)
            if(key == ord("p")):
                trackedCells = self.video.getTrackedCells()
                plotFunction(trackedCells)

            self.updateFrame()

    def updateFrame(self):
        param = [self.currentFrame,self.currentBlend,self.showMaskImg,self.showCellID,self.showLinagesTree,self.showOptImg,self.showWHI5ActivImg]
        updateFrame(self.video,param)

    def changeFrame(self,frameNum):
        self.currentFrame = frameNum
        self.updateFrame()

    #Change Between Florecent And Video Channel
    def changeChanell(self,division):
        self.currentBlend = division
        self.updateFrame()
