def cntImgPxlSimple(inputImg1, inputImg2):
    
    rows1,cols1 = inputImg1.shape
    count1 = 0
    for i in range(rows1):
        for j in range(cols1):
            count1 += inputImg1[i,j]

    count1 = count1/255       
    print(count1)




    rows2,cols2 = inputImg2.shape
    #Pixel-count
    cntPixels2 = rows2*cols2

    count2 = 0
    for i in range(rows2):
        for j in range(cols2):
            count2 += inputImg2[i,j]
    count2 = count2/255
    print(count2)
    
    deviatingValuedPixelPer = (abs(count1-count2)/count2)*100
    overlappingValuedPixelPer = 100-deviatingValuedPixelPer


  
    print ("Percentage overlapping of valued pixels from BASECASE",overlappingValuedPixelPer)

