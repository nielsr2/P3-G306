#!/usr/bin/python


import sys
import getopt
import cv2 as cv


def main(argv):
    print(argv[0])
    print("TRALALALAL")
    image = cv.imread(argv[0])
    (h, w) = image.shape[:2]
    # edges = cv.Canny(image, (h, w), 20, 40)
    edges = cv.Canny(image, 100, 200)
    cv.imwrite(
        "/Users/n/School/MED3/P3/Code/P3-G306/face_detection/niels2/photoshop/" + "canny.jpeg", edges)
    # imageOut = cv2.canny


if __name__ == "__main__":
    main(sys.argv[1:])
