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



#        _           _
#       | |         | |
#  _ __ | |__   ___ | |_ ___
# | '_ \| '_ \ / _ \| __/ _ \
# | |_) | | | | (_) | || (_) |
# | .__/|_| |_|\___/ \__\___/
# | |
# |_|



def photoBatch(ins, functionArray, postArray=None, preArray=None, irisArray=None, debug=True, debugIris=True):
    # print("photoBatch")
    photoArray = []
    # **********************************************************************
    #  checking if folder with imgs, or just a single img
    if (type(ins) is type("str")): #is folder, since it's a folder path
        # doing batchprocess for folder of images
        # m3F.printBlue("doing batchprocess for folder of images")
        inputImages = glob.glob(ins + "*.*g")
        inputImages.sort()
        #print("is " + inputImages)


        for imagePath in inputImages:
            # print("?????!!!!!??????")
            inputImage = cv2.imread(imagePath, -1)
            photoArray.append(m3Class.Photo(inputImage, imagePath))
    else:
        # doing batchprocess for single image
        # m3F.printBlue("doing batchprocess for single image")
        photoArray.append(m3Class.Photo(ins, "bla"))

    # **********************************************************************
    # perform PRE functions ( like face detection! )
    print("**********************************************************************")
    print("**********************************************************************")
    m3F.printBlue("DOING PRE FUNCIONS")
    print("**********************************************************************")
    print("**********************************************************************")
    for function in preArray:
        print("function.__name__  in pre: ", function.__name__)
        if (function.__name__ == "findEyes"):
            # print("FOUND FINDEYES FUNC")
            for photo in photoArray:
                # print("NIBBBBBsss")
                params = preArray[function]
                photo.faces = function(photo, **params)
        elif (function.__name__ == "fakeEyes" ):
            # print("fakeEyes")
            params = preArray[function]
            photoArray = function(photoArray, **params)
        elif (function.__name__ == "findEyes2"):
            params = preArray[function]
            for photo in photoArray:
                photo = function(photo, **params)
        else:
            # for photo in photoArray:
            params = preArray[function]
            function(photoArray, **params)

    # **********************************************************************
    #  Set debug flag for all functions in functionArray
    # if debug:
    for function in functionArray:
        params = functionArray[function]
        params["show"] = debug

    # if irisDebug:
    for function in irisArray:
        params = irisArray[function]
        params["show"] = debugIris

    # **********************************************************************
    #  perform iterations on photos
    print("**********************************************************************")
    print("**********************************************************************")
    m3F.printBlue("DOING FUNCION ARRAY")
    print("**********************************************************************")
    print("**********************************************************************")
    for photo in photoArray:
        # print(photo)
        # for face in photo.faces:
        #     print(face)
        photo = iterFunction(photo, functionArray)


    # **********************************************************************
    # perform stuff on irisArray
    print("**********************************************************************")
    print("**********************************************************************")
    m3F.printBlue("DOING IRIS FUNCION ARRAY")
    #          _ . - = - . _
    #        . "  \  \   /  /  " .
    #      ,  \                 /  .
    #    . \   _,.--~=~"~=~--.._   / .
    #   ;  _.-"  / \ !   ! / \  "-._  .
    #  / ,"     / ,` .---. `, \     ". \
    # /.'   `~  |   /:::::\   |  ~`   '.\
    # \`.  `~   |   \:::::/   | ~`  ~ .'/
    #  \ `.  `~ \ `, `~~~' ,` /   ~`.' /
    #   .  "-._  \ / !   ! \ /  _.-"  .
    #    ./    "=~~.._  _..~~=`"    \.
    #      ,/         ""          \,
    #        . _/             \_ .
    #           " - ./. .\. - "
    # print("**********************************************************************")
    print("**********************************************************************")
    for function in irisArray:
        m3F.printBlue("function name " + function.__name__)
        params = irisArray[function]

        if ("eye" in params):
            # m3F.printBlue(("Doing an eye with" + currentFunctionName))
            for photo in photoArray:
                for face in photo.faces:
                    # if face.eyes is not None:
                    for eye in face.eyes:
                        params["eye"] = eye
                        eye = function(**params)
        else:
            for photo in photoArray:
                for face in photo.faces:
                    if face.eyes is not None:
                        for eye in face.eyes:
                            if eye.iris is not None:
                                params["inputImg"] = eye.iris
                                eye.iris = function(**params)
                                # m3Show.imshow(eye.iris, "eye.iris NIELS TEST")
    # **********************************************************************
    #  perform POST functions ( such as generate comparison etc.)f
    for function in postArray:
        params = postArray[function]
        if (function.__name__ == "exportToFolder"):
            function(photoArray, ins, **params)
        else:
            photoArray = function(photoArray, **params)
    return photoArray


def loadMasksForComparison(photoArray, maskFolder):
    maskImgs = glob.glob(maskFolder + "*.*g")
    # print("is " + inputImages)
    print("maskImgs", maskImgs)
    maskImgs.sort()
    print("maskImgs", maskImgs)
    # for maskPath in maskImgs:
    #       print("maskPath", maskPath
    count = 0
    for photo in photoArray:
        # inputImage = cv2.imread(imagePath, -1)
        photo.testMask = cv2.imread(maskImgs[count], -1)
        m3Show.imshow(photo.testMask, "photo.testMask")
        count += 1
        for face in photo.faces:
            for eye in face.eyes:
                eye.testMask = m3F.typeSwap(
                                m3F.typeSwap(
                                 photo.testMask)
                                .crop(eye.cropRect)
                                                )
    return photoArray
