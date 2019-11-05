import numpy as np
import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class
from M3 import m3Show

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
        outputFolder = os.getcwd() + "/EXPORTS/" + inputFolder.replace("PICTURES/",
                                                                       "").replace("/", "") + now_string
        # print("path", outputFolder)
        os.mkdir(outputFolder)
        # print("../PICTURES/" + datetime.date())
    # print("output folder did not exist,", outputFolder, "created.")

# **********************************************************************
# IF FACE
    faceArray = []
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
                faceArray.append(face)
    functionArray.pop(eyeFunc)
# **********************************************************************
    if (didEyes):
        inputImages = faceArray
    for imagePath in inputImages:
        m3Show.imshow(imagePath.orginalImage, "original photo")
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
                        elif not (currentFunctionName == "makeFullMask" or currentFunctionName == "makePolyMask" or currentFunctionName == "applyPolyMask" or currentFunctionName == "makeComparison"):
                            currentFunction["inputImg"] = eye.image
                            eye.image = function(**currentFunction)
                        # elif not (currentFunctionName == "makeFullMask"):
                        #     currentFunction["inputImg"] = eye.image
                        #     eye.image = function(**currentFunction)
                    if(currentFunctionName == "makeFullMask" or currentFunctionName == "makePolyMask" or currentFunctionName == "applyPolyMask"):
                        print("FULL OR POLY")
                        currentFunction["inputImg"] = imagePath
                        imagePath = function(**currentFunction)
                    if(currentFunctionName == "makeComparison"):
                        currentFunction["faceArray"] = faceArray
                        currentFunction["functionArray"] = functionArray
                        function(**currentFunction)
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


def makeComparison(faceArray, functionArray, fileName):
    faces = []
    # print(str(functionArray))
    for face in faceArray:
        eyes = []
        if not (type(face.eyes) == type(None)):
            for eye in face.eyes:
                # h = m3Show.Histogram(eye.image, passThru=False)
                eyes.append(eye.image)
        else:
            text = np.zeros(shape=[200, 300, 3], dtype=np.uint8)
            cv2.putText(
                    img=text,
                    text="no eyes found",
                    org=(0, 0),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=4,
                    color=(255, 255, 255))
            eyes.append(text)
        eyes = concat(eyes)
        faces.append(eyes)
        now = datetime.now()
        now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
    output = concat(faces, direction="v")
    cv2.imwrite("EXPORTS/COMPARISONS/" + fileName + ".jpg", output)

def concat(images, direction="h"):
    hs, ws = [], []
    for img in images:
        h, w, c = img.shape
        hs.append(h)
        ws.append(w)
    hs.sort(reverse=True)
    ws.sort(reverse=True)
    outImgs = []
    for img in images:
        newSize = np.zeros_like(img)
        newSize = np.resize(newSize, (hs[0], ws[0], 3))
        newSize[0:img.shape[0], 0:img.shape[1]] = img
        outImgs.append(newSize)
    if (direction == "h"):
        result = np.concatenate((outImgs), axis=1)
    else:
        result = np.concatenate((outImgs), axis=0)
    return result
    # m3Show.imshow(fnes, "new sie test")
    # print("sort", hs[0], newSize.shape)
