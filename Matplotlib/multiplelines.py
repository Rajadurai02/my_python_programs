import matplotlib.pyplot as plt 
import numpy as np 
x1 = np.array([1,2,3,4,5])
x2 = np.array([2,6,8,9,10])
y1 = np.array([1,4,3,4,6])
y2 = np.array([5,8,4,6,2])

#just using default x value
plt.plot(y1)
plt.plot(y2)
plt.show()

#using four values as a single plot
plt.plot(x1,y1,x2,y2)
plt.show()