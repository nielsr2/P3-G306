
from matplotlib import pyplot as plt
import cv2, sys
sys.path.append("/M3")
from M3 import m3F as m3F
from M3 import m3Face as m3Face
from M3 import m3HoughCircle as m3HoughCircle
from M3 import m3Batch as m3Batch
from M3 import m3Pre as m3Pre
from M3 import m3Mask as m3Mask


def n():

    fArray = {m3Face.findEyes: {"inputImg": "ignorethis", "show": True},
            m3Mask.makePolyMask: {"inputImg": "ignorethis", "show": False},
            m3Mask.applyPolyMask: {"inputImg": "ignorethis", "show": True},
            m3HoughCircle.findCircleSimple: {"inputImg": "ignorethis", "show": True}}
            #fArray = {m3Face.findEyes: {"inputImg": "ignorethis"}}

            # fArray = {m3Face.findEyes: {"image": "ignorethis"},
            #           m3HoughCircle.findCircle: {"image": "ignorethis"}}
    #fArray = {m3Pre.gaussianBlur: {"inputImg": "ignorethis", "amount": 3, "show": True}}

    #print(m3F.printRed("TRALALA"))
    #m3Batch.batchProcess2("PICTURES/InputPictures/single/", fArray, True)
    m3Batch.batchProcess2("PICTURES/InputPictures/Set1/", fArray, True)


# sys.path.append('../M3')

# **********************************************************************
# exampe of input
'''
fArray = {function1: {"inputImg": "ignorethis", "param1": "blalbal1"},
          function2: {"inputImg": "ignorethis", "param2": "blalbal2"}}
'''
# **********************************************************************
# fArray = {m3Face.findEyes: {"image": "ignorethis"},
#           m3HoughCirc<le.findCircle: {"image": "ignorethis"}}
#fArray = {m3Face.findEyes: {"inputImg": "ignorethis", "show": True},
 #        m3Pre.gaussianBlur: {"inputImg": "ignorethis", "amount": 3, "show": True},
  #       m3HoughCircle.findCircleSimple: {"inputImg": "ignorethis", "show": True},
   #      m3Mask.makeCircularMask: {"inputImg": "ignorethis", "show": True},
    #     m3Mask.makeFullMask: {"inputImg": "ignorethis", "show": True}}
