
import cv2, sys
sys.path.append("/M3")
from M3 import m3F as m3F
from M3 import m3Face as m3Face
from M3 import m3HoughCircle as m3HoughCircle
from M3 import m3Batch as m3Batch
# sys.path.append('../M3')

# **********************************************************************
# exampe of input
'''
fArray = {function1: {"image": "ignorethis", "param1": "blalbal1"},
          function2: {"image": "ignorethis", "param2": "blalbal2"}}
'''
# **********************************************************************
# fArray = {m3Face.findEyes: {"image": "ignorethis"},
#           m3HoughCircle.findCircle: {"image": "ignorethis"}}
fArray = {m3HoughCircle.findCircle: {"image": "ignorethis"}}


m3Batch.batchProcess("/PICTURES/Eyes", fArray, False)
