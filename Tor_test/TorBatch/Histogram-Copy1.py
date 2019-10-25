
import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys


def Histogram(img):
    colors = ('b','g','r')
    img_1 = img 
    
  

    # read original image, in full color, based on command
    # line argument
    image = cv2.imread(img_1)

    # display the image 
    cv2.namedWindow(winname = 'img', flags = cv2.WINDOW_NORMAL)
    cv2.imshow(winname = 'img', mat = image)
    cv2.waitKey(delay = 0)


    # split into channels
    channels = cv2.split(image)

    
    #for i,col in enumerate(color):
       # hist = cv2.calcHist([img_1],[i],None,[256],[0,256])
       # plt.plot(hist,color = col)
       # plt.xlim([0,256])
        
    
    
    #something =plt.hist(img.ravel(),256,[0,256]); plt.show()

    
    #something_else, something =get_the_entire_name(); plt.show
    
    # tuple to select colors of each channel line
    colors = ("b", "g", "r") 
    plt.xlim([0, 256])
    for(channel, c) in zip(channels, colors):
        histogram = cv2.calcHist(
            images = [channel], 
            channels = [0], 
            mask = None, 
            histSize = [256], 
            ranges = [0, 256])

    something =plt.plot(histogram, color = c)

    plt.xlabel("Color value")
    plt.ylabel("Pixels")

    plt.show()
    
    return(something)

  
    #return (something)
    
    
    
 




   

