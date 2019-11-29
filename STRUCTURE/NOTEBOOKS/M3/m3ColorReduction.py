import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL
from sklearn.cluster import MiniBatchKMeans
import argparse



def colorReduction(inputImg, show):
    

    compactness, labels, centers = cv2.kmeans(samples,
                                        NCLUSTERS, 
                                        None,
                                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
                                        NROUNDS, 
                                        cv2.KMEANS_PP_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    image2 = res.reshape((inputImg.shape))
    
    

    if (show):
        cv2.imshow("KMEANS", image2)
        
    return image2