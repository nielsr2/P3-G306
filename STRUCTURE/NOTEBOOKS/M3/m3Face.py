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
from datetime import datetime
import dlib

# this uses the library face_recognition to find 68 points.
# first the image is downscaled, to allow faster processing
# the landmarks of each are aree sorted, as to get the boundaries of the eye
# A margin of 0.2 is added


def findEyes(photo, division, show=True, debug=False):
    h, w, c = photo.originalImage.shape
    downScaledDim = ((round(w/division)), round(h/division))
    copy = photo.originalImage.copy()
    pil_image = Image.fromarray(copy)
    inputImg = copy
    inputImg = cv2.resize(inputImg, downScaledDim)
    photo.loResImage = inputImg

    if debug:
        print("originalShape", h, w, c)
        print("downScaledDim", downScaledDim)
        m3Show.imshow(m3F.typeSwap(pil_image), "image to find eyes on")

    face_landmarks_list = face_recognition.face_landmarks(inputImg)

    if debug:
        print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
        print("face_landmarks_list type was", type(face_landmarks_list))

    if (len(face_landmarks_list) == 0):

        m3F.printRed(" found no faces in this picture")
        plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_RGB2BGR))
        plt.show()
        return [m3Class.Face(noFaceImg=inputImg)]

    faces = []
    for face_landmarks in face_landmarks_list:

        LeftEyeLandmarks = face_landmarks['left_eye']
        rightEyeLandmarks = face_landmarks['right_eye']

        # imgwithPoints = inputImg.copy()
        # for eye in (LeftEyeLandmarks, rightEyeLandmarks):
        #     for x, y in eye:
        #         imgwithPoints = cv2.rectangle(imgwithPoints, (x - 20, y - 20), (x + 20, y + 20), (0, 0, 255), -1)
        # **********************************************************************
        # if debug:
        #     m3Show.imshow(imgwithPoints, "with points")
        eyes = []
        for eyeLandmarkPoints in LeftEyeLandmarks, rightEyeLandmarks:
            xs, ys = [], []
            for x, y in eyeLandmarkPoints:
                xs.append(x)
                ys.append(y)
                # print("x y ", x, y)
            xs.sort(reverse=True)
            ys.sort(reverse=True)
            maxX = xs[0]
            maxY = ys[0]
            xs.sort(reverse=False)
            ys.sort(reverse=False)
            minX = xs[0]
            minY = ys[0]
            # print("maxX,maxY,minX,minY", maxX, maxY, minX, minY)
            margin = round((maxX - minX) * 0.2)
            cropRect = (minX - margin, minY - margin,
                        maxX + margin, maxY + margin)
            cropRect = [round(division*num) for num in cropRect]
            # for num in margin: num * division
            if show:
                m3Show.imshow(np.asarray(pil_image.crop(cropRect)), "cropRect")
            upscaledLandmarks = []
            for x, y in eyeLandmarkPoints:
                upscaledLandmarks.append((x * division, y * division))
                # y = y * division
            # print("upscaledLandmarks", upscaledLandmarks)
            eyes.append(m3Class.Eye(np.asarray(pil_image.crop(cropRect)), cropRect, upscaledLandmarks))
        faces.append(m3Class.Face(eyes))
    return faces


predictor = dlib.shape_predictor("MODELS/shape_predictor_194_face_landmarks.dat")

# predictor = dlib.shape_predictor(("MODELS/2.dat"))

# def find194(img):

def findEyes2(photo, division, show=True, ):
    img = photo.loResImage
    dimToScaleUp = division
    detector = dlib.get_frontal_face_detector()
    foundFaces = detector(img, 1)
    # print("foundFaces", foundFaces)
    # print("Number of faces detected: {}".format(len(foundFaces)))
    for index, data in enumerate(foundFaces):
        if index == 0:
            shape = predictor(img, data)
            points = []
            for i in range(shape.num_parts):
                point = shape.part(i)
                if (i >= 26 and i <= 69):  #
                    points.append([round(point.x * division), round(point.y * division)])
            for eye in photo.faces[0].eyes:
                cropRect = eye.cropRect
                # print("cropRect", cropRect)
                eye.manyLandmarkPoints = []
                ys = []
                for x, y in points:
                    ys.append(y)
                    # ensure that the points are within the croprect from 68 landmarks
                    # croprect: "The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate"
                    if (x > cropRect[0] and x < cropRect[2]):
                        if (y > cropRect[1] and y < cropRect[3]):
                            eye.manyLandmarkPoints.append([x, y])
    return photo
