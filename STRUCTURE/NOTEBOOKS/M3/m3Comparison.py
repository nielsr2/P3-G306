import cv2
import PIL
import numpy as np
from M3 import m3Show
#INPUTIMAGE 2 IS THE BASECASE - The handmask

# inputImg1 = cv2.imread("15.jpg_0hardedge.jpg",cv2.IMREAD_GRAYSCALE)
# inputImg2 = cv2.imread("15.jpg_0softedge.jpg",cv2.IMREAD_GRAYSCALE)
#
def batchcc(photoArray):
    for photo in photoArray:
        for face in photo.faces:
            for eye in face.eyes:
                ret, thresh1 = cv2.threshold(eye.iris,1,255,cv2.THRESH_BINARY)
                m3Show.imshow( eye.testMask, "MANMADE:")
                m3Show.imshow(thresh1, "thresh1:")
                compare(eye.testMask,thresh1)

def compare(machineMask,manMask):
    
    print (machineMask)
    print (manMask)
    
    inputImg1=cv2.cvtColor(machineMask, cv2.COLOR_BGR2GRAY)
    inputImg2=cv2.cvtColor(manMask, cv2.COLOR_BGR2GRAY)
    

    print (machineMask.shape)
    print (manMask.shape)


    
    rows1,cols1= inputImg1.shape
    count1 = 0
    for i in range(rows1):
        for j in range(cols1):
            count1 += inputImg1[i,j]

    count1 = count1/255       
    print(count1)

    rows2,cols2 = inputImg2.shape
    #Pixel-count
    cntPixels2 = rows2*cols2

    count2 = 0
    for i in range(rows2):
        for j in range(cols2):
            count2 += inputImg2[i,j]
    count2 = count2/255
    print(count2)
    
    deviatingValuedPixelPer = (abs(count1-count2)/count2)*100
    overlappingValuedPixelPer = 100-deviatingValuedPixelPer


  
    print ("Percentage overlapping of valued pixels from BASECASE",overlappingValuedPixelPer)