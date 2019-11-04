import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
from M3 import m3Class
import os
from PIL import ImageFilter, ImageEnhance
import PIL

# TODO - RENAME THEM FROM PARAMX TO SOOMETHINNG MEANINGFUL
def findCircle(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius, show):
    # old params for HoughCircle: img, cv2.HOUGH_GRADIENT, 1.5, 120, param1=60, param2=15, minRadius=0, maxRadius=int(m3F.typeSwap(img).height / 2))
    run(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius, show)


def findCircleSimple(inputImg, show):
    #run(inputImg, 1, 120, 60, 15, 10, 100, show)
    # print("inputImg type", type(inputImg))
    if isinstance(inputImg, type(m3Class.Eye())):
        run(inputImg, 1, 120, 200, 10, int(m3F.typeSwap(inputImg.image).height/6), int(m3F.typeSwap(inputImg.image).height/2.5), show)
    else:
        run(inputImg, 1, 120, 200, 10, int(m3F.typeSwap(inputImg).height/6), int(m3F.typeSwap(inputImg).height/2.5), show)


def findCircleDouble(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius, show):
    # old params for HoughCircle: img, cv2.HOUGH_GRADIENT, 1.5, 120, param1=60, param2=15, minRadius=0, maxRadius=int(m3F.typeSwap(img).height / 2))
    runDouble(inputImg, resolution, min_dist, param_1, param_2, min_radius, max_radius, show)


def run(tempInputImg, tempResolution, tempMin_dist, tempParam_1, tempParam_2, tempMinRadius, tempMaxRadius, tempShow):
    print("***************************************************************************************")

    img = tempInputImg
    print(tempMinRadius)
    isEyeClass = False
    eye = None
    if isinstance(img, type(m3Class.Eye())):
        isEyeClass = True
        eye = tempInputImg
        img = eye.image
    if not isinstance(img, type(None)):
        cimg = img

        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, tempResolution, tempMin_dist,
#                                   param1=tempParam_1, param2=tempParam_2, minRadius=tempMinRadius, maxRadius=tempMaxRadius)

        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=200,param2=10,
                                   minRadius=int(m3F.typeSwap(img).height/6),maxRadius=int(m3F.typeSwap(img).height/2.5))

        if not isinstance(circles, type(None)):

            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                # print(circles)
                for i in circles[0, :]:
                    if img[i[1],i[0]] < 15:
                        # draw the outer circle
                        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                        # draw the center of the circle
                        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
                    else:
                        # draw the outer circle
                        cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                        # draw the center of the circle
                        cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
            if (tempShow):
                m3F.imshow(cimg, "Circle")
                m3F.printGreen("CIRCLES FOUND^^^")
                print("img out", img.shape)
            if isEyeClass:
                eye.circle = circles
                print("RETURNED AN EYE WITH CIRCLES")
                return eye
            else:
                return img
        else:
            if (tempShow):
                m3F.imshow(cimg, "no circles found")
                m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("Image is NONE")


def runDouble(tempInputImg, tempResolution, tempMin_dist, tempParam_1, tempParam_2, tempMinRadius, tempMaxRadius, tempShow):
    print("***************************************************************************************")

    img = tempInputImg
    print(tempMinRadius)

    if not isinstance(img, type(None)):
        cimg = img
        if len(img.shape) == 3:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        bwimg = img.copy()

        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, tempResolution, tempMin_dist,
                                   param1=tempParam_1, param2=tempParam_2, minRadius=tempMinRadius, maxRadius=tempMaxRadius)

        if not isinstance(circles, type(None)):

            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                # print(circles)

                for i in circles[0, :]:
                    bwimg.fill(0)
                    # draw the outer circle
                    cv2.circle(bwimg, (i[0], i[1]), i[2], 255, -1)
                    # draw the center of the circle
                    # cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)
                    # m3F.imshow(bwimg,"circle")

                    mask = cv2.bitwise_and(img, bwimg)
                    # finalImg = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)

                    #m3F.imshow(mask, "final img")

                    pupilCircle = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, 3,
                                                   param1=60, param2=20, minRadius=5,
                                                   maxRadius=40)
                    if not isinstance(pupilCircle, type(None)):

                        if (pupilCircle.size != 0):
                            pupilCircle = np.uint16(np.around(pupilCircle))
                            # print(circles)
                            for j in pupilCircle[0, :]:
                                wiggle = 3
                                if i[0] + wiggle > j[0] > i[0] - wiggle and i[1] + wiggle > j[1] > i[1] - wiggle and i[2] > j[2]+10:
                                    # draw the outer circle
                                    cv2.circle(mask, (j[0], j[1]), j[2], (255, 255, 0), 0)
                                    # draw the center of the circle
                                    cv2.circle(mask, (j[0], j[1]), 2, (0, 0, 255), 1)
                                    m3F.imshow(mask, "final img")

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
