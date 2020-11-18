import matplotlib.pyplot as plt 
import numpy as np 
#histogram example is there are 250 people heights and that is some how 20 poeple have height 170 like that that converts into data 
#we use random function to generate people heights 
#this is called noramal distribution parameters (range,standard deviation,size)
x = np.random.normal(170,10,250)
plt.hist(x)
plt.show()