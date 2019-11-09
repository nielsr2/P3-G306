import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage
from skimage import img_as_ubyte
from skimage import restoration
from M3 import m3F as m3F


def denoise_tv_chambolle(inputImg, weight, eps, n_iter_max, multichannel, show):

    # documentation: https://scikit-image.org/docs/dev/api/skimage.restoration.html#skimage.restoration.denoise_tv_chambolle

    tvImg = skimage.restoration.denoise_tv_chambolle(inputImg, weight=weight, eps=eps, n_iter_max=n_iter_max,
                                                     multichannel=multichannel)
    # standard params skimage.restoration.denoise_tv_chambolle(inputImg, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)
    # print(len(tvImg.shape))

    tvImg = img_as_ubyte(tvImg)
    if show:
        m3F.imshow(tvImg, "Total variation")

    return tvImg
