import PIL
from matplotlib import pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
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


def Histogram(inputImg, passThru=True):

    newInputImg = cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB)
    # load image and split the image into the color channels
    b, g, r = cv2.split(newInputImg)


    # Creates a histogram of the different channels
    # fig = plt.figure()
    plt.hist(b.ravel(), 256, [0, 256])
    plt.hist(g.ravel(), 256, [0, 256])
    plt.hist(r.ravel(), 256, [0, 256])

    if passThru:
        BGR_Histogram =plt.show()
        return (inputImg)
    else:
        fig, axs = plt.subplots()
        # fig = Figure()
        canvas = FigureCanvas(fig)
        axs.hist(b.ravel(), 256, [0, 256])
        axs.hist(g.ravel(), 256, [0, 256])
        axs.hist(r.ravel(), 256, [0, 256])
        axs.axis('off')
        fig.tight_layout(pad=0)

        # fig.add_axes(plt.hist(b.ravel(), 256, [0, 256]))
        # fig.add_a(plt.hist(g.ravel(), 256, [0, 256]))
        # fig.add_a(plt.hist(r.ravel(), 256, [0, 256]))
        # width, height = fig.get_size_inches(fig) * fig.get_dpi()
        # foo = canvas.get_width_height()[::-1] + (3,)

        canvas = FigureCanvas(fig)
        foo = canvas.get_width_height()[::-1] + (3,)
        print("foo", foo)
        canvas.draw()       # draw the canvas, cache the renderer
        s, (width, height) = canvas.print_to_buffer()

        # return np.fromstring(canvas.tostring_rgb(), dtype='uint8').reshape(height, width, 3)
        # img = np.fromstring(canvas.to_string_rgb(), dtype='uint8')
        # img.reshape(height, width, 3)
        s = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
        print("stype:", type(s), s.shape)
        imshow(s, "hist")
        s = s.reshape(foo)
        imshow(s, "hist")
        #[::-1] + (3,))
        print("stype:", type(s), s.shape)
        return s


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
