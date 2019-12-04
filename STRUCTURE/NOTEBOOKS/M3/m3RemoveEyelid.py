import cv2, sys
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
import os
from PIL import ImageFilter, ImageEnhance
import PIL
import math

def removeEyelid(inputImg, show):
    #m3F.imshow(eye.iris,"removeEyelid")
    eye = inputImg.photo.face.eye
    gray = cv2.cvtColor(eye.iris, cv2.COLOR_BGR2GRAY)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
    print("maxVal", maxVal)
    print("minVal", minVal)
    
    height,width = gray.shape
    
    grayPil = m3F.typeSwap(gray)
    
    
    for i in eye.circle[0, :]:
        for y in range(width-1):
            for x in range(height-1):
                pixel = grayPil.getpixel((y,x))
                #print("pixel",pixel)
                if math.sqrt(((y-i[0])**2)+((x-i[1])**2)) < i[2]:
                    if pixel != maxVal or math.sqrt(((y-i[0])**2)+((x-i[1])**2)) < i[2]/2:
                        gray[x,y] = 255
                    
                    else:
                        #print("done here")
                        #gray.putpixel((x,y),minVal)
                        gray[x,y] = 0
                
    #gray = m3F.typeSwap(gray)            
    
    m3F.imshow(gray,"iris blob")
    
    kernel1 = np.ones((3, 3), np.uint8)
    kernel2 = np.ones((15, 15), np.uint8)
    closing1 = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel2)
    closing2 = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel1)
    
    m3F.imshow(closing1,"closed. Kernel 15")
    m3F.imshow(closing2,"closed. Kernel 3")
    return closing1