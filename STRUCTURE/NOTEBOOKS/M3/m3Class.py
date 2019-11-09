import numpy as np


class Photo:
    originalImage = None
    path = None
    faces = None
    mask = None
    def __init__(self, orginalImage="None", path="None"):
        self.orginalImage = orginalImage
        self.path = path


class Face:
    eyes = []

    def __init__(self, eyes="None"):
        self.eyes = eyes

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
