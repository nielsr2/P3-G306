import PIL
from matplotlib import pyplot as plt
import numpy as np
import os
import os.path
import cv2


def imshow(inputImg, title):
    plt.title(title)
    plt.axis("off")
    plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_BGR2RGB))
    plt.show()
    return inputImg