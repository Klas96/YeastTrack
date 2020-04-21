# import the necessary packages
from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np


class TrackedCell():
	#self.sizesTrace = []
	#self.whi5ActivTrace = []
	def __init__(self, centroid, size = -1, whi5Activ = -1):
		self.positionsTrace = []
		self.sizesTrace = []
		self.whi5ActivTrace = []
		self.positionsTrace.append(centroid)
		self.sizesTrace.append(size)
		self.whi5ActivTrace.append(whi5Activ)

	def update(self ,centroid,size = -1, whi5Activ = -1):
			self.positionsTrace.append(centroid)
			self.sizesTrace.append(size)
			self.whi5ActivTrace.append(whi5Activ)

	#Ret: latest registered poistion
	def getCentroid(self):
		return(self.positionsTrace[-1])

	def getSizesTrace(self):
		return(self.sizesTrace)

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
		#self.objects = OrderedDict()
		self.cellObjects = OrderedDict()
		self.disappeared = OrderedDict()

		#MAx disappeared before deleting
		self.maxDisappeared = maxDisappeared

    #Stors the centroid in nex availibal ObjectID
    #pre1: centroid
	#pre2: size
	def register(self, centroid,size = -1):
		#Register in nex availibal object
		#self.objects[self.nextObjectID] = centroid
		self.cellObjects[self.nextObjectID] = TrackedCell(centroid)
		self.disappeared[self.nextObjectID] = 0
		self.nextObjectID += 1

    #Dleats object from object list and disappeared list
    #pre: objectID
	def deregister(self, objectID):
		# to deregister an object ID we delete the object ID from
		# both of our respective dictionaries
		#del self.objects[objectID]
		del self.cellObjects[objectID]
		del self.disappeared[objectID]


	def updateCellInst(cellInstances):

		#Is empty
		if len(cellInstances) == 0:
			#Mark all as disappeared
			for objectID in list(self.disappeared.keys()):
				self.disappeared[objectID] += 1

				# if we have reached a maximum number of consecutive
				# frames where a given object has been marked as
				# missing, deregister it
				if self.disappeared[objectID] > self.maxDisappeared:
					self.deregister(objectID)


			return self.cellObjects

		#If no tracked object. Frst objects track all
		if len(self.cellObjects) == 0:
			for i in range(0, len(inputCentroids)):
				self.register(inputCentroids[i],sizes[i])



    #Run at each frame
    #pre: list of points sizes TODO WI5Activity
	#ret: List of objects
	def update(self, points, sizes = -1, cellInstances = -1):

		# is empty
		if len(points) == 0:
			# loop over any existing tracked objects and mark them
			# as disappeared
			for objectID in list(self.disappeared.keys()):
				self.disappeared[objectID] += 1

				# if we have reached a maximum number of consecutive
				# frames where a given object has been marked as
				# missing, deregister it
				if self.disappeared[objectID] > self.maxDisappeared:
					self.deregister(objectID)

			# return early as there are no centroids or tracking info
			# to update
			return self.cellObjects

		inputCentroids = np.zeros((len(points), 2), dtype="int")

		#Dont need??
		for (i, (pointX, pointY)) in enumerate(points):
			# use the bounding box coordinates to derive the centroid
			cX = int(pointX)
			cY = int(pointY)
			inputCentroids[i] = (cX, cY)

		#If no tracked object first object track all
		if len(self.cellObjects) == 0:
			for i in range(0, len(inputCentroids)):
				self.register(inputCentroids[i],sizes[i])

		#Try matching to current centroids
		else:
			#Grab the set of object IDs and corresponding centroids
			#objectIDs = list(self.objects.keys())
			cellObjectIDs = list(self.cellObjects.keys())

			#objectCentroids = list(self.objects.values())

			#lsit of points
			cellObjectList = list(self.cellObjects.values())
			cellObjectsCentroids = list()

			#MAkeing centroid list
			for cellObj in cellObjectList:
				cellObjectsCentroids.append(cellObj.getCentroid())

			#Compute the distance between each pair of object
			#D = dist.cdist(np.array(objectCentroids), inputCentroids)
			cellD = dist.cdist(np.array(cellObjectsCentroids), inputCentroids)

			# in order to perform this matching we must (1) find the
			# smallest value in each row and then (2) sort the row
			# indexes based on their minimum values so that the row
			# with the smallest value as at the *front* of the index
			# list
			#rows = D.min(axis=1).argsort()
			cellRows = cellD.min(axis=1).argsort()

			# next, we perform a similar process on the columns by
			# finding the smallest value in each column and then
			# sorting using the previously computed row index list
			#cols = D.argmin(axis=1)[rows]
			cellCols = cellD.argmin(axis=1)[cellRows]

			# in order to determine if we need to update, register,
			# or deregister an object we need to keep track of which
			# of the rows and column indexes we have already examined
			usedRows = set()
			usedCols = set()

			for (row, col) in zip(cellRows, cellCols):

				#Ignore examined rows or colums
				if row in usedRows or col in usedCols:
					continue


				# set its new centroid, and reset the disappeared
				# counter
				objectID = cellObjectIDs[row]
				self.cellObjects[objectID].update(inputCentroids[col],sizes[col])
				self.disappeared[objectID] = 0

				# indicate that we have examined each of the row and
				# column indexes, respectively
				usedRows.add(row)
				usedCols.add(col)

			# compute both the row and column index we have NOT yet
			# examined
			unusedRows = set(range(0, cellD.shape[0])).difference(usedRows)
			unusedCols = set(range(0, cellD.shape[1])).difference(usedCols)

			#in the event that the number of object centroids is
			#equal or greater than the number of input centroids
			#we need to check and see if some of these objects have
			#potentially disappeared
			if cellD.shape[0] >= cellD.shape[1]:
				# loop over the unused row indexes
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
					self.register(inputCentroids[col],sizes[col])

		return self.cellObjects
