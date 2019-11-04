import glob
import cv2
import os
from datetime import datetime
from . import m3F

# **********************************************************************
# exampe of input
'''Batch process a image folder with an array of functions.

Keyword arguments:
inputFolder -- String for inputFolder (relative to where function is called)
functionArray -- A dictionary of function : {params}. see example:

fArray = {function1: {"inputImg": "ignorethis", "param1": "blalbal1"},
          function2: {"inputImg": "ignorethis", "param2": "blalbal2"}}

export = boolean on whether to export the final result as an img
'''
# **********************************************************************


def batchProcess(inputFolder, functionArray, export):

    # print("batchProcess ran with folder: " + inputFolder)
    inputImages = glob.glob(inputFolder + "*.p*")
    outputFolder = "../PICTURES"
    # if not (os.path.exists(outputFolder)):  # if outfolder does not exist, create it
    # print("inputImages", inputImages)
    if (export):
        now = datetime.now()
        now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
        path = "../PICTURES/" + now_string
        print("path", path)
        os.mkdir(path)
        # print("../PICTURES/" + datetime.date())
    # print("output folder did not exist,", outputFolder, "created.")
    for imagePath in inputImages:
        if (m3F.evalSize(imagePath, 10, 10)):
            print("************************************************************\
                ****************************************************")
            print("processing: " + imagePath)
            # -1 means "return the loaded image as is (with alpha channel)."
            inputImage = cv2.imread(imagePath, -1)
            for function in functionArray:
                currentFunction = functionArray[function]
                # print("current function: ", current)
                currentFunction["inputImg"] = inputImage
                # m3F.imshow(inputImage, "BATCH DEBUGGING")
                # https://realpython.com/python-kwargs-and-args/
                print("**************************************")
                print("running" + str(function))
                outputImage = function(**currentFunction)
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
