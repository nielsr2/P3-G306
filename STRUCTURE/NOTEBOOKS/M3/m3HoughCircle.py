import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL

# TODO - RENAME THEM FROM PARAMX TO SOOMETHINNG MEANINGFUL
def findCircle(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius, show):
    # old params for HoughCircle: img, cv2.HOUGH_GRADIENT, 1.5, 120, param1=60, param2=15, minRadius=0, maxRadius=int(m3F.typeSwap(img).height / 2))
    run(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius)


def findCircleSimple(inputImg, show):
    run(inputImg, 1, 120, 60, 15, 10, 100, show)


def run(tempInputImg, tempResolution, tempMin_dist, tempParam_1, tempParam_2, tempMinRadius, tempMaxRadius, tempShow):
    print("***************************************************************************************")

    img = tempInputImg
    print(tempMinRadius)

    if not isinstance(img, type(None)):
        cimg = img
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, tempResolution, tempMin_dist,
                                   param1=tempParam_1, param2=tempParam_2, minRadius=tempMinRadius, maxRadius=tempMaxRadius)

        if not isinstance(circles, type(None)):

            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                # print(circles)
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # draw the center of the circle
                    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
                if (tempShow):
                    m3F.imshow(cimg, "Circle")
                    m3F.printGreen("CIRCLES FOUND^^^")
                    print("img out", img.shape)
                return img
        else:
            if (tempShow):
                m3F.imshow(cimg, "no circles found")
                m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("Image is NONE")
