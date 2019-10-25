#

m3-functions

notebooks

pics


# FUNCTION GUIDELINES

* First parameter must for an image (ndarray). The parameter should be called 'inputImg'
* Last parameter have boolean parameter to print the processed pictures in notebook, called 'show'

* if you import one of our other modules (like m3F) within another module (like m3Batch), do it like this: from . import m3F'


# TODOS

* FACE DETECTION -  Make new folder in eyes with the name of input set

# PIPELINES

# 1
Retinex -> median blur -> only R-channel -> structure extraction / denoising -> Hough
