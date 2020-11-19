import matplotlib.pyplot as plt 
import numpy as np 
y = np.array([12,34,56,7,8])
#changing line style using linestyle / ls
plt.plot(y,linestyle='dashed')
plt.show()
#changing color and width using color / c  |  linewidth / lw
plt.plot(y,linestyle = '-.',color = 'hotpink',linewidth = 10)
plt.show()