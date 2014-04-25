#############################################################
#############################################################
#############################################################
# Where vectorization really counts is in multidimensional arrays, like images.

import time
import matplotlib.pyplot as plt 

image = plt.imread("img_0001.jpg")

# We think the low green values are actually non-specific, background noise. 
# Lets look at the image without it. 
# Make anything in the green channel less than 40 be a zero

time1 = time.time()

## Built in vectorized functions
image[ image[:,:,1] < 40 ] = 0

# ASIDE: INDEXING WITH TRUTH ARRAYS
#############################
# a = np.array([[1,2,3],[4,5,6]])
# a >=3
# a[ a>=3 ]
#############################

time2 = time.time()

timevec = (time2 - time1)
print 'time for vectorized: ', timevec


################ Loop ##########

time3 = time.time()

for i in xrange(0, image.shape[0]):
	for k in xrange(0, image.shape[1]):
		if image[i,k,1] < 40:
				image[i,k,1] = 0

time4 = time.time()

timeloop = (time4 - time3)
print 'time for loops: ', timeloop

print 'vectorized is', (timeloop / timevec), 'times faster'

plt.imshow(image)
plt.show()


# thats the difference in your code taking a month to run, or a few hours.

