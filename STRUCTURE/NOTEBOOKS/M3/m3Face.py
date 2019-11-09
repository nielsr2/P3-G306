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


def findEyes(photo, show):
    # print("photo type", type(photo))
    inputImg = photo.originalImage
    # m3Show.imshow(photo.originalImage, " FINDEYS TEST")
    # print("proccesing", inputImgPath),

    # inputImg = cv2.imread(inputImgPath)

    face_landmarks_list = face_recognition.face_landmarks(inputImg)
    #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    #print("face_landmarks_list type was", type(face_landmarks_list))
    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(inputImg)
    if show:
        if (len(face_landmarks_list) == 0):
            m3F.printRed(" found no faces in this picture")
            plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_RGB2BGR))
            plt.show()
    faces = []
    for face_landmarks in face_landmarks_list:

        lEyeCoor = face_landmarks['left_eye']
        rEyeCoor = face_landmarks['right_eye']

        mg = (lEyeCoor[3][0] - lEyeCoor[0][0]) * 0.2

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
            left = [lEyeCoor[0][0] - mg, lEyeCoor[2][1] - mg, lEyeCoor[3][0] + mg, lEyeCoor[5][1] + mg]
            left = [round(num) for num in left]
            right = [rEyeCoor[0][0] - mg, rEyeCoor[2][1] - mg, rEyeCoor[3][0] + mg, rEyeCoor[5][1] + mg]
            right = [round(num) for num in right]
            # print("L AND R" + str(left) + " " + str(right))
            lEye = m3Class.Eye(np.asarray(
                pil_image.crop(left)), left, lEyeCoor)
            lEye.landmarkPoints = lEyeCoor
            rEye = m3Class.Eye(np.asarray(pil_image.crop(right)), right, rEyeCoor)
            rEye.landmarkPoints = rEyeCoor
        else:
            # If tilted right
            # print("tilted right")
            left = [lEyeCoor[0][0] - mg, lEyeCoor[1][1] -
                    mg, lEyeCoor[3][0] + mg, lEyeCoor[4][1] + mg]
            left = [round(num) for num in left]
            right = [rEyeCoor[0][0] - mg, rEyeCoor[1][1] -
                     mg, rEyeCoor[3][0] + mg, rEyeCoor[4][1] + mg]
            right = [round(num) for num in right]
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
