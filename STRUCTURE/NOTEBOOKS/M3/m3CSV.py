# TP, FN, FP

import csv
def makeCSV(photoArray, fileToSave):
    with open(fileToSave, 'w', newline='') as csvfile:
        fieldnames = ['image_name','eye','noCircles', 'TP', 'FN', 'FP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for photo in photoArray:
            for face in photo.faces:
                eyeCount = 0
                for eye in face.eyes:
                    writer.writerow({'image_name': photo.path, 'eye': eyeCount, 'noCircles': eye.noCircles, 'TP': eye.TP, 'FN': eye.FN, 'FP': eye.FP })
                    eyeCount += 1
