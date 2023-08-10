import matplotlib.pyplot as plt 
import numpy as np
import math 


x_p = [28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2] 
y_p = [42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12]
# x_n = [0]*len(x_p)
# y_p = [0]*len(y_p)
direction = 5*["North", "East", "South", "West"]

alpha = 45
# alpha = alpha * np.pi/180
alpha = np.deg2rad(45)
R= 20

################################################################################################
# ox, oy = origin
# px, py = point



# xN = x_p[0]*np.cos(alpha) - y_p[0]*np.sin(alpha)
# yN = x_p[0]*np.sin(alpha) + y_p[0]*np.cos(alpha)

# x_n[0] = [x_p[0]]
# y_n[0] = [y_p[0]+R]
x_n = [x_p[0]]
y_n = [x_p[0]+R]

qx = x_p[0] + math.cos(alpha) * (x_n[0] - x_p[0]) - math.sin(alpha) * (y_n[0] - y_p[0])
qy = y_p[0] + math.sin(alpha) * (x_n[0] - x_p[0]) + math.cos(alpha) * (y_n[0] - y_p[0])

x = [x_p[0], x_n[0], qx, 27]
y = [y_p[0], y_n[0], qy, 46]



plot1 = plt.plot(x, y, '*', color='tab:red')
plt.title('P(x,y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0, 50, 0, 60])
plt.grid()
# for i_x, i_y in zip(x, y):
#     plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.show()
    

print(qx,qy)


import math

# def rotate(origin, point, angle):
#     """
#     Rotate a point counterclockwise by a given angle around a given origin.

#     The angle should be given in radians.
#     """
#     ox, oy = origin
#     px, py = point

#     qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
#     qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
#     return qx, qy

