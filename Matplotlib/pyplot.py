import matplotlib.pyplot as plt 
import numpy as np 
x = np.array([1,2,3,4,5])
y = np.array([4,8,2,6,20])

#ploting with line
plt.plot(x,y)
plt.show()

#plotting without line
plt.plot(x,y,'o')
plt.show()

#without x axis
plt.plot(y)
plt.show()