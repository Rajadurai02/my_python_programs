import matplotlib.pyplot as plt 
import numpy as np 
x = np.array(['A','B','C','D'])
y = np.array([10,20,30,40])
plt.bar(x,y)
plt.show()
# turning into horizontal
 
x = np.array(['A','B','C','D'])
y = np.array([10,20,30,40])
plt.barh(x,y)
plt.show()


#changing color
x = np.array(['A','B','C','D'])
y = np.array([10,20,30,40])
plt.bar(x,y,color = 'green')
plt.show()

#changing width
x = np.array(['A','B','C','D'])
y = np.array([10,20,30,40])
plt.bar(x,y,width = 0.5)
plt.show()