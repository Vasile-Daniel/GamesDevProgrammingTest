import math
import numpy as np
import matplotlib.pyplot as plt
def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


R = 20
origin=(28,42)
point=(28,42+R)


NewPointA=rotate(origin, point, math.radians(45))

NewPointA = np.atleast_2d(NewPointA)
origin = np.atleast_2d(origin)
point = np.atleast_2d(point)

print(NewPointA[0][0],NewPointA[0][1])
x = [origin[0][0],point[0][0], 27, NewPointA[0][0]]
y = [origin[0][1],point[0][1], 46, NewPointA[0][1]] 

plt.plot(x,y, '*', color='tab:red')
plt.axis([0, 50, 0, 70])
plt.grid()
plt.show()