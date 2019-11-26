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
        # print("PHOTO")
        for face in photo.faces:
            # print("FACE")
            eyesToSave = []
            if not (type(face.eyes) == type(None)):
                for eye in face.eyes:
                    m3Show.imshow(eye.wip,"fasf")
                    # print("EYEYEYEYEYEYEYEYEY")
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


# def exportToFolder(photoArray, folderName=None):
#     now_string = datetime.now().strftime("-%d-%m-%Y---%H-%M-%S")
#     outputFolder = os.getcwd() + "/EXPORTS/" + folderName + "_" +  now_string
#     # print("path", outputFolder)
#     os.mkdir(outputFolder)
#     for photo in photoArray:
#         # kjkm,
#         for face in photo.faces:
#             # i++
#             for eye in face.eyes:
#                 imagePath = outputFolder + "/" + os.path.basename(photo.path) #takes just the filename part of the path
#         cv2.imwrite(imagePath, eye)
#         pass



def exportToFolder(photoArray, inputFolder, parent=None, fileName=None):
    # outputFolder = os.getcwd() + "/EXPORTS/" + folderName + "_" +  now_string
    now_string = datetime.now().strftime("-%d-%m-%Y---%H-%M-%S")
    outputFolder = os.getcwd() + "/EXPORTS/" + inputFolder.replace("PICTURES/InputPictures","").replace("/", "") + now_string + "/"
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
                        if attr[0] is fileName:
                            m3Show.imshow(attr[1],"asdf")
                            os.makedirs(outputFolder, exist_ok=True)
                            path = outputFolder  + os.path.basename(photo.path) + "_" + str(eyeCount) + ".jpeg"
                            print("path", path)
                            cv2.imwrite(path, attr[1])
                            eyeCount += 1

        # for x in dir(photo):'
        # if childType is not None:
            # for child in
            #     print("debuggins; ", child)
            #     if (type(child[1]) is type(childType)):
            #         for property in child[1].__dict__.items():
            #             if (property is property[0]):
            #                 print("SUCCESS", property)

                    # print(item[0])
                    # print("x",int, x, "type(someType)", type(fileType))
                    # int + 1
                    # if (type(x) is type(someType)):
                    # print(x, "WAS TYPE")



















def photoBatch(ins, functionArray, postArray=None, preArray=None,  debug=True ):
    print("photoBatch")
    photoArray = []
    # copyfunctionArray = funcArrToStr(functionArray)

    # **********************************************************************
    #  checking if folder with imgs, or just a single img
    if (type(ins) is type("str")): #is folder, since it's a folder path
        # print("???????????")
        # doing batchprocess for folder of images
        # m3F.printBlue("doing batchprocess for folder of images")
        # print("is " + ins)
        inputImages = glob.glob(ins + "*.*g")
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
    for function in preArray:
        print("function.__name__  in pre: ", function.__name__ )
        if (function.__name__ == "findEyes"):
            print("FOUND FINDEYES FUNC")
            for photo in photoArray:
                # print("NIBBBBBsss")
                params = preArray[function]
                photo.faces = function(photo, **params)
        elif (function.__name__ == "fakeEyes"):
            print("fakeEyes")
            params = preArray[function]
            photoArray = function(photoArray, **params)
        else:
            # for photo in photoArray:
            params = preArray[function]
            function(photoArray, **params)

    # **********************************************************************
    #  Set debug flag for all functions in functionArray
    for function in functionArray:
        functionParams = functionArray[function]
        functionParams["show"] = debug

    # **********************************************************************
    #  perform iterations on photos
    for photo in photoArray:
        # print(photo)
        # for face in photo.faces:
        #     print(face)
        photo = iterFunction(photo, functionArray)

    # **********************************************************************
    #  perform POST functions ( such as generate comparison etc.)
    for function in postArray:
        params = postArray[function]
        if (function.__name__ == "exportToFolder"):
            function(photoArray, ins, **params)
        else:
            photoArray = function(photoArray, **params)
    #
    #
    # # **********************************************************************
    # # doing facedetection
    # # find face function in array, run it, and remove it from array. results in Photo obj with data
    # # **********************************************************************
    # didFaceDetection = False  #use this for keeping track of this
    # for function in functionArray:
    #      # read this, but it's parsing the paramters into the function1
    #                                                   # http://book.pythontips.com/en/latest/args_and_kwargs.html
    # if  (didFaceDetection):
    #     functionArray.pop(findEyesFunction)
    #
    #
    #


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
    hs, ws = [], []
    for img in images:
        if (len(img.shape) == 3):
            # print("######## WAS 3 DIM")
            h, w, c = img.shape
            hs.append(h)
            ws.append(w)
        else:
            # print("######## WAS ELSE DIM")
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
