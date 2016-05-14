# Code for plotting graphs using already existing data files

import numpy as np            #creating objects of the numpy library
import pylab as pl            #creating objects of the pylab library
data = np.loadtxt('Data.txt') #using the 'loadtxt' function to read a file  
                              #The file mentioned above must be located in the same folder as this code. 
                              #And the file extension should be .txt only. The name could be anything you wish
pl.plot(data[:,1], data[:,3]) #The numbers represent the columns in our Data to be plotted on x- and y- axis respectively
pl.xlabel('l')                #Labelling the x-axis by the variable name plotted on x-axis
pl.ylabel('nu')               #Labelling the y-axis by the variable name plotted on y-axis
pl.show()                     #Using the show function to create image of graph plotted using python 2.7
