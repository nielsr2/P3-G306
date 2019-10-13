import cv2
import numpy as np
from matplotlib import pyplot as plt
import m3F
import os
def findCircle(imgPath):
    print("****************************************************************************************************************")
    print("proccesing", imgPath)

    img = cv2.imread(imgPath,0)
    count = 0
    if not isinstance(img, type(None)):

        img  = cv2.medianBlur(img,5)
        cimg=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR )

        
   
        #NoneType = type(None)

        #ret,thresh1 = cv2.threshold(greyImg,111,255,cv2.THRESH_BINARY)
        #thresh1 = cv2.medianBlur(thresh1,17)
        #cimg = cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
        #plt.imshow(cimg)
        #plt.show()
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)

        #print("type(circles) IS: ", type(circles))
        if not isinstance(circles, type(None)):
            #print("was not note None, was: ", type(circles))
            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    # draw the outer circle
                    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                    # draw the center of the circle
                    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
                    #plt.show(cimg)
                    plt.imshow(cimg)
                    plt.show()
                    m3F.gHist(img)
                    m3F.printGreen("CIRCLES FOUND^^^")
                    return cimg;
        else:

            plt.imshow(cimg)
            plt.show()
            m3F.gHist(img)
            m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("NONE IMAGE")



#plt.imshow(cimg)
#plt.show()