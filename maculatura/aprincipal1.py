import matplotlib.pyplot as plt 
import numpy as np 
import math

x_origin = [28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2] 
y_origin = [42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12]
# direction = 5*["North", "East", "South", "West"]
direction = 5*["North", "East", "South", "West"]

len_x = len(x_origin)
angle = 45
R = 20 
# angle = np.deg2rad(angle) #  angle = angle*np.pi/180  
id = [] # number 

for i in range(1,len_x+1):
    id.append(i)

matrix = np.zeros((len_x,4))
matrix = np.array(matrix, dtype=object)
for i in range(len_x):
    matrix[i][0] = id[i]
    matrix[i][1] = x_origin[i]
    matrix[i][2] = y_origin[i]
    matrix[i][3] = direction[i]

        
def VisiblePoints(id,angle,R):
    obj = matrix[id-1]
    print(obj)
    ox = obj[1]
    oy = obj[2]

    if (obj[3] == "North"):
        px = obj[1]
        py = obj[2]+R
        print(obj[3])
    elif (obj[3] == "West"):
        px = obj[1]-R
        py = obj[2]
        print(obj[3])
    elif (obj[3] == "South"):
        px = obj[1]
        py = obj[2]-R
        print(obj[3])
    elif (obj[3] == "East"):
        px = obj[1]+R
        py = obj[2]
        print(obj[3])
    
    pox =  ox  - px 
    poy =  oy  - py

    qx1 = ox - np.cos(angle) * pox + np.sin(angle) * poy 
    qy1 = oy - np.cos(angle) * poy - np.sin(angle) * pox 

    x = [ox, px, qx1, 27] 
    y = [oy, py, qy1, 46]

    return x,y 

x, y = VisiblePoints(1,angle,R)

print(x)


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
p1 = [x[1],y[1]]
p2 = [x[0], y[0]]
p3 = [x[2], y[2]]
angle1 = calculate_angle(p1, p2, p3)
print(angle1) # Output: 90.0

plt.plot(x,y, '*', color='tab:red')
plt.axis([0, 50, 0, 70])
plt.axis('equal')
plt.grid()
for i_x, i_y in zip(x, y):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.show()


