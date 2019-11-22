import numpy as np
import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class
from M3 import m3Show
import json


def iterFunction(photo, functionArray):
    # **********************************************************************
    # doing facedetection
    # find face function in array, run it, and remove it from array. results in Photo obj with data
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


def funcArrToStr(multilevelDict):
    dict = []
    for function in multilevelDict:

        print(function.__name__)
        e = {function.__name__: multilevelDict[function]}
        dict.append(e)
    return json.dumps(dict)


def nibBatch(ins, functionArray, exportAs="live", comparisonName=None, debug=True):
    photoArray = []
    isSingle = False
    copyfunctionArray = funcArrToStr(functionArray)
    # if debug:
    for function in functionArray:
        functionParams = functionArray[function]
        functionParams["show"] = debug
    if (type(ins) is type("str")): #is folder, since it's a folder path
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
        photo = iterFunction(photo, functionArray)

    if (exportAs == "live"):
        # print("photoArray[0].mask", type(photoArray[0].mask))
        # print("rep", repr(photoArray[0].mask))
        if (photoArray[0].mask is None):
            # m3F.printRed("NO FACES, JUST PASSING INPUT")
            return cv2.cvtColor(ins, cv2.COLOR_BGR2GRAY)
        else:
            # m3F.printGreen("PASSING MASK")
            return photoArray[0].mask

    if (exportAs == "comparison"):
        facesToSave = []
        for photo in photoArray:
            for face in photo.faces:
                eyesToSave = []
                if not (type(face.eyes) == type(None)):
                    for eye in face.eyes:
                        eyesToSave.append(eye.wip)
                    facesToSave.append(concat(eyesToSave))
        now = datetime.now()
        now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
        output = concat(facesToSave, direction="v")
        m3Show.imshow(output, "asdfadf")
        if (comparisonName is not None):
            file = open(("EXPORTS/COMPARISONS/" + comparisonName + "_" + now_string + ".txt"), "w+")
            file.write(copyfunctionArray)
            cv2.imwrite("EXPORTS/COMPARISONS/" + comparisonName + "_" + now_string + ".jpg", output)
        else:
            cv2.imwrite("EXPORTS/COMPARISONS/" + now_string + ".jpg", output)

#
# def makeComparison(photoArray, functionArray, fileName):
#     faces = []
#     # print(str(functionArray))
#     for face in photoArray:
#         eyes = []
#         if not (type(face.eyes) == type(None)):
#             for eye in face.eyes:
#                 # h = m3Show.Histogram(eye.image, passThru=False)
#                 print( "**********************************************************************")
#                 print("appending EYES ******")
#                 eyes.append(eye.image)
#             eyes = concat(eyes)
#             faces.append(eyes)
#         now = datetime.now()
#         now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
#     output = concat(faces, direction="v")
#     cv2.imwrite("EXPORTS/COMPARISONS/" +  + ".jpg", output)

def concat(images, direction="h"):
    # print("images", images)
    hs, ws = [], []
    for img in images:
        if (len(img.shape) == 3):
            print("######## WAS 3 DIM")
            h, w, c = img.shape
            hs.append(h)
            ws.append(w)
        else:
            print("######## WAS ELSE DIM")
            h, w = img.shape
            hs.append(h)
            ws.append(w)
    hs.sort(reverse=True)
    ws.sort(reverse=True)
    outImgs = []
    for img in images:
        newSize = np.zeros_like(img)
        if (len(img.shape) == 3):
            newSize = np.resize(newSize, (hs[0], ws[0], 3))
        else:
            newSize = np.resize(newSize, (hs[0], ws[0]))
        newSize[0:img.shape[0], 0:img.shape[1]] = img
        outImgs.append(newSize)
    if (direction == "h"):
        result = np.concatenate((outImgs), axis=1)
    else:
        result = np.concatenate((outImgs), axis=0)
    return result
