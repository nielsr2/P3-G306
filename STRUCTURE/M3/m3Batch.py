import glob
from PIL import Image
import cv2
import numpy as np
import types
import os
import m3Iris
import m3F
inputFolder = "eyes/"
outputFolder = "irises/"


inputImages = glob.glob(inputFolder + "*.j*")

for imagePath in inputImages:
    # TODO: fix how these folders work
    # if outfolder does not exist, create it
    if not (os.path.exists(outputFolder)):
        os.mkdir(outputFolder)
        print("output folder did not exist,", outputFolder, "created.")


    if (m3F.evalSize(imagePath, 10, 10)):
        # -1 means "return the loaded image as is (with alpha channel)."
        imgIn = cv2.imread(imagePath, -1)
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # DO STUFF TO IMAGES IN THIS BLOCK
        # TODO: check if this was afunction, if we can have an array of functions parsed in here
        # https://stackoverflow.com/questions/706721/how-do-i-pass-a-method-as-a-parameter-in-python
        imgOut = m3Iris.findCircle(imagePath)
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    else:
        print("****************************************************************************************************************")
        m3F.printRed("####IMAGE TOOO SMALL###")
        continue
        # *************************

     # change imagePath from input folder to output folder
    imagePath = imagePath.replace(inputFolder, "")
    imagePath = outputFolder + imagePath
    # print("imagePath", imagePath)
    cv2.imwrite(imagePath, imgOut)
