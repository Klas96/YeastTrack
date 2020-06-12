import cv2

def getPositionFromContour(contour):
    moments = cv2.moments(contour)
    #TOOD Byt till funktioner ist??
    cx = int(moments['m10']/moments['m00'])
    cy = int(moments['m01']/moments['m00'])
    position = (cx,cy)
    return(position)
