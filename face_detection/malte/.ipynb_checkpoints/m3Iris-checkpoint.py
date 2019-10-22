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
        img = cv2.imread(inputImg,0)
        print("proccesing", inputImg)
        #print("input was string (filepath), image read from filepath")
    else:
        #print("input was image", type(imgPath))
        img = inputImg
    count = 0
    if not isinstance(img, type(None)):

        #img  = cv2.medianBlur(img,5)
        
        #img = cv2.fastNlMeansDenoising(img, None, m3F.typeSwap(img).height*0.3, int(m3F.typeSwap(img).height*0.1))
        

        cimg=cv2.cvtColor(img,cv2.COLOR_GRAY2BGR )
        
        img = m3F.typeSwap(img)
        img = img.filter(ImageFilter.GaussianBlur(img.height/40))
        img = img.filter(ImageFilter.UnsharpMask(radius=2, percent=200, threshold=1))
        img = ImageEnhance.Contrast(img).enhance(1.4)
        #img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        #img = ImageEnhance.Sharpness(img).enhance(2)
    
        img = m3F.typeSwap(img)
        img = cv2.medianBlur(img,5)
        cimg=img.copy()
        
        can = cv2.Canny(img,200,10)
        
   
        #NoneType = type(None)

        #ret,thresh1 = cv2.threshold(greyImg,111,255,cv2.THRESH_BINARY)
        #thresh1 = cv2.medianBlur(thresh1,17)
        #cimg = cv2.cvtColor(thresh1,cv2.COLOR_GRAY2BGR)
        #plt.imshow(cimg)
        #plt.show()
        print("image height: ", int(m3F.typeSwap(img).height))
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=200,param2=10,minRadius=int(m3F.typeSwap(img).height/6),maxRadius=int(m3F.typeSwap(img).height/2.5))
        
        
        #print("type(circles) IS: ", type(circles))
        if not isinstance(circles, type(None)):
            #print("was not note None, was: ", type(circles))
            if (circles.size != 0):
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    print("circle:",i[0],i[1])
                    print("pixel:",cimg[i[1],i[0]])
                    if cimg[i[1],i[0]] < 15:
                        #print("pixel value", cimg(i[0],i[1])
                        # draw the outer circle
                        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),1)
                        # draw the center of the circle
                        #cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
                        #plt.show(cimg)
                        print("circle radius: ", i[2])
                        combined = np.hstack((cimg,can))
                        finalImg = cv2.cvtColor(combined, cv2.COLOR_BGR2RGB)
                        plt.imshow(finalImg)
                        plt.show()
                        m3F.gHist(img)
                        m3F.printGreen("CIRCLES FOUND^^^")
                        return cimg;
        else:
            can = cv2.Canny(img,50,30)
            combined = np.hstack((cimg,can))
            plt.imshow(combined)
            m3F.gHist(img)
            m3F.printRed("NO CIRCLES FOUND^^^")
    else:
        m3F.printRed("NONE IMAGE")



#plt.imshow(cimg)
#plt.show()