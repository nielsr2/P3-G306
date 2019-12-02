import numpy as np


class Photo:
    originalImage = None
    path = None
    faces = []
    mask = None
    def __init__(self, originalImage="None", path="None"):
        self.originalImage = originalImage
        self.path = path
        self.mask = None

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Face:
    path = ""
    images = []
    eyes = []
    originalImage = None
    mask = None
    wip = None
    noFaceImg = None
    def __init__(self, eyes=[], noFaceImg=None):
        self.eyes = eyes
        self.noFaceImg = noFaceImg

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)


class Eye:
    image = None
    coordinates = None
    landmarkPoints = None
    circle = None
    mask = None
    polyMask = None
    houghOutline = None
    polyMaskedImage = None
    # **********************************************************************
    # wip = work in progress
    wip = None
    # **********************************************************************
    iris = None
    def __init__(self, im="None", coor="None", landmarkPoints="None"):
        self.image = im
        self.coordinates = coor
        self.landmarkPoints = landmarkPoints
        self.wip = np.copy(self.image)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

#
# class Iris:
#     originalImage = None
#     circles = None
#     irisFromMask = None
#
#     def __init__(self, originalImage, irisFromMask):
#         originalImage = originalImage
#         irisFromMask = irisFromMask
