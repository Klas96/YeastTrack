from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np
from Segmentation.cellInstance import  cellInstance
from Tracking.TrackedCell import TrackedCell
#vaiabels
#objects
#disappeared
#maxDisappeared
class CentroidTracker():
    #Constructor
	def __init__(self, maxDisappeared=50):
		# initialize the next unique object ID along with two ordered
		# dictionaries used to keep track of mapping a given object
		# ID to its centroid and number of consecutive frames it has
		# been marked as "disappeared", respectively
		self.nextObjectID = 0
		self.cellObjects = OrderedDict()
		self.disappeared = OrderedDict()
		self.frameNumber = 0

		#MAx disappeared before deleting
		self.maxDisappeared = maxDisappeared

	#Stors the centroid in next availibal ObjectID
	#pre1: centroid
	#pre2: size
	def register(self, cellInstans, frameNum = -1):
		#Register in nex availibal object
		#self.objects[self.nextObjectID] = centroid
		self.cellObjects[self.nextObjectID] = TrackedCell(cellInstans,self.nextObjectID,frameNum)
		self.disappeared[self.nextObjectID] = 0
		self.nextObjectID += 1

	#Del object from object list and disappeared list
	#pre: objectID
	def deregister(self, objectID):
		#del self.objects[objectID]
		del self.cellObjects[objectID]
		del self.disappeared[objectID]

	def updateCellInst(self, cellInstances):

		#Is empty
		if len(cellInstances) == 0:
			#Mark all as disappeared
			for objectID in list(self.disappeared.keys()):
				self.disappeared[objectID] += 1

				#If the object have been gone for long enough delet
				if self.disappeared[objectID] > self.maxDisappeared:
					self.deregister(objectID)


			return(list(self.cellObjects.values()))

		#If no tracked object. Frst objects track all
		if len(self.cellObjects) == 0:
			for i in range(0, len(cellInstances)):
				self.register(cellInstances[i],self.frameNumber)


		inputCentroids = np.zeros((len(cellInstances), 2), dtype="int")

		for i in range(0,len(cellInstances)):
			inputCentroids[i] = cellInstances[i].getPosition()

		#Try matching to current centroids
		else:
			#Grab the set of object IDs and corresponding centroids
			#objectIDs = list(self.objects.keys())
			cellObjectIDs = list(self.cellObjects.keys())

			#objectCentroids = list(self.objects.values())

			#List of trackdedCell Objects
			cellObjectList = list(self.cellObjects.values())
			cellObjectsCentroids = list()

			#Makeing centroid list
			for cellObj in cellObjectList:
				cellObjectsCentroids.append(cellObj.getCentroid())

			#Compute the distance between each pair of object
			cellD = dist.cdist(np.array(cellObjectsCentroids), inputCentroids)

			#Find the smallest value in each row and then
			#Sort the rows so the row with smalest value is on top.
			cellRows = cellD.min(axis=1).argsort()

			#Finding smalest value in each colom
			#sorting using the previously computed row index list
			cellCols = cellD.argmin(axis=1)[cellRows]

			#Keeping track of used Rows and used coloms
			usedRows = set()
			usedCols = set()

			for (row, col) in zip(cellRows, cellCols):

				#Ignore examined rows or colums
				if row in usedRows or col in usedCols:
					continue


				#set its new centroid, and reset the disappeared counter
				objectID = cellObjectIDs[row]
				self.cellObjects[objectID].update(cellInstances[col])
				self.disappeared[objectID] = 0

				#Indicate that we have examined each of the row and
				#Column indexes, respectively
				usedRows.add(row)
				usedCols.add(col)

			#Compute both the row and column index we have NOT yet examined
			unusedRows = set(range(0, cellD.shape[0])).difference(usedRows)
			unusedCols = set(range(0, cellD.shape[1])).difference(usedCols)

			#in the event that the number of object centroids is
			#equal or greater than the number of input centroids
			#we need to check and see if some of these objects have
			#potentially disappeared
			if cellD.shape[0] > cellD.shape[1]:
				#loop over the unused row indexes
				for row in unusedRows:
					#grab the object ID for the corresponding row
					#index and increment the disappeared counter
					objectID = cellObjectIDs[row]
					self.disappeared[objectID] += 1

					#check to see if the number of consecutive
					#frames the object has been marked "disappeared"
					#for warrants deregistering the object
					if self.disappeared[objectID] > self.maxDisappeared:
						self.deregister(objectID)

			# otherwise, if the number of input centroids is greater
			# than the number of existing object centroids we need to
			# register each new input centroid as a trackable object
			else:
				for col in unusedCols:
					self.register(cellInstances[col],self.frameNumber)

		#Update all cells in Disaperd list
		#for disi in self.disappeared:
		for objectID in list(self.disappeared.keys()):
			#self.cellObjects[objectID].update()
			pass


		#frame number increases with one
		self.frameNumber = self.frameNumber + 1
		return(list(self.cellObjects.values()))
