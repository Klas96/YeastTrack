import cv2

class cellInstance:

    def __init__(self,contour,whi5Activ = -1):

        self.whi5Activ = whi5Activ
        self.contour = contour

    def getPosition(self):
        moments = cv2.moments(self.contour)
        #TOOD Byt till funktioner ist??
        cx = int(moments['m10']/moments['m00'])
        cy = int(moments['m01']/moments['m00'])
        position = (cx,cy)
        return(position)

    def getSize(self):
        moments = cv2.moments(self.contour)
        size = moments['m00']
        return(size)

    def getWHI5Activity(self):
        return(self.whi5Activ)

    def getContour(self):
        return(self.contour)

    def setWhi5Activity(whi5Activ):
        self.whi5Activ = whi5Activ
