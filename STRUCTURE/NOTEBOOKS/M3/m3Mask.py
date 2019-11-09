
from M3 import m3Show
from M3 import m3Class
from M3 import m3F as m3F
import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")


def makeCircularMask(photo, show):
    for face in photo.faces:
        for eye in face.eyes:
            maskImg = eye.image.copy()
            maskImg.fill(0)
            if not isinstance(eye.circle, type(None)):
                # firstCircle = eye.circle[0]
                for i in eye.circle[0, :]:
                    print("i", i)
                    cv2.circle(maskImg, (i[0], i[1]), i[2], (255, 255, 255), -1)
                    eye.mask = maskImg
                    if (show):
                        m3Show.imshow(maskImg, "mask")
    return photo


def makeCircularOutline(photo, show):
    for face in photo.faces:
        for eye in face.eyes:
            maskImg = eye.image.copy()
            if not isinstance(eye.circle, type(None)):
                # firstCircle = eye.circle[0]
                for i in eye.circle[0, :]:
                    print("i", i)
                    cv2.circle(maskImg, (i[0], i[1]), i[2], (255, 255, 255), 2)
                    if (show):
                        m3Show.imshow(maskImg, "mask")
                        eye.mask = maskImg
    return photo

def fullImgEyeOutline(photo, show):

    fullMask = photo.orginalImage.copy()
    x, y, channels = fullMask.shape
    for face in photo.faces:
        for eye in face.eyes:
            if not isinstance(eye.mask, type(None)):
                coor = eye.coordinates
                # fullMask[coor[0]:x, coor[1]:y] = eye.mask

                for i in eye.circle[0, :]:
                    print("i", i)
                    cv2.circle(fullMask, (coor[0]+i[0], coor[1]+i[1]), i[2], (0, 255, 0), 2)

                    print("coor", coor)
                    #fullMask[coor[1]:coor[1]+eye.mask.shape[0], coor[0]:coor[0]+eye.mask.shape[1]] = eye.mask
                photo.mask = fullMask

    if (show):
        m3Show.imshow(photo.orginalImage, "full original")
        m3Show.imshow(fullMask, "full mask")

    return photo


def makeFullMask(photo, show):
    fullMask = photo.orginalImage.copy()
    fullMask.fill(0)

    # img1 = cv.imread('messi5.jpg')
    # img2 = cv.imread('opencv-logo-white.png')
    # I want to put logo on top-left corner, So I create a ROI
    x, y, channels = fullMask.shape
    for face in photo.faces:
        for eye in inputImg.eyes:
            if not isinstance(eye.mask, type(None)):
                coor = eye.coordinates
                # fullMask[coor[0]:x, coor[1]:y] = eye.mask
                print("coor", coor)
                fullMask[coor[1]:coor[1]+eye.mask.shape[0], coor[0]:coor[0]+eye.mask.shape[1]] = eye.mask
    photo.mask = fullMask
    if (show):
        m3Show.imshow(photo.orginalImage, "full original")
        m3Show.imshow(fullMask, "full mask")
    return photo


def makePolyMask(photo, show, apply=False):

    for eye in inputImg.eyes:
        polyMask = inputImg.orginalImage.copy()
        polyMask.fill(0)
        print("EYE COOR", eye.coordinates)
        polyMask = cv2.fillPoly(polyMask, np.int_([eye.landmarkPoints]), (255, 255, 255))
        # epm = m3Class.Eye(np.asarray(pil_image.crop(left)), left, lEyeCoor)
        # epm = polyMask.crop(eye.coordinates)

        eye.polyMask = m3F.typeSwap(m3F.typeSwap(polyMask).crop(eye.coordinates))
        if show:
            m3Show.imshow(eye.polyMask, "poly")
    return inputImg


def applyPolyMask(inputImg, show=True):
    for eye in inputImg.eyes:
        eye.image = cv2.bitwise_and(eye.image, eye.polyMask)
        if show:
            m3Show.imshow(eye.image, "masked")
    return inputImg
