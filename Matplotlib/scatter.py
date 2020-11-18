import matplotlib.pyplot as plt 
import numpy as np 
#using sactter
x = np.array([2,4,6,8,9,1,3,5,7,3])
y = np.array([20,40,56,45,67,86,47,93,27,96])
plt.scatter(x,y)
plt.show()
#with four datas
x = np.array([2,4,6,8,9,1,3,5,7,3])
y = np.array([20,40,56,45,67,86,47,93,27,96])
plt.scatter(x,y,color = 'red')

x = np.array([2,4,6,8,9,1,3,5,7,3])
y = np.array([80,20,65,54,76,68,78,34,73,60])
plt.scatter(x,y,color='blue')
plt.show()

#every one with different color and differnt size
x = np.array([2,4,6,8,9,1,3,5,7,3])
y = np.array([20,40,56,45,67,86,47,93,27,96])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown"])
sizes = np.array([5,5,10,20,50,16,4,9,10,30,])
plt.scatter(x,y,c = colors,s = sizes)
plt.show()

#color map
x = np.array([2,4,6,8,9,1,3,5,7,3])
y = np.array([20,40,56,45,67,86,47,93,27,96])
colors = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
plt.scatter(x,y,c = colors,cmap = 'nipy_spectral')
plt.colorbar()
plt.show()

#random values with alpha value
x = np.random.randint(100,size = 100)
y = np.random.randint(100,size = 100)
colors = np.random.randint(100,size = 100)
size = 10 * np.random.randint(100,size = 100)
plt.scatter(x,y,c = colors,s = size,cmap = 'rainbow',alpha = 0.5)
plt.colorbar()
plt.show()