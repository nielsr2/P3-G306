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


class Face:
    path = ""
    images = []
    eyes = []
    originalImage = None
    mask = None
    wip = None
    noFaceImg = None
    def __init__(self, eyes=None, noFaceImg=None):
        self.eyes = eyes
        self.noFaceImg = noFaceImg

class Eye:
    image = None
    coordinates = None
    landmarkPoints = None
    circle = None
    mask = None
    polyMask = None
    polyMaskedImage = None
    # **********************************************************************
    # wip = work in progress
    wip = None
    def __init__(self, im="None", coor="None", landmarkPoints="None"):
        self.image = im
        self.coordinates = coor
        self.landmarkPoints = landmarkPoints
        self.wip = np.copy(self.image)
