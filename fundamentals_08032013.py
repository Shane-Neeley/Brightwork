# All the images are on a public dropbox folder that is going to self destruct in 7 days.
# Use pythonanywhere's servers to host this folder, so the script can run on the cloud.
# Why is it going to self-destruct in 10 days? For one, I wanted to see if I can do it. For 2, incase some
# robot decides to download it over and over all day long, sapping my dropbox bandwidth.

# Convention for numpy use
import numpy as np

# Lets create an array

my_array = np.array( [0,1,2,3] )

# hit enter, you see the array printed

# learn some things about your array

my_array.dtype
len(my_array)

# integer, 64 bit is the data type of the objects in your array

# you can change those into strings, in case you use them as text or something

str_array = my_array.astype(str)

# to see the differences in these arrays

for i in my_array:
	print i*4

for i in str_array:
	print i*4

# This was basically a python list. Numpy is more useful for multidimensional arrays.
# Which sounds like a fancy word, but basically we just mean a table, dataset, rows/columns of values.
# I will stick to 1, 2 and 3 dimensional arrays. One just a list, or one row / column of data.
# 2 dimensions would be a table of data. And 3 dimensions is most often seen in an image like RGB, where you pixels, which are in rows / columns.
# But those pixels are themselves made of an array of 3 values R,G and B.

dim2_array = np.array([[0,1,2,3], [0,1,2,3], [0,1,2,4]])

dim2_array.ndim
dim2_array.shape
dim2_array.size

# When doing math on an array, you can choose to do the whole thing, or line by line.
np.mean(dim2_array)
np.mean(dim2_array, axis = 0)
np.mean(dim2_array, axis = 1)

# Easy to forget, but very important is indexing these arrays. 
dim2_array[:]
dim2_array[:2]
dim2_array[:2,:]
dim2_array[:2,:2]
dim2_array[0][::-1]

# more dimensions and data get confusing to look at. And doing math, you get lots of sig figs.
dim2_array = np.array([[0.002002020203020,1,2.83893289239832,3.3243283293], [0.32323222,10000000000000,2,3], [0,1,2,300000000000000000000]])
# What is that again??

# So a little unix lesson is always helpful..
# Note to shane... try canopy on windows for this

ls 
cd Desktop/Temps

# I do this a lot
# use numpy's ability to save your array as a csv file, then look at it in excel.

np.savetxt('lookatarray.csv', dim2_array, delimiter = ',')

# While were in excel, let me show you genfromtxt.
# Lets edit something in excel

# Show tab completion in iPython for np.gen
np.genfromtxt('lookatarray', delimiter = ',')

# NAs and NANs come up often when there is missing data.

arr = np.array([0,7,1,8, np.nan])
np.mean(arr)

# You have to make it into a masked array in order to do math with nans
# Show tab completion in iPython for np.ma.
arr2 = np.ma.masked_array(arr, np.isnan(arr))
np.mean(arr2)


#########################################################
#########################################################
#########################################################
# These scientific libraries have many function. Finance for example 

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import numpy as np

today = date.today()

# Wait, what does this do again? How do you use it. You could go to google, or just:
?quotes_historical_yahoo
# Ok so it takes 2 dates and returns the info on the stock between that
# Oh see theres a function parse_yahoo_historical that will tell you how it works. 
?parse_yahoo_historical
# Ok it is    d, open, close, high, low, volume

# If thats not enough info and you wan't the source code.
??quotes_historical_yahoo

start_date = (today.year -1, today.month, today.day)

year_of_data = quotes_historical_yahoo('TICKER', start_date, today)

# try indexing it, you get some error. Oh its not a numpy array...weird.

COWyear = quotes_historical_yahoo('cow', start_date, today)

DOGyear = quotes_historical_yahoo('dog', start_date, today)

COWyear = np.array(COWyear)

DOGyear = np.array(DOGyear)

COWcloses = COWyear[:,2]

DOGcloses = DOGyear[:,2]

plt.clf()

plt.subplot(211)
plt.plot(COWcloses, 'ro')
plt.subplot(212)
plt.plot(DOGcloses, 'bo')

 





