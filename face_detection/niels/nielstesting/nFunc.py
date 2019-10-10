import cv2
import numpy as np

def ntest(str):
    print("Niels:", str)
    return;

webcamBool = False;
cap = None;
frame2 = None;
def initWebcam():
    webcamBool = True;
    cap = cv2.VideoCapture(0)
    while webcamBool:
        _, frame = cap.read()
        frame = np.asarray(frame)
        frame2 = frame
    return;
