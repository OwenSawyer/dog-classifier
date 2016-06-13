from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import time
import scipy.misc
import matplotlib.image as mpimg
from scipy.ndimage import filters
import os
def resize(image, size):
    os.chdir('./imagenet')
    img = scipy.misc.imread(image)                          
    img = scipy.misc.imresize(img,(size,size))
    imsave(image[:-4]+'large.jpg', img)