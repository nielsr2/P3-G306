import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class

# **********************************************************************
# exampe of input
'''Batch process a image folder with an array of functions.

Keyword arguments:
inputFolder -- String for inputFolder (relative to where function is called)
functionArray -- A dictionary of function : {params}. see example:

fArray = {function1: {"inputImg": "tobereplacebyactualimageobj", "param1": "blalbal1"},
          function2: {"inputImg": "ignorethis", "param2": "blalbal2"}}

export = boolean on whether to export the final result as an img
'''
# **********************************************************************


def nTest():
    return "test1", "test2"


def batchProcess2(inputFolder, functionArray, export):
    # print("batchProcess ran with folder: " + inputFolder)
    inputImages = glob.glob(inputFolder + "*.*g")
    outputFolder = "../PICTURES"
    # if not (os.path.exists(outputFolder)):  # if outfolder does not exist, create it
    # print("inputImages", inputImages)
    if (export):
        now = datetime.now()
        now_string = now.strftime("-%d-%m-%Y---%H-%M-%S")
        outputFolder = os.getcwd() + "/EXPORTS/" + inputFolder.replace("PICTURES/", "").replace("/", "") + now_string
        # print("path", outputFolder)
        os.mkdir(outputFolder)
        # print("../PICTURES/" + datetime.date())
    # print("output folder did not exist,", outputFolder, "created.")

# **********************************************************************
# IF FACE
    eyeImgArray = []
    didEyes = False
    for function in functionArray:
        if (function.__name__ == "findEyes"):
            didEyes = True
            eyeFunc = function
            currentFunction = functionArray[function]

            for imagePath in inputImages:
                inputImage = cv2.imread(imagePath, -1)
                currentFunction["inputImg"] = inputImage
                face = m3Class.Immer(inputImage, imagePath)
                face.eyes = function(**currentFunction)
                eyeImgArray.append(face)
    functionArray.pop(eyeFunc)
# **********************************************************************
    if (didEyes):
        inputImages = eyeImgArray
    for imagePath in inputImages:

        print("************************************************************\
            ****************************************************")

        # -1 means "return the loaded image as is (with alpha channel)."
        if (didEyes):
            inputImage = imagePath
        else:
            print("processing: " + imagePath)
            inputImage = cv2.imread(imagePath, -1)
        for function in functionArray:
            currentFunction = functionArray[function]
            # print("current function: ", current)
            currentFunctionName = function.__name__
            print("function name ", function.__name__)
            # m3F.imshow(inputImage, "BATCH DEBUGGING")
            # https://realpython.com/python-kwargs-and-args/
            if (didEyes):
                if (imagePath.eyes is not None):
                    for eye in imagePath.eyes:
                        # print("eye coor: " + str(eye.coordinates))
                        if (currentFunctionName == "findCircleSimple" or currentFunctionName == "makeCircularMask"):
                            currentFunction["inputImg"] = eye
                            eye = function(**currentFunction)
                        # elif not (currentFunctionName == "makeFullMask"):
                        #     currentFunction["inputImg"] = eye.image
                        #     eye.image = function(**currentFunction)
                    if(currentFunctionName == "makeFullMask" or currentFunctionName == "makePolyMask"):
                        print("FULL OR POLY")
                        currentFunction["inputImg"] = imagePath
                        imagePath = function(**currentFunction)
            else:
                currentFunction["inputImg"] = inputImage
                outputImage = function(**currentFunction)
                inputImage = outputImage
        if (export and not didEyes):
            imagePath2 = imagePath.path.replace(inputFolder, "")
            outPath = outputFolder + "/" + imagePath2
            # print("OUT PATH: ", outPath)
            cv2.imwrite(outPath, outputImage)


def batchProcess(inputFolder, functionArray, export):

    # print("batchProcess ran with folder: " + inputFolder)
    inputImages = glob.glob(inputFolder + "*.*g")
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
        # if (m3F.evalSize(imagePath, 10, 10)):
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
        # else:
        #     print("************************************************************\
        #             ****************************************************")
        #     m3F.printRed("IMAGE TOOO SMALL")
        #     continue
        if (export):
            imagePath = imagePath.replace(inputFolder, "")
            imagePath = outputFolder + imagePath
            cv2.imwrite(imagePath, outputImage)
