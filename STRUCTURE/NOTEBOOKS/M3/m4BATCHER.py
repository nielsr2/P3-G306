import numpy as np
import glob
import cv2
import os
from datetime import datetime
from . import m3F
from M3 import m3Class
from M3 import m3Show
from M3 import m3CSV

def photoBatcher():
    photoArray = []
    def init(inputFolder, preArray):
        # **********************************************************************
        # import folder of images, append as photo obj to photoArray
        # ______________________________________________________________________
        inputImages = glob.glob(inputFolder + "*.*g")
        inputImages.sort()
        #print("is " + inputImages)
        for imagePath in inputImages:
            # print("?????!!!!!??????")
            inputImage = cv2.imread(imagePath, -1)
            photoArray.append(m3Class.Photo(inputImage, imagePath))
        # **********************************************************************
        # **********************************************************************
            for function in preArray:
                # print("function.__name__  in pre: ", function.__name__, function.__dir__)
                if (function.__name__ == "findEyes68"):
                    # print("FOUND FINDEYES FUNC")
                    for photo in photoArray:
                        params = preArray[function]
                        photo.faces = function(photo, **params)
                elif (function.__name__ == "findEyes194"):
                    params = preArray[function]
                    for photo in photoArray:
                        photo = function(photo, **params)
                else:
                    # for photo in photoArray:
                    params = preArray[function]
                    function(photoArray, **params)

    # **********************************************************************
    def iterate(functionArray):
        for photo in photoArray:
            doingFor = None
            # print("functionArray", functionArray)
            for el in functionArray:
                print("el", el, type(el))
                # el = retdict(**el)
                # print("el", el, type(el))
                for function, params in el.items():
                    # params = functionArray[function]
                    print("function, params", function, params)

                    if (function == "doFor"):
                        # print("shitzngiggles!!!", )
                        for face in photo.faces:
                            for eye in face.eyes:
                                doingFor = params["doAs"]
                                setattr(eye, params["doAs"], getattr(eye, params["original"]))
                            # m3Show.imshow(eye.image, "orignal")
                            # m3Show.imshow(getattr(eye, params["doAs"]), params["doAs"])
                            # print(eye.__dict__.items())
                    elif (function == "doForEye"):
                        print("doingFor = eye")
                        doingFor = "eye"
                    else:

                        print("function.__name__  in pre: ", function.__name__)
                        for face in photo.faces:
                            for eye in face.eyes:
                                m3F.printGreen("doingFor")
                                # m3F.printGreen(str(doingFor))
                                if doingFor == "eye":
                                    eye = function(eye, **params)
                                else:
                                # print("doingFor",doingFor, "gottenattr", getattr(eye, str(doingFor)))
                                    setattr(eye, doingFor, function(getattr(eye, str(doingFor)), **params))
    def post(postArray):
        for function in postArray:
            params = postArray[function]
            photoArray = function(photoArray, **params)
