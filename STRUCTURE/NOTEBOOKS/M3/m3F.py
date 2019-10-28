# __name__ = "__main__"

import PIL
from matplotlib import pyplot as plt
import numpy as np
import os
import os.path
import cv2

# http://ozzmaker.com/add-colour-to-text-in-python/


def printRed(stringarr):
    #prstr = ""
    # for el in stringarr:
    #    prstr + str(el)
    prstr = "\033[1;41;39m" + stringarr + "\]"
    print(prstr)


def printGreen(stringarr):
    prstr = "\033[1;42;39m" + stringarr + "\]"
    print(prstr)


def printBlue(stringarr):
    prstr = "\033[1;44;39m" + stringarr + "\]"
    print(prstr)


def evalSize(imagePath, w, h):
    im = PIL.Image.open(imagePath)
    # print("W & H", im.width, im.height)
    if (im.width > w and im.height > h):
        # was larger,
        return True
    else:
        # too small
        return False


# https://pythontic.com/image-processing/pillow/histogram
def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)


def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)


def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)


def gHist(imagePath):
    # print(type(imagePath))
    pimg = PIL.Image.fromarray(imagePath)
    hist = pimg.histogram()
    # plt.hist(hist,bins=256)
    plt.figure(0)
    for i in range(0, 256):
        plt.bar(i, hist[i], alpha=0.3)
    plt.show()

# swaps input between numpy ndArray (OPENCV USES) and PIL image
def typeSwap(inputIm):
    # printBlue("typeswap:")
    nd = np.ndarray(1)
    im = PIL.Image.Image()
    #print(type(inputIm), type(nd))
    if (type(inputIm) == type(nd)):
        inputIm = PIL.Image.fromarray(inputIm)
        return inputIm
    elif(type(inputIm) == type(im)):
        inputIm = np.asarray(inputIm)
        return inputIm


def filecount(dir_name):
    return len([f for f in os.listdir(dir_name)if os.path.isfile(os.path.join(dir_name, f))])


# shows image in notebook

def imshow(inputImg, title):
    plt.title(title)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB))
    plt.show()

def getRed(inputImg, show):

    (channel_b, channel_g, channel_r) = cv2.split(inputImg)
    if (show):
        imshow(channel_r,"red")
    return channel_r


