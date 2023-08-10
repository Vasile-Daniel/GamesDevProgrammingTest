import matplotlib.pyplot as plt 
import numpy as np

arrX = [28, 27, 16, 40, 8, 6, 28, 39, 12, 36,22, 33,41, 41, 14,6, 46,17,28,2] 
arrY = [42, 46, 22,50, 6, 19, 5, 36, 34, 20, 47,19, 18,34, 29, 49, 50, 40, 26, 12]
direction = 5*["North", "East", "South", "West"]
givenP = zip(arrX,arrY)
beta = 45
beta1 = beta * np.pi/180
RR = 28.3

def rotate(p, origin=(0, 0), degrees=0):
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle),  np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T-o.T) + o.T).T)


points=[(28, 28+RR)]

origin=(28, 42)

new_points = rotate(points, origin=origin, degrees=45)
x = [new_points[0]]
x = [new_points[1]]
print(new_points)

