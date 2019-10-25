import glob
from PIL import Image
import cv2 
import numpy as np
import types
import os
import m3Iris, m3F
inputFolder = "eyes/"
outputFolder = "irises/"
irisesExpected = m3F.filecount(inputFolder)
irisesFound = 0

inputImages=glob.glob(inputFolder + "*.j*")

for imagePath in inputImages:
    
    # if outfolder does not exist, create it
    if not (os.path.exists(outputFolder)):
            os.mkdir(outputFolder)
            print("output folder did not exist,", outputFolder, "created.")
    

    # DO STUFF TO ALL IMAGES BELOW (SENDS IMAGEPATH TO YOUR FUNCTIONS)
    # *************************
    if (m3F.evalSize(imagePath,10,10)):
        imgOut = m3Iris.findCircle(imagePath)
    else:
        print("****************************************************************************************************************")
        m3F.printRed("####IMAGE TOOO SMALL###")
        continue;
        # *************************

     #change imagePath from input folder to output folder
    imagePath = imagePath.replace(inputFolder, "")
    imagePath = outputFolder + imagePath
    print("imagePath", imagePath)
    print("length",len(imgOut))
    
    if (type(imgOut) == type(list())):
        #print("was list")
        # if output 
        eyes = iter(imgOut) # used to iterate thru an array. the output of first next() is the first element of array, and so on
        
        cv2.imwrite(imagePath,next(eyes))
        irisesFound += 1
    else:
        if not(type(imgOut) == type(None)):
            cv2.imwrite(imagePath,imgOut)
            irisesFound += 1
        #else:   
            #m3F.printRed("IMAGE NULL")
            
m3F.printBlue("Found {}% of irises in the images".format(irisesFound/irisesExpected*100))