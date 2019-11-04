
from M3 import m3Show
from M3 import m3Class
from M3 import m3F as m3F
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")


def makeCircularMask(inputImg, show):
    eye = inputImg
    maskImg = eye.image.copy()
    maskImg.fill(0)
    if not isinstance(eye.circle, type(None)):
        # firstCircle = eye.circle[0]
        for i in eye.circle[0, :]:
            print("i", i)
            cv2.circle(maskImg, (i[0], i[1]), i[2], (255, 255, 255), -1)
            if (show):
                m3Show.imshow(maskImg, "mask")
        eye.mask = maskImg
    return eye


def makeFullMask(inputImg, show):
    fullMask = inputImg.orginalImage.copy()
    fullMask.fill(0)
    # img1 = cv.imread('messi5.jpg')
    # img2 = cv.imread('opencv-logo-white.png')
    # I want to put logo on top-left corner, So I create a ROI
    x, y, channels = fullMask.shape
    for eye in inputImg.eyes:
        if not isinstance(eye.mask, type(None)):
            coor = eye.coordinates
            # fullMask[coor[0]:x, coor[1]:y] = eye.mask
            print("coor", coor)
            fullMask[coor[1]:coor[1]+eye.mask.shape[0], coor[0]:coor[0]+eye.mask.shape[1]] = eye.mask
    inputImg.mask = fullMask
    if (show):
        m3Show.imshow(inputImg.orginalImage, "full original")
        m3Show.imshow(fullMask, "full mask")
    return inputImg


def makePolyMask(inputImg, show, apply=False):
    print("lalala")
    polyMask = inputImg.orginalImage.copy()
    polyMask.fill(0)
    for eye in inputImg.eyes:
        polyMask = cv2.fillPoly(polyMask, np.int_([eye.landmarkPoints]), (255, 255, 255))
        eye.polyMask = polyMask
        if show:
            m3Show.imshow(polyMask, "poly")
        if apply:
            print("lalla")
            # masked = cv2..bitwise_and(img, mask)
        return inputImg


# def applyMask(inputImg, )
