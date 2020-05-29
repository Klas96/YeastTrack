import cv2
import numpy as np
from getMaskFrame import getMaskFrame

#pre: image with white bloobs maskFrame
#ret List of key ppoints
#TODO: optimize Paramters
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

    # Draw detected blobs as red circles.
    # cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
    im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    return(keypoints)

#Pre: frameVideo
#Ret1: Mask For all cells
#Ret2: Array with keypoints for all cells
def detectCells(frame):
    #Theresholding
    #mask = otsuThreshold(frame)
    #making Convex hull
    #mask = convexHull(mask)
    maskFrame = getMaskFrame(frame)

    #filter none cells by roundness and size
    keypoints = blobDetection(maskFrame)
    #create classification frame
    #classFrame = getClassFrame(maskFrame,keypoints)

    return(keypoints)



img = cv2.imread('/home/klas/Documents/Chalmers/ExamensArbete/YeastTrack/ImageData/VidEamp.png')
detectCells(img)
