# Convert list of tif images to jpg

import Image

import os
from os.path import join as join2

dir = os.getcwd()

tifs = [f for f in os.listdir(dir) if f.endswith('.png')]

for i in tifs:
	Image.open( join2(dir, i)).save( join2(dir, i + '.jpg'), 'JPEG', quality=100)

	

