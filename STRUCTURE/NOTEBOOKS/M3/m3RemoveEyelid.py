import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL

def removeEyelid(eye, show):
    #m3F.imshow(eye.iris,"removeEyelid")
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(eye.iris)
    for i in eye.iris:
        if i is maxVal:
            i = 0
    m3F.imshow(eye.iris,"removed eyelid")