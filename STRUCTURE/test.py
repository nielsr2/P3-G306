
import cv2, sys
import M3
# sys.path.append('../M3')

# **********************************************************************
# exampe of input
'''
fArray = {function1: {"image": "ignorethis", "param1": "blalbal1"},
          function2: {"image": "ignorethis", "param2": "blalbal2"}}
'''
# **********************************************************************
fArray = {M3.findEyes: {"image": "ignorethis"},
          M3.findCircle: {"image": "ignorethis"}}

M3.batchProcess("../PICTURES/InputPictures/Set1", fArray, False)
