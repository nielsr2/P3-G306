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

    for function in functionArray:
        functionParams = functionArray[function]
        currentFunctionName = function.__name__
        m3F.printBlue("function name " + currentFunctionName)
        # currentFunction["inputImg"] = inputImages
        # **********************************************************************
        if ("inputImg" in functionParams):
            # print("was inputImg")
            # print(photo)
            for face in photo.faces:
                if face.eyes is not None:
                    for eye in face.eyes:
                        m3F.printBlue(("Doing an inputimg as eye.wip with" +    currentFunctionName))
                        functionParams["inputImg"] = eye.wip
                        eye.wip = function(**functionParams)
                        # m3Show.imshow(eye.wip, "eye.wip")
        if ("photo" in functionParams):
            m3F.printBlue("Doing an photo with" + currentFunctionName)
            functionParams["photo"] = photo
            photo = function(**functionParams)
        if ("eye" in functionParams):
            m3F.printBlue(("Doing an eye with" + currentFunctionName))
            for face in photo.faces:
                if face.eyes is not None:
                    for eye in face.eyes:
                        functionParams["eye"] = eye
                        eye = function(**functionParams)
        if ("iris" in functionParams):
            m3F.printBlue(("Doing an eye with" + currentFunctionName))
            for face in photo.faces:
                if face.eyes is not None:
                    for eye in face.eyes:
                        functionParams["eye"] = eye.masked
                        eye.masked = function(**functionParams)
    return photo


def funcArrToStr(multilevelDict):
    dict = []
    for function in multilevelDict:
        print(function.__name__)
        e = {function.__name__: multilevelDict[function]}
        dict.append(e)
    return json.dumps(dict)

#
# def generateComparison(photoArray, outputName=None, attrs=None ,  fileName=None):
#     print("generateComparison")
#     facesToSave = []
#     for photo in photoArray:
#         # if (jnustEyes
#         # print("PHOTO")
#         for face in photo.faces:
#             # print("FACE")
#             eyesToSave = []
#             if not (type(face.eyes) == type(None)):
#                 for eye in face.eyes:
#                     # m3Show.imshow(eye.wip, "fasf")
#                     # print("EYEYEYEYEYEYEYEYEY")
#                     print(attrs)
#                     for attr in eye.__dict__.items():
#                         # print("attr", attr)
#
#                         if attr[0] in attrs:
#                             # if
#                             if attr[1] is not None:
#                                 facesToSave.append(attr[1])
#                             # else:
#                             #     facesToSave.append(eye.image)
#             # if (len(eyesToSave) > 1):
#                 # facesToSave.append(eyesToSave)
#             # else:
#                 # facesToSave.append(eyesToSave[0])
#     now = datetime.now()
#     now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
#     # print(facesToSave[0], type(facesToSave[0]))
#     output = concat(facesToSave, direction="v")
#     # m3Show.imshow(output, "asdfadf")
#     if (outputName is not None):
#         # file = open(("EXPORTS/COMPARISONS/" + fileName + "_" + now_string + ".txt"), "w+")
#         # file.write(ffxa)
#         cv2.imwrite("EXPORTS/COMPARISONS/" + outputName + "_" + now_string + ".jpg", output)
#     else:
#         cv2.imwrite("EXPORTS/COMPARISONS/" + now_string + ".jpg", output)


def exportToFolder(photoArray, inputFolder, parent=None, fileName=None):
    # outputFolder = os.getcwd() + "/EXPORTS/" + folderName + "_" +  now_string
    now_string = datetime.now().strftime("-%d-%m-%Y---%H-%M-%S")
    outputFolder = os.getcwd() + "/EXPORTS/" + inputFolder.replace("PICTURES/InputPictures", "").replace("/", "") + now_string + "/"
    print("outputFolder", outputFolder)
    # print("path", outputFolder)
    if parent is "Photo":
        for photo in photoArray:
            pass
            # rr = photo.__dict__.items()
    if parent is "Eye":
        for photo in photoArray:
            for face in photo.faces:
                eyeCount = 0
                for eye in face.eyes:
                    for attr in eye.__dict__.items():
                        print("attr", attr)
                        if attr[0] is attr:
                            # m3Show.imshow(attr[1],"asdf")
                            os.makedirs(outputFolder, exist_ok=True)
                            path = outputFolder  + os.path.basename(photo.path) + "_" + str(eyeCount) + ".jpeg"
                            print("path", path)
                            cv2.imwrite(path, attr[1])
                            eyeCount += 1

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
                                m3F.typeSwap(photo.testMask)
                                .crop(eye.cropRect)
                                                )
    return photoArray


def fakeEyes(photoArray):
    print("fakeEyes ran")
    for photo in photoArray:
        # m3Show.imshow(photo.originalImage,"asdfasdf")
        temp = []
        temp.append(m3Class.Face([m3Class.Eye(photo.originalImage)]))
        photo.faces = temp
    return photoArray


def concat(images, direction="h"):
    # print("images", images)
    hs, ws = [], [] # used for storing widths and heights, as images should be of the same size in one of the directons. used for picking highest value
    for img in images:
        # m3Show.imshow(img, "img in images (concat)")
        # if img is not None:
        if (len(img.shape) == 3):
            h, w, c = img.shape
            hs.append(h)
            ws.append(w)
        else:
            h, w = img.shape
            hs.append(h)
            ws.append(w)
    hs.sort(reverse=True)
    ws.sort(reverse=True)
    outImgs = []
    for img in images:

        if img is not None:
            # print("img", img)
            newSize = np.zeros_like(img)
            if (len(img.shape) == 3):
                newSize = np.resize(newSize, (hs[0], ws[0], 3))
            else:
                newSize = np.resize(newSize, (hs[0], ws[0]))
            newSize[0:img.shape[0], 0:img.shape[1]] = img
            outImgs.append(newSize)
    # print("ooutImgs", outImgs)
    # for img in outImgs:
        # m3Show.imshow(img, "outimg in outimages (concat)")
    if (direction == "h"):
        result = np.concatenate(outImgs, axis=1)
    else:
        result = np.concatenate(outImgs, axis=0)
    return result


def rattr(obj, attributeName):
    for attribute in obj.__dict__.items():
        if attribute[0] is attributeName:
            return attribute[1]  # return data for attribute

# , input=irisOrg):
#     return photo


def storeAttr(photo, eyeAttr, attrName):
    for face in photo.faces:
        for eye in face.eyes:
            setattr(eye, attrName, rattr(eye.eyeAttr, attrName))

    return photo

#  attrs: a list of attrs of eye. like ["image", "wip", "iris", "mask"]
def generateComparison(photoArray, outputName=None,
                       attrs=None, folderName=None):
    # print("generateComparison")
    for photo in photoArray:
        facesToSave = []
        for face in photo.faces:
            if not (type(face.eyes) == type(None)): # TODO: fix this
                for eye in face.eyes:
                    # print(attrs)
                    for attr in eye.__dict__.items():
                        # print("attr", attr)
                        if attr[0] in attrs:
                            # if
                            if attr[1] is not None:
                                facesToSave.append(attr[1])
                            # else:
                            #     facesToSave.append(eye.image)
            # if (len(eyesToSave) > 1):
                # facesToSave.append(eyesToSave)
            # else:
                # facesToSave.append(eyesToSave[0])
        now = datetime.now()
        now_string = now.strftime("%d-%m-%Y--%H-%M-%S")
        # print(facesToSave[0], type(facesToSave[0]))
        output = concat(facesToSave, direction="v")
        m3Show.imshow(output, "generateComparison output")
        # if (outputName is not None):
            # file = open(("EXPORTS/COMPARISONS/" + fileName + "_" + now_string + ".txt"), "w+")
            # file.write(ffxa)
        os.makedirs("EXPORTS/" + folderName + "/",exist_ok=True)
        cv2.imwrite("EXPORTS/" + folderName + "/" + os.path.basename(photo.path) + "_"  + ".jpg", output)
        # else:
        #     cv2.imwrite("EXPORTS/COMPARISONS/" + now_string + ".jpg", output)
