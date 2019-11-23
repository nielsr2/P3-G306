import numpy as np
import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class
from M3 import m3Show


def iterFunction(photo, functionArray):
    # **********************************************************************
    # doing facedetection
    # find function in array, run it, and remove it from array. results in Photo obj with data
    # **********************************************************************
    didFaceDetection = False
    for function in functionArray:
        if (function.__name__ == "findEyes"):
            didFaceDetection = True
            findEyesFunction = function
            functionParams = functionArray[function]
            functionParams["photo"] = photo
            photo.faces = function(**functionParams)
    if (didFaceDetection):
        functionArray.pop(findEyesFunction)
    for function in functionArray:
        functionParams = functionArray[function]
        currentFunctionName = function.__name__
        m3F.printBlue("function name " + currentFunctionName)
        # currentFunction["inputImg"] = inputImages
        # **********************************************************************
        if ("inputImg" in functionParams and didFaceDetection):
            # print("was inputImg")
            for face in photo.faces:
                for eye in face.eyes:
                    m3F.printBlue(("Doing an inputimg as eye.wip with" + currentFunctionName))
                    functionParams["inputImg"] = eye.wip
                    eye.wip = function(**functionParams)
                    # m3Show.imshow(eye.wip, "eye.wip")
        if ("photo" in functionParams and didFaceDetection):
            m3F.printBlue("Doing an photo with" + currentFunctionName)
            functionParams["photo"] = photo
            photo = function(**functionParams)
        if ("eye" in functionParams and didFaceDetection):
            m3F.printBlue(("Doing an eye with" + currentFunctionName))
            for face in photo.faces:
                for eye in face.eyes:
                    functionParams["eye"] = eye
                    eye = function(**functionParams)
    return photo


def nibBatch(ins, functionArray, exportAs="live", debug=True):
    photoArray = []
    isSingle = False
    copyfunctionArray = functionArray.copy()
    # if debug:
    for function in functionArray:
        functionParams = functionArray[function]
        functionParams["show"] = debug
    if (type(ins) is type("str")):
        # doing batchprocess for folder of images
        # m3F.printBlue("doing batchprocess for folder of images")
        inputImages = glob.glob(ins + "*.*g")
        for imagePath in inputImages:
            inputImage = cv2.imread(imagePath, -1)
            photoArray.append(m3Class.Photo(inputImage, imagePath))
    else:
        # doing batchprocess for single image
        isSingle = True
        # m3F.printBlue("doing batchprocess for single image")
        photoArray.append(m3Class.Photo(ins, "bla"))

    for photo in photoArray:
        photo = iterFunction(photo, copyfunctionArray)


    if (exportAs == "live"):
        # print("photoArray[0].mask", type(photoArray[0].mask))
        # print("rep", repr(photoArray[0].mask))
        if (photoArray[0].mask is None):
            # m3F.printRed("NO FACES, JUST PASSING INPUT")
            return cv2.cvtColor(ins, cv2.COLOR_BGR2GRAY)
        else:
            # m3F.printGreen("PASSING MASK")
            return photoArray[0].mask
