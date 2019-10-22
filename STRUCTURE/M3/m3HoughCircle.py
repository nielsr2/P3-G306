import cv2
import numpy as np
from matplotlib import pyplot as plt
import m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL


def findCircle(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius):
    # old params for HoughCircle: img, cv2.HOUGH_GRADIENT, 1.5, 120, param1=60, param2=15, minRadius=0, maxRadius=int(m3F.typeSwap(img).height / 2))
    __run(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius)


def findCircle(inputImg):
    __run(inputImg, 1.5, 120, param1=60, param2=15, minRadius=0, maxRadius=int(m3F.typeSwap(img).height / 2))


def __run(tempInputImg, tempResolution, tempMin_dist, tempParam_1, tempParam_2, tempMin_radius, tempMax_radius):
    print("***************************************************************************************")
    img = tempInputImg
    if not isinstance(img, type(None)):
        cimg = img
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, tempResolution, tempMin_dist, tempParam_1, tempParam_2,
                                   tempMin_radius, tempMax_radius)

        if not isinstance(circles, type(None)):

            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                # print(circles)
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # draw the center of the circle
                    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

                m3F.imshow(cimg, "Circle")
                m3F.printGreen("CIRCLES FOUND^^^")
                print("img out", img.shape)
                return img
        else:
            m3F.imshow(cimg, "no circles found")
            m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("Image is NONE")
