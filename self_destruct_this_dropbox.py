import os
from datetime import date
import time
import subprocess

this_folder = os.getcwd()
# This folder is in my pythonanywhere server. And is a public folder.

# See http://stackoverflow.com/questions/12280143/how-to-move-to-one-folder-back-in-python/17726833#17726833
back_one_folder = os.path.normpath(this_folder + os.sep + os.pardir)

destruct = False

destruct_call = ('rm -r %s' % this_folder).split()

while destruct == False:
	
	today = date.today()
	
	if str(today) == '2013-08-10':
		print 'SelfDestructing'
		subprocess.call( destruct_call )	
		destruct = True

	
	else:
		print 'alive for another 12 hours'
		time.sleep(43200)   #43200 seconds = 12 hours









