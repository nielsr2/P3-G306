from M3 import m3Class
from M3 import m3F as m3F
import cv2
import sys
from PIL import Image, ImageDraw
import face_recognition
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
from M3 import m3Show


def i(eye, show):
    m3Show.imshow(eye.wip, "wip i i i i ")
    ii = cv2.integral(eye.wip)
    print("ii ", ii)
    m3Show.imshow(ii, " ii i i i i ")
