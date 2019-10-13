import PIL
from matplotlib import pyplot as plt

# http://ozzmaker.com/add-colour-to-text-in-python/
def printRed(stringarr):
    #prstr = ""
    #for el in stringarr:
    #    prstr + str(el)
    prstr = "\033[1;41;39m" + stringarr + "\]"
    print(prstr)
    
def printGreen(stringarr):
    prstr = "\033[1;42;39m" + stringarr + "\]"
    print(prstr)

def printBlue(stringarr):
    prstr = "\033[1;44;39m" + stringarr + "\]"
    print(prstr)
    
    
    
    
    
    
# https://pythontic.com/image-processing/pillow/histogram
def getRed(redVal):
    return '#%02x%02x%02x' % (redVal, 0, 0)

def getGreen(greenVal):
    return '#%02x%02x%02x' % (0, greenVal, 0)

def getBlue(blueVal):
    return '#%02x%02x%02x' % (0, 0, blueVal)

def gHist(imagePath):
    #print(type(imagePath))
    pimg = PIL.Image.fromarray(imagePath)
    hist = pimg.histogram();
    #plt.hist(hist,bins=256)
    plt.figure(0)
    for i in range(0, 256):
        plt.bar(i, hist[i], alpha=0.3)
    plt.show()
