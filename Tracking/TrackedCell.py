import numpy as np
from Segmentation.cellInstance import cellInstance

class TrackedCell():

	def __init__(self, cellInst = -1, cellID = -1,detectionFrameNum = -1):
		self.cellTrace = []
		self.cellTrace.append(cellInst)
		self.cellID = cellID
		self.detectionFrameNum = detectionFrameNum
		self.motherID = None
		self.relatabelityFactor = 0

	def update(self ,cellInst = -1):
			if(cellInst == -1):
				cellInst = self.cellTrace[-1]
				self.cellTrace.append(cellInst)
			self.cellTrace.append(cellInst)

	def setMotherCell(self,motherID,relatabelityFactor = -1):
		self.motherID = motherID
		self.relatabelityFactor = relatabelityFactor

	def getMotherCell(self):
		return(self.motherID)

	def getRelatabelityFactor(self):
		return(self.relatabelityFactor)

	def getDetectionFrameNum(self):
		return(self.detectionFrameNum)

	def getContour(self,pos = -1):
		if(pos > 0 and pos > self.detectionFrameNum):
			pos = pos - self.detectionFrameNum

		#If pos < detectionFrameNum here means want pos before cell was detected give first instance
		if(pos < self.detectionFrameNum and pos > 0):
			#return Early
			return(self.cellTrace[0].getContour())

		#If pos >= len(cellTrace) want position of cell after it have disaperd
		if(pos >= len(self.cellTrace)):
			#Return earlt latest instace
			return(self.cellTrace[-1].getContour())

		return(self.cellTrace[pos].getContour())

	def getCellID(self):
		return(self.cellID)

	#Ret No Arg: latest registered poistion
    #Ret Arg: position at that frame number
	def getCentroid(self, pos = -1):
		if(pos > 0 and pos > self.detectionFrameNum):
			pos = pos - self.detectionFrameNum

		#If pos < detectionFrameNum here means want pos before cell was detected give first instance
		if(pos < self.detectionFrameNum and pos > 0):
			#return Early
			return(self.cellTrace[0].getPosition())

		#If pos >= len(cellTrace) want position of cell after it have disaperd
		if(pos >= len(self.cellTrace)):
			#Return earlt latest instace
			return(self.cellTrace[-1].getPosition())

		return(self.cellTrace[pos].getPosition())

	def getSizesTrace(self):
		sizeTrace = []
		for cellInst in self.cellTrace:
			sizeTrace.append(cellInst.getSize())
		return(sizeTrace)

	def getSizesTraceFromBegining(self):
		sizeTrace = []
		for i in range(self.detectionFrameNum):
			sizeTrace.append(0)
		for cellInst in self.cellTrace:
			sizeTrace.append(cellInst.getSize())
		return(sizeTrace)

	def getWhi5Trace(self):

		whi5Trace = []

		for cellInst in self.cellTrace:
			whi5Trace.append(cellInst.getWHI5Activity())

		return(whi5Trace)

	def getPosTrace(self):

		xPosTrace = []
		yPosTrace = []
		for cellInst in self.cellTrace:
			(xPos, yPos) = cellInst.getPosition()
			xPosTrace.append(xPos)
			yPosTrace.append(yPos)

		return(xPosTrace,yPosTrace)
