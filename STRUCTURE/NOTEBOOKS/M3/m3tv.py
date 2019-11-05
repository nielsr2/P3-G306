import numpy as np
import matplotlib.pyplot as plt
import cv2
import skimage
from skimage import restoration
from M3 import m3F as m3F



def denoise_tv_chambolle(inputImg,weight,eps,n_iter_max,multichannel, show):

    tvImg = skimage.restoration.denoise_tv_chambolle(inputImg, weight=weight, eps=eps, n_iter_max=n_iter_max, multichannel=multichannel)
    # standard params skimage.restoration.denoise_tv_chambolle(inputImg, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=False)
    tvImg = cv2.cvtColor(tvImg, cv2.COLOR_GRAY2BGR)

    if (show):
        m3F.imshow(tvImg, "Total variation")

    return tvImg