import cv2 

#InputImg2 has to be equal to handmade mask. 
def cntImgPxl (inputImg1, inputImg2): 
    
    
    
    inputImg1 = cv2.imread("15.jpg_0hardedge.jpg",0)
    inputImg2 = cv2.imread("15.jpg_0softedge.jpg",0)

    ret,binary1 = cv2.threshold(inputImg1,127,255,cv2.THRESH_BINARY)
    ret,binary2 = cv2.threshold(inputImg2,127,255,cv2.THRESH_BINARY)


    rows1,cols1 = inputImg1.shape

    for i in range(rows1):
        for j in range(cols1):
            k = inputImg1[i,j]
            #Non-black pixels
            cntNotBlack1 = cv2.countNonZero(binary1)
            #Pixel-count
            cntPixels1 = rows1*cols1
            #Black-pixels
            cntBlack1 = cntPixels1 - cntNotBlack1


    rows2,cols2 = inputImg2.shape

        for i in range(rows2):
            for j in range(cols2):
            k = inputImg2[i,j]
            #Non-black pixels
            cntNotBlack2 = cv2.countNonZero(binary2)
            #Pixel-count
            cntPixels2 = rows2*cols2
            #Black-pixels
            cntBlack2 = cntPixels2 - cntNotBlack2
        

    pixelPercentage = (cntBlack2/cntBlack1)*100

    print (cntNotBlack1)
    print (cntNotBlack2)
    print (cntPixels1)
    print (cntPixels2)
    print (cntBlack1)
    print (cntBlack2)
    print (pixelPercentage)
    
    return (pixelPercentage)



        

   

