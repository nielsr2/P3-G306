import PIL
from matplotlib import pyplot as plt
import numpy as np
import os
import os.path
import cv2
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm,colors 




def imshow(inputImg, title):
    plt.title(title)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB))
    newInputImg=plt.show()
    return  inputImg


def scatter(inputImg):
    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)
    
    #Splits the image into three channel; rgb 
    r, g, b = cv2.split(newInputImg)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    #Normalizing pixels (0-1) and set it to it's true color 
    pixel_colors = newInputImg.reshape((np.shape(newInputImg)[0]*np.shape(newInputImg)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    
    #Plot it in x,y,z
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    scatterPlot=plt.show()
    
    return (inputImg)
 

def Histogram(inputImg):
    
    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)


    #load image and split the image into the color channels
    b, g, r = cv2.split(newInputImg)
    
    
    #Creates a histogram of the different channels
    plt.hist(b.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(r.ravel(), 256, [0, 256])
    BGR_Histogram =plt.show()
    
    return (inputImg)
 




def rgbToHSV(inputImg):
    
    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)

    
    hsv_pic = cv2.cvtColor(newInputImg, cv2.COLOR_RGB2HSV)
    
    #Splits into color channels and creates a 3D plot 
    h,s,v = cv2.split(hsv_pic)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")
    
    #Pixels colors and normalize 
    pixel_colors = newInputImg.reshape((np.shape(newInputImg)[0]*np.shape(newInputImg)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()
    
    #plots into H, S and V
    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")

    result = plt.show()
    
    return (inputImg)
    
def h_Pass(inputImage):
    
    laplacian = cv.Laplacian(img,cv.CV_64F)
    sobelx = cv.Sobel(img,cv.CV_64F,1,0,ksize=5)
    sobely = cv.Sobel(img,cv.CV_64F,0,1,ksize=5)
    
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    
    plt.show()
    
    return (inputImg)
 





   

