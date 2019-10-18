import cv2 
from matplotlib import pyplot as plt
import m3F
import numpy as np

import json

import retinex

    
def runMSRCP(imgPath):
    with open('config.json', 'r') as f:
        config = json.load(f)

    img = cv2.imread(imgPath,1)

    shape = img.shape
    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']
    )

    m3F.imshow(img_msrcp,"MSRCP")
    return img_msrcp
    