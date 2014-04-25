
# cell pics from http://www.cellimagelibrary.org/groups/9070
# augmented in photoshop for effect

import numpy as np 
import matplotlib.pyplot as plt 
import os

cwd = os.getcwd()

image_dir = os.path.join(cwd, 'image_timeseries')

# Show how the paths work

# need to do this list comprehension because of ds_Store
files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]

redperimage = []
greperimage = []

# Show what an image array looks like. A plt.imread then look through i, k, print k

for image in files:
	
	img = plt.imread( os.path.join( image_dir, image))
	reds = img[:,:,0]
	redperimage.append( np.sum(reds))
	greens = img[:,:,1]
	greperimage.append( np.sum(greens))

redperimage = np.array(redperimage, dtype = float)
greperimage = np.array(greperimage, dtype = float)

ratio = redperimage / greperimage

plt.subplot(211)
# since this X is number of image you can write [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
plt.plot(range(0, len(redperimage)), redperimage, 'ro')
plt.plot(range(0, len(greperimage)), greperimage, 'go')

plt.subplot(212)
plt.plot(range(0, len(ratio)), ratio, 'ko')

plt.show()


	








		

