import numpy as np 
import matplotlib.pyplot as plt 
import os

# Show the matplotlib gallery

cwd = os.getcwd()
tmsrs = np.genfromtxt("A10Bleb_pct_chg_smoothed.csv", delimiter = ',')

# check out tmsrs.shape

if not os.path.exists( os.path.join(cwd, 'figs')):
	os.makedirs( os.path.join(cwd, 'figs'))
figdir = os.path.join(cwd, 'figs')	

# Come in handy to name the figures in the loop
nums = xrange(0, tmsrs.shape[1])

# for i in tmsrs: print i  #to see how each item is a row, which = 375 entries. 
# plt.plot(tmsrs)
# plt.plot(tmsrs.T)
# plt.plot(tmsrs.T * -1)

# timepoint5 = tmsrs.T[5]

# length = timepoint5.shape[0]

for timepoint, num in zip(tmsrs.T, nums):
	length = timepoint.shape[0]
	myrange = range(1, length+1)
	fig = plt.figure()

	# google how do I turn off matplotlib axis. How do I set limits matplotlib axes.
	ax = plt.Axes(fig, [0., 0., 1., 1.])
	ax.set_axis_off()
	fig.add_axes(ax)
	#uncomment xlim first
	plt.xlim([0, 100])

	ax.text(0, 1, '    # 1', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 2, '    # 2', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 3, '    # 3', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 4, '    # 4', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 5, '    # 5', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 6, '    # 6', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 7, '    # 7', color = 'r', size = 15, verticalalignment='center')
	ax.text(0, 8, '    # 8', color = 'r', size = 15, verticalalignment='center')

	timepoint = timepoint * -1

	plt.barh(myrange, timepoint, color = 'k', align = 'center')

	plt.title("Watch them grow")
	plt.xlabel("Signal")

	plt.savefig( os.path.join(figdir, 'timepoint_%s.png' %num) )
	
	plt.close()

	print num




