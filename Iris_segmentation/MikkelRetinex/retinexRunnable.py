import cv2 
from matplotlib import pyplot as plt
import numpy as np

import json

import retinex

    
def runMSRCP(imgPath):
    with open('config.json', 'r') as f:
        config = json.load(f)

    img = cv2.imread(imgPath,1)
    print("img after reading", img.shape)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #shape = img.shape
    img_msrcp = retinex.MSRCP(
        img,
        config['sigma_list'],
        config['low_clip'],
        config['high_clip']
    )
    
    

    print("img_msrcp", img_msrcp.shape)
    #img_msrcp=cv2.cvtColor(img_msrcp,cv2.COLOR_BGR2RGB)
    plt.title("MSRCP")
    plt.imshow(img_msrcp)
    plt.show()
    return img_msrcp
    