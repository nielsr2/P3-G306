from M3 import m3Class
from M3 import m3F as m3F
import cv2
import sys
from PIL import Image, ImageDraw
import face_recognition
import numpy as np
from matplotlib import pyplot as plt
sys.path.append("/M3")
from M3 import m3F as m3F
from M3 import m3Show

# Find all facial features in all the faces in the image


def findEyes(photo, scalePercent, show):
    # print("photo type", type(photo))
    h, w, c = photo.originalImage.shape
    print("originalShape", h,w,c)
    # downScaledDim = (round(w/100 *(scalePercent)),round(h/100 * (scalePercent)))
    downScaledDim = ((round(w/20)),round(h/20))
    inputImg = photo.originalImage.copy()
    inputImg = cv2.resize(inputImg, downScaledDim)
    dimToScaleUp = 20
    print("downScaledDim", downScaledDim )
    # m3Show.imshow(photo.originalImage, " FINDEYS TEST")
    # print("proccesing", inputImgPath),

    # inputImg = cv2.imread(inputImgPath)

    face_landmarks_list = face_recognition.face_landmarks(inputImg)
    #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    #print("face_landmarks_list type was", type(face_landmarks_list))
    # Create a PIL imagedraw object so we can draw on the picture
    # pil_image = Image.fromarray(inputImg)
    pil_image = Image.fromarray(photo.originalImage.copy())
    m3Show.imshow(m3F.typeSwap(pil_image),"fadsf")
    if (len(face_landmarks_list) == 0):
        m3F.printRed(" found no faces in this picture")
        plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_RGB2BGR))
        plt.show()
        return [m3Class.Face(noFaceImg=inputImg)]
    faces = []
    for face_landmarks in face_landmarks_list:

        lEyeCoor = face_landmarks['left_eye']
        rEyeCoor = face_landmarks['right_eye']

        mg = (lEyeCoor[3][0] - lEyeCoor[0][0]) * 0.2 * 10

        # **********************************************************************
        imgwithPoints = inputImg.copy()
        for eye in (lEyeCoor, rEyeCoor):
            for x, y in eye:
                imgwithPoints = cv2.rectangle(imgwithPoints, (x - 2, y - 20), (x + 20, y + 20), (0, 0, 255), -1)
        # **********************************************************************
        # if debug:
        #     m3Show.imshow(imgwithPoints, "with points")

        if lEyeCoor[0][1] > lEyeCoor[3][1]:
            # If tilted left - based on how it's seen on image
            # print("tilted left")
            left = [lEyeCoor[0][0] * dimToScaleUp - mg, lEyeCoor[2][1] * dimToScaleUp - mg, lEyeCoor[3][0] * dimToScaleUp  + mg, lEyeCoor[5][1] * dimToScaleUp  + mg]
            left = [round(num) for num in left]
            right = [rEyeCoor[0][0] * dimToScaleUp  - mg, rEyeCoor[2][1] * dimToScaleUp - mg, rEyeCoor[3][0]* dimToScaleUp  + mg, rEyeCoor[5][1] * dimToScaleUp + mg]
            right = [round(num) for num in right]
            print("L AND R" + str(left) + " " + str(right))
            m3Show.imshow(np.asarray(pil_image.crop(left)), "l")
            m3Show.imshow(np.asarray(pil_image.crop(right)), "r")
            lEye = m3Class.Eye(np.asarray(pil_image.crop(left)), left, lEyeCoor)
            lEye.landmarkPoints = lEyeCoor
            rEye = m3Class.Eye(np.asarray(pil_image.crop(right)), right, rEyeCoor)
            rEye.landmarkPoints = rEyeCoor
        else:
            # If tilted right
            # print("tilted right")
            left = [lEyeCoor[0][0] * dimToScaleUp  - mg, lEyeCoor[1][1] * dimToScaleUp - mg, lEyeCoor[3][0] * dimToScaleUp + mg, lEyeCoor[4][1]* dimToScaleUp  + mg]
            left = [round(num) for num in left]
            right = [rEyeCoor[0][0] * dimToScaleUp - mg, rEyeCoor[1][1] * dimToScaleUp - mg, rEyeCoor[3][0] * dimToScaleUp  + mg, rEyeCoor[4][1] * dimToScaleUp  + mg]
            right = [round(num) for num in right]
            m3Show.imshow(np.asarray(pil_image.crop(left)), "l")
            m3Show.imshow(np.asarray(pil_image.crop(right)), "r")
            lEye = m3Class.Eye(np.asarray(
                pil_image.crop(left)), left, lEyeCoor)
            lEye.landmarkPoints = lEyeCoor
            rEye = m3Class.Eye(np.asarray(
                pil_image.crop(right)), right, rEyeCoor)
            rEye.landmarkPoints = rEyeCoor
    # print('eyeImages', type(eyeImages), len(eyeImages))
    # return eyeImages
        faces.append(m3Class.Face([lEye, rEye]))
    return faces
