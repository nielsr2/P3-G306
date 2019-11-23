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
    plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB), interpolation='none')
    plt.show()
    # plt.axes
    return inputImg


def scatter(inputImg):
    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)

    # Splits the image into three channel; rgb
    r, g, b = cv2.split(newInputImg)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    # Normalizing pixels (0-1) and set it to it's true color
    pixel_colors = newInputImg.reshape((np.shape(newInputImg)[0]*np.shape(newInputImg)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    # Plot it in x,y,z
    axis.scatter(r.flatten(), g.flatten(), b.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Red")
    axis.set_ylabel("Green")
    axis.set_zlabel("Blue")
    scatterPlot=plt.show()

    return (inputImg)


def Histogram(inputImg):

    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)
    # load image and split the image into the color channels
    b, g, r = cv2.split(newInputImg)


    # Creates a histogram of the different channels
    plt.hist(b.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(r.ravel(), 256, [0, 256])
    BGR_Histogram =plt.show()

    return (inputImg)


def rgbToHSV(inputImg):

    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)

    hsv_pic = cv2.cvtColor(newInputImg, cv2.COLOR_RGB2HSV)

    # Splits into color channels and creates a 3D plot
    h,s,v = cv2.split(hsv_pic)
    fig = plt.figure()
    axis = fig.add_subplot(1, 1, 1, projection="3d")

    # Pixels colors and normalize
    pixel_colors = newInputImg.reshape((np.shape(newInputImg)[0]*np.shape(newInputImg)[1], 3))
    norm = colors.Normalize(vmin=-1.,vmax=1.)
    norm.autoscale(pixel_colors)
    pixel_colors = norm(pixel_colors).tolist()

    # plots into H, S and V
    axis.scatter(h.flatten(), s.flatten(), v.flatten(), facecolors=pixel_colors, marker=".")
    axis.set_xlabel("Hue")
    axis.set_ylabel("Saturation")
    axis.set_zlabel("Value")

    result = plt.show()

    return (inputImg)
<<<<<<< HEAD
    
def h_Pass(inputImg):
    
    #Converting img to grayscale
    

    inputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2GRAY)
    inputImg1 = cv2.GaussianBlur(inputImg,(5,5),0)
    
    #Adding lowpass laplacian_filter
    laplacian = cv2.Laplacian(inputImg1,cv2.CV_64F)
    #Adding lowpass sobelX_filter
    sobelx = cv2.Sobel(inputImg1,cv2.CV_64F,1,0,ksize=5)
    #Adding lowpass sobelY_filter
    sobely = cv2.Sobel(inputImg1,cv2.CV_64F,0,1,ksize=5)
    
    plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
    plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
    
    #plt.imshow((laplacian*255).astype(np.uint8))
    plt.show()

    return (inputImg)
=======
>>>>>>> 65f6e067f2782bb3e41ba6cb579a082cb7f375f0
 
def r_Channel (inputImg):
    
    img = inputImg
   

    b = img.copy()
    # set green and red channels to 0
    b[:, :, 1] = 0
    b[:, :, 2] = 0


    g = img.copy()
    # set blue and red channels to 0
    g[:, :, 0] = 0
    g[:, :, 2] = 0

    r = img.copy()
    # set blue and green channels to 0
    r[:, :, 0] = 0
    r[:, :, 1] = 0


    # RGB - Blue
    cv2.imshow('B-RGB', b)

    # RGB - Green
    cv2.imshow('G-RGB', g)

    # RGB - Red
    redImg= cv2.imshow('R-RGB', r)
    
    return (redImg)


def r_channel (inputImg):

    img = inputImg
    b,g,r = cv2.split(img)
    cv2.imshow('Blue Channel',b)
    cv2.imshow('Green Channel',g)
    cv2.imshow('Red Channel',r)
    img=cv2.merge((b,g,r))
    cv2.imshow('Merged Output',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return (inputImg)



