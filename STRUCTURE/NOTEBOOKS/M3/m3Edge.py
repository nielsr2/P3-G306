import cv2
from M3 import m3Show


def sobel(inputImg, show=True):
    out = cv2.Sobel(inputImg, inputImg.depth(), 0, 1, 3)
    if show:
        m3Show.imshow(out, "show")
