from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import time
import scipy.misc
import matplotlib.image as mpimg
from scipy.ndimage import filters
import os
import urllib
import copy


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''
    Timeout function for when retreiving images
    From:
    http://code.activestate.com/recipes/473878-timeout-function-using-threading/
    '''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return False
    else:
        return it.result

def fetch_picture(url,name):
    '''
    Does a thing
    '''
    testfile = urllib.URLopener()
    timeout(testfile.retrieve, (url, url[-15:]), {}, 500)

    if os.path.isfile(url[-15:]):
        #remove corrupt file
        if os.path.getsize(url[-15:]) <= 1024:
            return False
        else:
            #return True
            #resizing image
            try:
                image = imread(url[-15:])     
                #height = image.shape[0]
                #width = image.shape[1]
                
                #goal_height = 125
                #scalar = float(height)/goal_height
                #image = scipy.misc.imresize(image, (
                    #int(ceil(height/scalar)),
                    #int(ceil(width/scalar))))
                scipy.misc.imsave(name+'.jpg', image)    
                os.remove(url[-15:])                
                return True
            except:
                return False

    return False

#def resize(image, size):
    #os.chdir('./categoryPictures')
    #img = scipy.misc.imread(image)
    #img = scipy.misc.imresize(img,(size,size))
    #imsave(image[:-4]+'large.jpg', img)
    
def do():
    pass
    #for cat in dog_cat:
         #Fetch cat name from main
         #get first working from url, name after cat name
         
def slim_categories():
    txt = open("cat_mapping.txt", "w")
    cat_map = {}
    count = 0
    for i in open("wnid-dog.txt"):
        for line in open("wnid-name.txt"):
            if i[1:10] in line:
                split = line.split("\t")
                split[1] = split[1][:-1]
                split.insert(1,"***")
                txt.write(str(split)  + '\n')
                cat_map[split[0]] = split[2]
                break
        count += 1
    return cat_map

def get_category_pictures():
    #str = "['n02102040', '***', 'English springer, English springer spaniel']"
    #lista = str.split("***")
    #first = lista[0][2:-4]
    #second = lista[1][4:-2]
    base_url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid="
    count = 1
    for c in open("cat_mapping.txt"):
        lista = c.split("***")
        wnid = lista[0][2:-4]
        name = lista[1][4:-3]
        html = urllib.urlopen(base_url+str(wnid))
        for line in html:
            if (fetch_picture(line.strip(),name)):
                print (count)
                count += 1
                break

#http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02095412
#Get images for wnid    

if __name__=='__main__':
    print("start")
    txt = open("cat_mapping.txt")
    #os.chdir('./categoryPictures')
    #fetch_picture('http://static.flickr.com/116/258440999_51087a78ff.jpg')