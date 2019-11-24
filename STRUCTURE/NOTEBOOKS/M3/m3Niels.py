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
    # iter for iterate ,
    # Iterate: make repeated use of a mathematical or computational procedure, applying it each time to the result of the previous application; perform iteration.
    # **********************************************************************
    # doing facedetection
    # find face function in array, run it, and remove it from array. results in Photo obj with data
    # **********************************************************************
    didFaceDetection = False  #use this for keeping track of this
    for function in functionArray:
        if (function.__name__ == "findEyes"):
            didFaceDetection = True
            findEyesFunction = function
            functionParams = functionArray[function]
            functionParams["photo"] = photo
            photo.faces = function(**functionParams)  # read this, but it's parsing the paramters into the function1
                                                      # http://book.pythontips.com/en/latest/args_and_kwargs.html
    if  (didFaceDetection):
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






def generateComparison(photoArray, fileName=None):
    print("generateComparison")
    facesToSave = []
    for photo in photoArray:
        # if (jnustEyes
        print("PHOTO")
        for face in photo.faces:
            print("FACE")
            eyesToSave = []
            if not (type(face.eyes) == type(None)):
                for eye in face.eyes:
                    m3Show.imshow(eye.wip,"fasf")
                    print(eye,)
                    eyesToSave.append(eye.wip)
                    facesToSave.append(concat(eyesToSave))
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
    # print(facesToSave[0], type(facesToSave[0]))
    output = concat(facesToSave, direction="v")
    m3Show.imshow(output, "asdfadf")
    if (fileName is not None):
        # file = open(("EXPORTS/COMPARISONS/" + fileName + "_" + now_string + ".txt"), "w+")
        # file.write(ffxa)
        cv2.imwrite("EXPORTS/COMPARISONS/" + fileName + "_" + now_string + ".jpg", output)
    else:
        cv2.imwrite("EXPORTS/COMPARISONS/" + now_string + ".jpg", output)

    #
    # if (exportAs == "live"):
    #     # print("photoArray[0].mask", type(photoArray[0].mask))
    #     # print("rep", repr(photoArray[0].mask))
    #     if (photoArray[0].mask is None):
    #         # m3F.printRed("NO FACES, JUST PASSING INPUT")
    #         return cv2.cvtColor(ins, cv2.COLOR_BGR2GRAY)
    #     else:
    #         # m3F.printGreen("PASSING MASK")
    #         return photoArray[0].mask


def exportToFolder(photoArray, folderName=None):
    now_string = datetime.now().strftime("-%d-%m-%Y---%H-%M-%S")
    outputFolder = os.getcwd() + "/EXPORTS/" + inputFolder.replace("PICTURES/","").replace("/", "") + folderName + "_" +  now_string
    # print("path", outputFolder)
    os.mkdir(outputFolder)
    for photo in photoArray:
        imagePath = photo.path
        imagePath = imagePath.replace(inputFolder, "")
        imagePath = outputFolder + imagePath
        cv2.imwrite(imagePath, outputImage)
        pass



def photoBatch(ins, functionArray, postArray=None, preArray=None,  debug=True ):
    photoArray = []
    isSingle = False
    copyfunctionArray = funcArrToStr(functionArray)
    # if debug:
    for function in preArray:
        params = preArray[function]
        function(photoArray, **params)
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

    for function in postArray:
        params = postArray[function]
        function(photoArray, **params)








































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
