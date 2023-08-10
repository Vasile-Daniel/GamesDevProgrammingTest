import numpy as np
import matplotlib.pyplot as plt
def rotate(point, origin, degrees):
    radians = np.deg2rad(degrees)
    x,y = point
    offset_x, offset_y = origin
    adjusted_x = (x - offset_x)
    adjusted_y = (y - offset_y)
    cos_rad = np.cos(radians)
    sin_rad = np.sin(radians)
    qx = offset_x + cos_rad * adjusted_x + sin_rad * adjusted_y
    qy = offset_y + sin_rad * adjusted_x + cos_rad * adjusted_y
    return qx, qy
R = 20
origin=(28,42)
PointA=(28,42+R)


NewPointA=rotate(PointA,origin,45)

NewPointA = np.atleast_2d(NewPointA)
origin = np.atleast_2d(origin)
PointA= np.atleast_2d(PointA)

print(NewPointA[0][0],NewPointA[0][1])
x = [origin[0][0],PointA[0][0], 27, NewPointA[0][0]]
y = [origin[0][1],PointA[0][1], 46, NewPointA[0][1]] 

plt.plot(x,y, '*', color='tab:red')
plt.axis([0, 50, 0, 70])
plt.grid()
plt.show()

