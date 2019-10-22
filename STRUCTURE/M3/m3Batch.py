import glob
# from PIL import Image
import cv2
# import numpy as np
# import types
import os
import datetime


# **********************************************************************
# exampe of input
'''
fArray = {function1: {"image": "ignorethis", "param1": "blalbal1"},
          function2: {"image": "ignorethis", "param2": "blalbal2"}}
'''
# **********************************************************************


def batchProcess(inputFolder, functionArray, export):
    inputImages = glob.glob(inputFolder + "*.j*")
    outputFolder = "../PICTURES"
    if not (os.path.exists(outputFolder)):  # if outfolder does not exist, create it
        os.mkdir("../PICTURES/" + datetime.date())
    if (export):
        print("../PICTURES/" + datetime.date())
    # print("output folder did not exist,", outputFolder, "created.")
    for imagePath in inputImages:
        if (m3F.evalSize(imagePath, 10, 10)):
            # -1 means "return the loaded image as is (with alpha channel)."
            inputImage = cv2.imread(imagePath, -1)
            for key in functionArray:
                current = functionArray[key]
                print("current function: ", current)
                current["image"] = inputImage
                outputImage = key(**current)  # https://realpython.com/python-kwargs-and-args/
                inputImage = outputImage
        else:
            print("************************************************************\
                    ****************************************************")
            m3F.printRed("IMAGE TOOO SMALL")
            continue
        if (export):
            imagePath = imagePath.replace(inputFolder, "")
            imagePath = outputFolder + imagePath
            cv2.imwrite(imagePath, outputImage)
