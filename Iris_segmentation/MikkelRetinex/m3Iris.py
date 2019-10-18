import cv2
import numpy as np
from matplotlib import pyplot as plt
import m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL


def findCircle(inputImg):
    print("***************************************************************************************")
    if (type(inputImg) == str):
        img = cv2.imread(inputImg, 0)
        print("proccesing", inputImg)
        # print("input was string (filepath), image read from filepath")
    else:
        # print("input was image", type(imgPath))
        img = inputImg
    count = 0
    if not isinstance(img, type(None)):
        uImg = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        plt.title("unprocessed")
        plt.imshow(uImg)
        plt.show()

        print(img.shape)
        img = cv2.medianBlur(img, 5)
        cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        # 1



        circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

        if not isinstance(circles, type(None)):
            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                # print(circles)
                for i in circles[0, :]:
                    # draw the outer circle
                    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    # draw the center of the circle
                    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

                    #can = cv2.Canny(img, 30, 60)
                    #combined = np.hstack((cimg, can))
                    plt.imshow(cimg)
                    plt.show()
                    m3F.printGreen("CIRCLES FOUND^^^")
                    return cimg;
        else:
            can = cv2.Canny(img, 50, 30)
            combined = np.hstack((cimg, can))
            plt.imshow(combined)
            m3F.gHist(img)
            m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("NONE IMAGE")

# plt.imshow(cimg)
# plt.show()
