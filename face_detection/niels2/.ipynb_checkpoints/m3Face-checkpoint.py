import cv2
from PIL import Image, ImageDraw
import face_recognition
import numpy as np
from matplotlib import pyplot as plt
import m3F


# Find all facial features in all the faces in the image

def findEyes(inputImPath):
    print("proccesing", inputImPath),

    inputIm = cv2.imread(inputImPath)

    face_landmarks_list = face_recognition.face_landmarks(inputIm)
    #print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))
    #print("face_landmarks_list type was", type(face_landmarks_list))
    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(inputIm)
    eyeImages = []
   
    if (len(face_landmarks_list) == 0):
        m3F.printRed(" found no faces in this picture")
        plt.imshow(cv2.cvtColor(inputIm,cv2.COLOR_RGB2BGR))
        plt.show()
    for face_landmarks in face_landmarks_list:

        left_eye = face_landmarks['left_eye']
        right_eye = face_landmarks['right_eye']
    
        mg = (left_eye[3][0]-left_eye[0][0])*0.2
    
        if left_eye[0][1] > left_eye[3][1]:
            # If tilted left - based on how it's seen on image
            print("tilted left")
            left = [left_eye[0][0]-mg,left_eye[2][1]-mg,left_eye[3][0]+mg,left_eye[5][1]+mg]
            right = [right_eye[0][0]-mg,right_eye[2][1]-mg,right_eye[3][0]+mg,right_eye[5][1]+mg]
            eyeImages.append(np.asarray(pil_image.crop(left)))
            eyeImages.append(np.asarray(pil_image.crop(right)))
        else:
            # If tilted right
            print("tilted right")
            left = [left_eye[0][0]-mg,left_eye[1][1]-mg,left_eye[3][0]+mg,left_eye[4][1]+mg]
            right = [right_eye[0][0]-mg,right_eye[1][1]-mg,right_eye[3][0]+mg,right_eye[4][1]+mg]
            eyeImages.append(np.asarray(pil_image.crop(left)))
            eyeImages.append(np.asarray(pil_image.crop(right)))
            
    print('eyeImages',type(eyeImages),len(eyeImages))
    return eyeImages;