import numpy as np
import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class
from M3 import m3Show

def batchProcess2(inputs, functionArray, export):
    faceArray = []
    didFaceDetection = False
    if (type(inputs) == type(str)):
        # doing batchprocess for folder of images
        inputImages = glob.glob(inputs + "*.*g")
        for imagePath in inputImages:
            inputImage = cv2.imread(imagePath, -1)
            faceArray.append(m3Class.Face(inputImage, imagePath))
    else:
        # doing batchprocess for single image
        faceArray.append(m3Class.Face(inputs))

    if (export):
        now = datetime.now()
        now_string = now.strftime("-%d-%m-%Y---%H-%M-%S")
        outputFolder = os.getcwd() + "/EXPORTS/" + inputs.replace("PICTURES/", "").replace("/", "") + now_string
        # print("path", outputFolder)
        os.mkdir(outputFolder)

    for function in functionArray:
        if (function.__name__ == "findEyes"):
            didFaceDetection = True
            eyeFunc = function
            currentFunction = functionArray[function]
            for face in faceArray:
                currentFunction["inputImg"] = face.orginalImage
                face.eyes = function(**currentFunction)

    if (didFaceDetection):
        functionArray.pop(eyeFunc)

    for face in faceArray:
        for function in functionArray:
            currentFunction = functionArray[function]
            # print("current function: ", current)
            currentFunctionName = function.__name__
            print("function name ", function.__name__)
