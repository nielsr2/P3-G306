class Immer:
    path = ""
    images = []
    eyes = []
    orginalImage = None
    mask = None

    def __init__(self, orginalImage="None", path="None"):
        self.orginalImage = orginalImage
        self.path = path


class Eye:
    image = None
    coordinates = None
    landmarkPoints = None
    circle = None
    mask = None
    polyMask = None
    polyMaskedImage = None

    def __init__(self, im="None", coor="None", landmarkPoints="None"):
        self.image = im
        self.coordinates = coor
        self.landmarkPoints = landmarkPoints
