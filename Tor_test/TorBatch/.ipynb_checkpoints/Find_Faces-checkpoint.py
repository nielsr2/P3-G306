import glob
from PIL import Image
import cv2 
import numpy as np
import types
import os
import m3Face, m3Iris, m3F
from matplotlib import pyplot as plt
inputFolder = "faces/"
outputFolder = "eyes/"
eyesExpected = 37   # Manually type in the number of eyes expected from inputFolder
eyesFound = 0

inputImages=glob.glob(inputFolder + "*.j*")

for imagePath in inputImages:
    
    # if outfolder does not exist, create it
    if not (os.path.exists(outputFolder)):
            os.mkdir(outputFolder)
            print("output folder did not exist,", outputFolder, "created.")
    # read input image
#    imgIn = cv2.imread()
    

    
    # DO STUFF TO ALL IMAGES BELOW
    # *************************

    imgOut = m3Face.findEyes(imagePath)
    # *************************

        #change imagePath from input folder to output folder
    imagePath = imagePath.replace(inputFolder, "")
    inputName = imagePath.replace(".jpeg", "")
    imagePath = outputFolder + inputName
    
    if (type(imgOut) == type(list()) and len(imgOut) > 0):
        eyes = iter(imgOut) # used to iterate through an array. the output of first next() is the first element of array, and so on
        eyeCount = 1
        faceCount = 1
        
        for i in imgOut:
            LR = "Left"
            if ((eyeCount % 2) == 0):
                LR = "Right"
            ouputImg = "{}_Face_{}_{}.jpeg".format(imagePath,str(faceCount),LR)
            cv2.imwrite(ouputImg,next(eyes))
            eyesFound += 1
            
            if ((eyeCount % 2) == 0):
                faceCount += 1
            eyeCount += 1

m3F.printBlue("Found {}% of eyes in the images".format(eyesFound/eyesExpected*100))