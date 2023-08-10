import numpy as np
import matplotlib.pyplot as plt 

x_origin = [28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2] # see img 1
y_origin = [42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12] # see img 1
direction = 5*("North", "East", "South", "West") # see img 1
points =zip(x_origin, y_origin,direction)
# print(set(points))
points =list(points)
# print(points)
# points
nr = list(range(1,21))
# print(nr)
len_x = len(x_origin)

S = [(39, 36), (41, 34)]
# print(S[1])
M = np.atleast_2d(S)
# print(M)

# matrix = np.atleast_2d(list(zip(nr,x_origin,y_origin,direction)))
matrix = list(zip(nr,x_origin,y_origin,direction))
# print(matrix)

# for i in matrix:
#     print(matrix[i])
for i in range(len(matrix)):
    for j in range(len(S)):
        if (S[j] == matrix[i][1:3]) :
            print(matrix[i])