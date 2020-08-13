import numpy as np
import cv2
import pandas as pd
from scipy import ndimage as nd
import gc


def imagesToPrameter(optImgArr,floImgArr,maskImgArr = []):
    #Save Originals to DataFrame
    #img2 = img.reshape(-1)
    #print("loading Images")
    optImgReArr = []
    floImgReArr = []
    for imgIndex in range(len(optImgArr)):
        optImgReArr.append(optImgArr[imgIndex].reshape(-1))
        floImgReArr.append(floImgArr[imgIndex].reshape(-1))

    df = pd.DataFrame()
    #df['optImg'] = np.append(optImgReArr)
    df['optImg'] = np.concatenate(optImgReArr, axis=0)
    df['floImg'] = np.concatenate(floImgReArr, axis=0)
    del optImgReArr
    del floImgReArr
    gc.collect()

    #Add Filters To Model
    #print("loading Median Filter")
    #MEDIAN with sigma=3
    medC0Z3Arr = []
    medC1Z2Arr = []
    for imgIndex in range(len(optImgArr)):
        medC0Z3 = nd.median_filter(optImgArr[imgIndex], size=3)
        medC1Z2 = nd.median_filter(floImgArr[imgIndex], size=3)
        medC0Z3Arr.append(medC0Z3.reshape(-1))
        medC1Z2Arr.append(medC1Z2.reshape(-1))
    df['MedS3C0Z3'] = np.concatenate(medC0Z3Arr, axis=0)
    df['MedS3C1Z2'] = np.concatenate(medC1Z2Arr, axis=0)
    del medC0Z3Arr
    del medC1Z2Arr
    gc.collect()

    medC0Z3Arr = []
    medC1Z2Arr = []
    for imgIndex in range(len(optImgArr)):
        medC0Z3 = nd.median_filter(optImgArr[imgIndex], size=1)
        medC1Z2 = nd.median_filter(floImgArr[imgIndex], size=1)
        medC0Z3Arr.append(medC0Z3.reshape(-1))
        medC1Z2Arr.append(medC1Z2.reshape(-1))
    df['MedS1C0Z3'] = np.concatenate(medC0Z3Arr, axis=0)
    df['MedS1C1Z2'] = np.concatenate(medC1Z2Arr, axis=0)
    del medC0Z3Arr
    del medC1Z2Arr
    gc.collect()

    #print("loading Variance")
    #VARIANCE with size=3
    varC0Z3Arr = []
    varC1Z2Arr = []
    for imgIndex in range(len(optImgArr)):
        varC0Z3 = nd.generic_filter(optImgArr[imgIndex], np.var, size=3)
        varC1Z2 = nd.generic_filter(floImgArr[imgIndex], np.var, size=3)
        varC0Z3Arr.append(varC0Z3.reshape(-1))
        varC1Z2Arr.append(varC1Z2.reshape(-1))
    df['varS3C0Z3'] = np.concatenate(varC0Z3Arr, axis=0)
    df['varS3C1Z2'] = np.concatenate(varC1Z2Arr, axis=0)
    del varC0Z3Arr
    del varC1Z2Arr
    gc.collect()

    #VARIANCE with size=3
    varC0Z3Arr = []
    varC1Z2Arr = []
    for imgIndex in range(len(optImgArr)):
        varC0Z3 = nd.generic_filter(optImgArr[imgIndex], np.var, size=1)
        varC1Z2 = nd.generic_filter(floImgArr[imgIndex], np.var, size=1)
        varC0Z3Arr.append(varC0Z3.reshape(-1))
        varC1Z2Arr.append(varC1Z2.reshape(-1))
    df['varS1C0Z3'] = np.concatenate(varC0Z3Arr, axis=0)
    df['varS1C1Z2'] = np.concatenate(varC1Z2Arr, axis=0)
    del varC0Z3Arr
    del varC1Z2Arr
    gc.collect()

    #VARIANCE with size=3
    histEC0Z3Arr = []
    histEC1Z2Arr = []
    for imgIndex in range(len(optImgArr)):
        histEC0Z3 = cv2.equalizeHist(optImgArr[imgIndex])
        histEC1Z2 = cv2.equalizeHist(floImgArr[imgIndex])
        histEC0Z3Arr.append(histEC0Z3.reshape(-1))
        histEC1Z2Arr.append(histEC1Z2.reshape(-1))
    df['histES1C0Z3'] = np.concatenate(histEC0Z3Arr, axis=0)
    df['histES1C1Z2'] = np.concatenate(histEC1Z2Arr, axis=0)
    del histEC0Z3Arr
    del histEC1Z2Arr
    gc.collect()


    if maskImgArr != []:
        print("loading Labels")
        maskImgArrRe = []
        for maskImgIndex in range(len(maskImgArr)):
            maskImg = maskImgArr[maskImgIndex].reshape(-1)
            maskImgArrRe.append(maskImg)
        #print(maskIm)
        df['Labels'] = np.concatenate(maskImgArrRe, axis=0)
        del maskImgArrRe
        gc.collect()
        #print("writing to File")
        #df.to_csv('YeastCell/Train/modelTrain.csv', index=False)

    return(df)
