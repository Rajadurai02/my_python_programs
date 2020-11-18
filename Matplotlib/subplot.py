import matplotlib.pyplot as plt 
import numpy as np 
#sub plot that uses to draw multilple plots in ine figure
#that takes two parameters (row,column,index)
#and i also add title that adds tiltle to the plots
#supertitle that adds single entire title
#plot 1
x = np.array([0,1,2,3,4,5])
y = np.array([0,2,4,6,8,10])
plt.subplot(3,2,1)
plt.plot(x,y)
plt.title('Multiple  of 2')
#plot 2
x = np.array([0,1,2,3,4,5])
y = np.array([0,3,6,9,12,15])
plt.subplot(3,2,2)
plt.plot(x,y)
plt.title('Multiple  of 3')
#plot 3
x = np.array([0,1,2,3,4,5])
y = np.array([0,4,8,12,16,20])
plt.subplot(3,2,3)
plt.plot(x,y)
plt.title('Multiple  of 4')
#plot 4
x = np.array([0,1,2,3,4,5])
y = np.array([0,5,10,15,20,25])
plt.subplot(3,2,4)
plt.plot(x,y)
plt.title('Multiple  of 5')
#plot 5
x = np.array([0,1,2,3,4,5])
y = np.array([0,6,12,18,24,30])
plt.subplot(3,2,5)
plt.plot(x,y)
plt.title('Multiple  of 6')
#plot 6
x = np.array([0,1,2,3,4,5])
y = np.array([0,7,14,21,28,35])
plt.subplot(3,2,6)
plt.plot(x,y)
plt.title('Multiple  of 7')
plt.suptitle('Multiples')
plt.show()