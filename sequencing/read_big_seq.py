##############################################################
# Let's say you get this file back from the sequencing company.
# You did an experiment testing random peptides on some virus within your cell culture.
# You wanted to see which peptides bind most strongly to the virus because you 
# want to make a new biological therapeutic that binds and disables the virus. 

import numpy as np 

my_seqs = np.genfromtxt('sequencereads.txt', delimiter = '\n', dtype = str)

print my_seqs.size, 'sequences in this file \n'

molecular_weight_dict = {"A":89.09, "R":174.2, "D":133.1, "N":132.12, "C":121.16, "E":147.13, "Q":146.14, "G":75.07, "H":155.15, "I":131.17, "L":131.17, "K":146.19, "M":149.21, "F":165.19, "P":115.13, "S":105.09, "T":119.12, "W":204.23, "Y":181.19, "V":117.15, "X":0.0}

def Calculate_molecular_weight(sequence):
    mw = 0
    for i in list(sequence):
        mw += molecular_weight_dict[i]
    return mw 

##NumpyMW = np.vectorize(Calculate_molecular_weight)
##
##MWs = NumpyMW(my_seqs)
##
##print 'Average MW: ', np.mean(MWs)
##print 'Standard Dev. MW: ', np.std(MWs)



###################################################
###################################################
###################################################


# The non-vectorized version not that much slower
import time
time1 = time.time()

arr = []
for i in my_seqs:
 	mw = Calculate_molecular_weight(i)
 	arr.append(mw)

print np.mean(arr)	
time2 = time.time()

print time2-time1, 'time'


























