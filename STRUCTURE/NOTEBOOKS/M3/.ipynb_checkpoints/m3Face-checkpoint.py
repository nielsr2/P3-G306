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
# Find all facial features in all the faces in the image


def findEyes(photo, division, show=True):
    # print("photo type", type(photo))
    h, w, c = photo.originalImage.shape

    # downScaledDim = (round(w/100 *(scalePercent)),round(h/100 * (scalePercent)))
    downScaledDim = ((round(w/division)), round(h/division))
    copy = photo.originalImage.copy()
    pil_image = Image.fromarray(copy)
    inputImg = copy
    inputImg = cv2.resize(inputImg, downScaledDim)
    dimToScaleUp = division
    # if show:
        # print("originalShape", h, w, c)
        # print("downScaledDim", downScaledDim)
        # m3Show.imshow(m3F.typeSwap(pil_image), "image to find eyes on")
    # m3Show.imshow(photo.originalImage, " FINDEYS TEST")
    # print("proccesing", inputImgPath),

    # inputImg = cv2.imread(inputImgPath)

    face_landmarks_list = face_recognition.face_landmarks(inputImg)
    #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    #print("face_landmarks_list type was", type(face_landmarks_list))
    # Create a PIL imagedraw object so we can draw on the picture
    # pil_image = Image.fromarray(inputImg)

    if (len(face_landmarks_list) == 0):

        m3F.printRed(" found no faces in this picture")
        plt.imshow(cv2.cvtColor(inputImg, cv2.COLOR_RGB2BGR))
        plt.show()
        return [m3Class.Face(noFaceImg=inputImg)]
    faces = []
    for face_landmarks in face_landmarks_list:

        lEyeCoor = face_landmarks['left_eye']
        rEyeCoor = face_landmarks['right_eye']
        print()
        mg = (lEyeCoor[3][0] - lEyeCoor[0][0]) * 0.2 * 10

        # **********************************************************************
        imgwithPoints = inputImg.copy()
        for eye in (lEyeCoor, rEyeCoor):
            for x, y in eye:
                imgwithPoints = cv2.rectangle(imgwithPoints, (x - 2, y - 20), (x + 20, y + 20), (0, 0, 255), -1)
        # **********************************************************************
        # if debug:
        #     m3Show.imshow(imgwithPoints, "with points")
        eyes = []
        for eyeLandmarkPoints in lEyeCoor, rEyeCoor:
            xs, ys = [],[]
            for x, y in eyeLandmarkPoints:
                xs.append(x)
                ys.append(y)
                print("x y ", x, y)
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
            cropRect = (minX - margin, minY - margin, maxX + margin, maxY + margin)
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

import dlib



def findEyes2(photo, division, show=True):
    detector = dlib.get_frontal_face_detector()

    # downScaledDim = (round(w/100 *(scalePercent)),round(h/100 * (scalePercent)))
    h, w, c = photo.originalImage.shape
    downScaledDim = ((round(w/division)),round(h/division))
    copy = photo.originalImage.copy()
    pil_image = Image.fromarray(copy)
    inputImg = copy
    img = cv2.resize(inputImg, downScaledDim)
    dimToScaleUp = division
    predictor = dlib.shape_predictor
    ("MODELS/shape_predictor_194_face_landmarks.dat")
    dets = detector(img, 1)
    print("dets", dets)
    print("Number of faces detected: {}".format(len(dets)))
    for k, d in enumerate(dets):
        # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
        #     k, d.left(), d.top(), d.right(), d.bottom()))
        # Get the landmarks/parts for the face in box d.
        shape = predictor(img, d)
        print("kkkk", k)
        # for part in shape.part
        # print("shape.parts():", shape.parts())
        # print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                  # shape.part(1)))

        imgwithPoints = img.copy()
        for i in range(shape.num_parts):
            p = shape.part(i)
            print("p", p)
            # for x, y in set:
            imgwithPoints = cv2.rectangle(imgwithPoints, (p.x - 10, p.y - 10 ), (p.x + 10, p.y + 10), (0, 0, 255), -1)
        cv2.imwrite("pointsss" + datetime.now().strftime("%d-%m-%Y--%H-%M-%S") + ".jpg", imgwithPoints)
        m3Show.imshow(imgwithPoints, "imgwithPoints")






#
#
#
#
# def find194(img):
#     detector = dlib.get_frontal_face_detector()
#     predictor = dlib.shape_predictor
#     ("MODELS/shape_predictor_194_face_landmarks.dat")
#
#     faces = detector(img, 1)
#     # print("dets", dets)
#     # print("faces", faces)
#     # print("faces[0]", faces[0])
#     # print(enumerate(faces))
#     # print("faces", faces)
#     # faces = enumerate(faces[0])
#     # print("Number of faces detected: {}".format(len(faces)))
#     for index, data in enumerate(faces):
#         print("index, data", index, data)
#         if index == 0:
#                 # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
#                 #     k, d.left(), d.top(), d.right(), d.bottom()))
#                 # Get the landmarks/parts for the face in box d.
#                 shape = predictor(img, data)
#                 imgwithPoints = img.copy()
#                 points = []
#                 for i in range(shape.num_parts):
#                     point = shape.part(i)
#                     # print("p", p)
#                     # for x, y in set:
#                     imgwithPoints = cv2.rectangle(imgwithPoints, (point.x - 10, point.y - 10 ), (point.x + 10, point.y + 10), (0, 0, 255), -1)
#                     cv2.imwrite("pointsss" + datetime.now().strftime("%d-%m-%Y--%H-%M-%S") + ".jpg", imgwithPoints)
#                     m3Show.imshow(imgwithPoints, "imgwithPoints")
#                     points.append([point.x, point.y])
#                 return points
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def findLess(img, division, show):
#     face_landmarks_list = face_recognition.face_landmarks(img)
#     for face_landmarks in face_landmarks_list:
#         lEyeCoor = face_landmarks['left_eye']
#         rEyeCoor = face_landmarks['right_eye']
#
#         if (len(face_landmarks_list) == 0):
#
#             m3F.printRed(" found no faces in this picture")
#             plt.imshow(cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
#             plt.show()
#             return None
#             # return[m3Class.Face(noFaceImg=inputImg)]
#
#         eyesOut = []
#         for eyeLandmarkPoints in lEyeCoor, rEyeCoor:
#             xs, ys = [],[]
#             for x, y in eyeLandmarkPoints:
#                 xs.append(x)
#                 ys.append(y)
#                 print("x y ", x, y)
#             # sort x, y for min and max values, for ROI
#             xs.sort(reverse=True)
#             ys.sort(reverse=True)
#             maxX = xs[0]
#             maxY = ys[0]
#             xs.sort(reverse=False)
#             ys.sort(reverse=False)
#             minX = xs[0]
#             minY = ys[0]
#             # print("maxX,maxY,minX,minY", maxX, maxY, minX, minY)
#             margin = round((maxX - minX) * 0.2)
#             cropRect = (minX - margin, minY - margin,
#                         maxX + margin, maxY + margin)
#             cropRect = [round(division*num) for num in cropRect]
#             # for num in margin: num * division
#             img = m3F.typeSwap(img)
#             # if show:
#             # m3Show.imshow(np.asarray(img.crop(cropRect)), "cropRect")
#             upscaledLandmarks = []
#             for x, y in eyeLandmarkPoints:
#                 upscaledLandmarks.append((x * division, y * division))
#                 # y = y * division
#             # print("upscaledLandmarks", upscaledLandmarks)
#             eyesOut.append([cropRect, upscaledLandmarks])
#         # faces.append(m3Class.Face(eyes))
#     return eyesOut
#
#
#
#
#
#
#
#
#
#
# def findEyes2(photo, division=8, show=True):
#     h, w, c = photo.originalImage.shape
#     downScaledDim = ((round(w/division)), round(h/division))
#     img = photo.originalImage.copy()
#     # pil_image = Image.fromarray(copy)
#     img = cv2.resize(img, downScaledDim)
#     dimToScaleUp = division
#
#     x2smallLandmarks = findLess(img, division, True)
#     face = None
#     print(x2smallLandmarks)
#     if x2smallLandmarks is None:
#         face = m3Class.Face(noFaceImg=img)
#     else:
#         # fo
#         face.manyLandmarkPoints = find194(img)
#         print("manyLandmarkPoints", manyLandmarkPoints)



def findEyes2(photo, division, show=True):
    # downScaledDim = (round(w/100 *(scalePercent)),round(h/100 * (scalePercent)))
    h, w, c = photo.originalImage.shape
    downScaledDim = ((round(w/division)),round(h/division))
    copy = photo.originalImage.copy()
    pil_image = Image.fromarray(copy)
    inputImg = copy
    img = cv2.resize(inputImg, downScaledDim)
    dimToScaleUp = division
    detector = dlib.get_frontal_face_detector()
    dets = detector(img, 1)
    print("dets", dets)
    print("Number of faces detected: {}".format(len(dets)))
    for index, data in enumerate(dets):
        if index == 0:
            # print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
            #     k, d.left(), d.top(), d.right(), d.bottom()))
            # Get the landmarks/parts for the face in box d.
            shape = predictor(img, data)
            print("kkkk", index)
            # for part in shape.part
            # print("shape.parts():", shape.parts())
            # print("Part 0: {}, Part 1: {} ...".format(shape.part(0),
                                                    # shape.part(1)))
            points = []
            imgwithPoints = img.copy()
            for i in range(shape.num_parts):
                point = shape.part(i)
                # for x, y in set:
                imgwithPoints = cv2.rectangle(imgwithPoints, (point.x - 10, point.y - 10 ), (point.x + 10, point.y + 10), (0, 0, 255), -1)
                points.append([point.x * division, point.y * division])
            cv2.imwrite("pointsss" + datetime.now().strftime("%d-%m-%Y--%H-%M-%S") + ".jpg", imgwithPoints)
            m3Show.imshow(imgwithPoints, "imgwithPoints")
            for eye in photo.faces[0].eyes:
                cropRect = eye.cropRect
                print("cropRect", cropRect)
                for x, y in points:
                #"The box is a 4-tuple defining the left, upper, right, and lower pixel coordinate"
                    # print("x, y", x,y)

                    imgwithPoints = img.copy()
                    if (x > cropRect[0] and x < cropRect[2]):
                        if (y > cropRect[1] and y < cropRect[3]):
                            # print("in bounds x, y", x, y)
                            eye.manyLandmarkPoints.append([x, y])
                            imgwithPoints = cv2.rectangle(imgwithPoints, (x - 100, y - 100 ), (x + 100, y + 100), (0, 0, 255), -1)
                m3Show.imshow(imgwithPoints, "in bounds! imgwithPoints")

    return photo

#predictor = dlib.shape_predictor("MODELS/shape_predictor_194_face_landmarks.dat")
# def find194(img):
