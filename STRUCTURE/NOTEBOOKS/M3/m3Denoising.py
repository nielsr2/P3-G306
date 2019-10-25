import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL


def denoise(inputImg):
    outputImg = cv2.fastNlMeansDenoisingColored(inputImg,7,21,20,10)
    return outputImg