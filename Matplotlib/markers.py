import matplotlib.pyplot as plt 
import numpy as np 
y = np.array([23,45,67,89,1])
#using marker with line d for diamand as well many of these are here
plt.plot(y,marker = 'D')
plt.show()

#changing color appereance of line and marker is stated as marker/line/color
plt.plot(y,'*-.g')
plt.show()
# we change marker size,facecolor,edgecolor using ms,mfc,mec
plt.plot(y,'<-.b',ms = 20,mec = 'green',mfc = 'red')
plt.show()