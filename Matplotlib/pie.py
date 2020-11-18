import matplotlib.pyplot as plt 
import numpy as np 
#using pie 
#it uses the formula x/sum(x) to draw 
x = np.array([24,67,86,12])
plt.pie(x)
plt.show()

#using labels
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']
plt.pie(x,labels = label)
plt.show()

#changing angles using startangle
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']
plt.pie(x,labels = label,startangle = 90)
plt.show()

#cut a specified area using explode
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']
myexplode = [0.2,0.1,0,0]
plt.pie(x,labels = label,explode = myexplode)
plt.show()

#using shadows
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']
myexplode = [0.2,0.1,0,0]
plt.pie(x,labels = label,explode = myexplode,shadow=True)
plt.show()

#changing colors
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']
myexplode = [0.2,0.1,0,0]
color = ['red','blue','hotpink','yellow']
plt.pie(x,labels = label,explode = myexplode,colors = color)
plt.show()


#title and legend
x = np.array([24,67,86,12])
label = ['orange','apple','mango','banana']

plt.pie(x,labels = label)
plt.legend(title = 'Fruites')
plt.show() 