'''
This code extract files from a .tar or .zip folder and eventually plots graphs

The first three lines are for importing the neccessary libraries of Python 2.7 in our program

The tarfile.open() is a function from the library tarfile which just OPENS and DOES NOT READ the .tar file

It is of utmost importance that one must write the file name within inverted commas and the .tar file should be in the same directory as this 
code. Otherwise it leads to an error which says "JSOC_20160516_1282_CarrRotfix2096.tar not defined".

'tf' is simply a object name which we will use to apply other functions within the tarfile library

for loop is used with integer variable from the list of names inside the tarfile

It can be observed that the for loop begins with 1st entry rather than the usual 0th entry. This is because the namelist contains the path of directory in the 0th entry which is of no use to us. It leads to error of returning NoneType in 'fileobj'.

However, the fileobj is a object-like datatype of the file and cannot be used to plot graphs directly. Hence, we make use of the function loadtxt() of numpy library to extract all the data.

The plylab library is then used to plot the graph and label the x- and y- axes.

The pylab function show() is used outside the for loop. If used inside, it will plot all the files in different graphs. 

The commented print statements were the breakpoints by which we can check for location of any errors.
'''

import numpy as np
import pylab as pl
import tarfile 
with tarfile.open('JSOC_20160516_1282_CarrRotfix2096.tar') as tf:
	#print tf
	namelist = tf.getnames()
	#print namelist
	for i in range(1, len(namelist)):
		#print namelist[i]
		fileobj = tf.extractfile(namelist[i])
		#print fileobj
		data = np.loadtxt(fileobj)
		pl.plot(data[:,1], data[:,3], 'ro')
		pl.xlabel ('l')
		pl.ylabel ('nu')
pl.show()
