# from pylab import *
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.cbook as cbook
# import time
# import scipy.misc
# import matplotlib.image as mpimg
# from scipy.ndimage import filters
# import os
# import urllib
# import copy
#
#
# def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
#     '''
#     Timeout function for when retreiving images
#     From:
#     http://code.activestate.com/recipes/473878-timeout-function-using-threading/
#     '''
#     import threading
#     class InterruptableThread(threading.Thread):
#         def __init__(self):
#             threading.Thread.__init__(self)
#             self.result = None
#
#         def run(self):
#             try:
#                 self.result = func(*args, **kwargs)
#             except:
#                 self.result = default
#
#     it = InterruptableThread()
#     it.start()
#     it.join(timeout_duration)
#     if it.isAlive():
#         return False
#     else:
#         return it.result
#
# def fetch_picture(url):
#     '''
#     Does a thing
#     '''
#     testfile = urllib.URLopener()
#     timeout(testfile.retrieve, (url, url[-15:]), {}, 500)
#
#     if os.path.isfile(url[-15:]):
#         #remove corrupt file
#         if os.path.getsize(url[-15:]) <= 1024:
#             return False
#         else:
#             return True
#             #resizing image
#             #try:
#                 #image = scipy.misc.imread(url)
#                 #image_data = (open(url, 'rb').read())
#                 #image = scipy.misc.imresize(image,(size,size))
#                 #imsave(image[:-4]+'large.jpg', img)
#                 #os.remove(filename)
#                 #print filename
#                 #i += 1
#             #except:
#                 #return -1
#
#     return False
#
# def resize(image, size):
#     os.chdir('./imagenet')
#     img = scipy.misc.imread(image)
#     img = scipy.misc.imresize(img,(size,size))
#     imsave(image[:-4]+'large.jpg', img)
#
