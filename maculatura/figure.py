import matplotlib.pyplot as plt
import numpy as np 
import math 

R = 20
origin = [28,42]
point = [origin[0], origin[1]+R]

x = [origin[0], point[0]]
y = [origin[1], point[1]]

unghi = []
x = []
y = []
for i in range(0,360, 10):
    
    angle = np.deg2rad(i) # angle = np.pi*i/180 
    unghi.append(angle)


    opx = (point[0] - origin[0])
    opy = (point[1] - origin[1])

    qx = origin[0] + np.cos(angle) * opx  - np.sin(angle) * opy
    qy = origin[1] + np.sin(angle) * opx + np.cos(angle) * opy

    x.append(qx)
    y.append(qy)

x.append(origin[0])
y.append(origin[1])

print(unghi)

print(angle)
plt.plot(x,y, '*', color = 'red')
plt.grid()
plt.show()