#Returnsfirst Whi5 activation Index
def getDevisionFrameNum(doughter):
    thresh = 0.30
    cellWhi5Trace = doughter.getWhi5Trace()
    index = 0
    for whi5 in cellWhi5Trace:
        index = index + 1
        if whi5 > thresh:
            index = index+doughter.getDetectionFrameNum()
        
    return(index)
