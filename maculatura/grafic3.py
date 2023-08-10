import matplotlib.pyplot as plt 
import numpy as np


x = [28, 28]
y = [42, 48] 

plt.plot(x,y, '*', color='tab:red')
plt.axis([0, 50, 0, 60])
plt.show()