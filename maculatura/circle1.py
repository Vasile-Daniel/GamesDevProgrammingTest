import matplotlib.pyplot as plt
import numpy as np
import math 
angle1 = 45 
angle = (angle1*np.pi)/180
R = 20 

x0 = 28
y0 = 42

x = 28
y = 42 + R  

x2 = 27
y2 = 46

pox =  x - x0
poy =  y - y0 

x1 = x0 + np.cos(angle) * pox - np.sin(angle) * poy 
y1 = y0 + np.sin(angle) * pox + np.cos(angle) * poy

X = [x0, x, x1, x2]
Y = [y0, y, y1, y2]


def calculate_angle(p1, p2, p3):
    # Calculate the vectors between the points
    v1 = [p1[0] - p2[0], p1[1] - p2[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    # Calculate the dot product of the vectors
    dot_product = v1[0] * v2[0] + v1[1] * v2[1]
    # Calculate the magnitude of the vectors
    mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
    mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
    # Calculate the angle between the vectors in radians
    angle = math.acos(dot_product / (mag_v1 * mag_v2))
    # Convert the angle to degrees and return it
    return math.degrees(angle)
# Example usage
p1 = [X[1],Y[1]]
p2 = [X[0], Y[0]]
p3 = [X[2], Y[2]]
angle1 = calculate_angle(p1, p2, p3)
print(angle1) # Output: 90.0

plt.plot(X,Y, '*', color='tab:red')
plt.axis([0, 50, 0, 70])
plt.axis('equal')
plt.grid()
for i_x, i_y in zip(X, Y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.show()
