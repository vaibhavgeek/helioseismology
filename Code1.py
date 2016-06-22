import numpy as np			#create object of numpy library
import pylab as pl			#create object of pylab library
data = np.loadtxt('data.txt')		#loading the data in text format into Python. The file should be in same folder as this code.
pl.plot(data[:,1], data[:,3])		#The numbers represent the column numbers in our data which are to be plotted on x- and y- axis 					respectively
pl.xlabel('l')				#Labelling the x- axis by variable plotted on it	
pl.ylabel('nu')				#Labelling the y- axis by variable plotted on it
pl.show()				#Using show function to create an image of graph plotted in Python
