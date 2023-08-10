from PIL import Image
############################################
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
################################################

"""
Project Name: Tech Test for Games Developments Bootcamp  
Author: Vasile-Daniel DAN 
Location: Sheffield, UK 
Initial Date: 7 August 2023 (Last Update: 10 august 2023)  
"""

"""
PROBLEM FORMULATION 

Given the data from "img1", make a function where given a Point value returns all points in a visible cone that extends in the direction given a visible cone value made up of degrees and maximum direction. 

For instance, the function VisiblePoints(1,45,20) returns an array with one object (27,46,2,East).

In this example, the 45 degree cone is 45 degrees in each direction so could be visualised like in "img2":

"""
######### INPUT DATA  PROVIDED ###############################################################################
img1 = Image.open("tabel1.jpg")
img1.show()
img2 = Image.open("conul.jpg")
img2.show()
############ INPUT DATA ############################################################################
x_origin = [28, 27, 16, 40, 8,  6, 28, 39, 12, 36, 22, 33, 41, 41, 14,  6, 46, 17, 28,  2] # see img 1
y_origin = [42, 46, 22, 50, 6, 19,  5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12] # see img 1
points = zip(x_origin, y_origin)
direction = 5*["North", "East", "South", "West"] # see img 1 

len_x = len(x_origin)
angle = 45 # 
R = 20 
id = [] # number - see img 1 

for i in range(1,len_x+1):
    id.append(i)

########## PROBLEM SOLVING ##################################################################################################
# put all the data in 1 matrix (bidimensional array): x_origin,y_origin, number direction 
matrix = np.zeros((len_x,4))
matrix = np.array(matrix, dtype=object)
for i in range(len_x):
    matrix[i][0] = id[i]
    matrix[i][1] = x_origin[i]
    matrix[i][2] = y_origin[i]
    matrix[i][3] = direction[i]

# Find the points on the circle on the left and side part of direction (North, Weast, South, East)        
def rotatingPoint(id,unghi,R):
    angle = (unghi * np.pi) /180 # angle = deg2rad(unghi)

    obj = matrix[id-1]
    print(obj)
    x0 = obj[1]
    y0 = obj[2]

    if (obj[3] == "North"):
        x = obj[1]
        y = obj[2]+R
        print(obj[3])
    elif (obj[3] == "West"):
        x = obj[1]-R
        y = obj[2]
        print(obj[3])
    elif (obj[3] == "South"):
        x = obj[1]
        y = obj[2]-R
        print(obj[3])
    elif (obj[3] == "East"):
        x = obj[1]+R
        y = obj[2]
        print(obj[3])

    pox = x0 - x
    poy = y0 - y

    # "LEFT" CON + "RIGHT CONE" = 1 cone 
    # P(x1,y1) for the "left" cone -- the half left cone direction 
    x1 = x0 - np.cos(angle) * pox - np.sin(angle) * poy 
    y1 = y0 - np.cos(angle) * poy + np.sin(angle) * pox

    #  P(x2,y2) for the "left" cone -- the half left cone direction 
    x2 = x0 - np.cos(angle) * pox + np.sin(angle) * poy 
    y2 = y0 - np.cos(angle) * poy - np.sin(angle) * pox

    abscisa = [x0, x2, x1, x] 
    ordonata = [y0, y2, y1, y]


    return abscisa, ordonata  
# call the function rotatingPoint() 
X, Y = rotatingPoint(1,angle,R)
# print(set(zip(X,Y)))


# Call the function 'grafic()' to show the graphic like in the privided picture (more or less :D )
# Find the points within the sector (the core of the problem)
def grafic(x,y,R):

    # Calculate angles for the points
    angle1 = np.degrees(np.arctan2(y[1] - y[0], x[1] - x[0]))
    angle2 = np.degrees(np.arctan2(y[2] - y[0], x[2] - x[0]))

    # Find the points within the sector
    points_in_sector = []
    for point in points:
        xp, yp = point
        angle_point = np.degrees(np.arctan2(yp - y[0], xp - x[0]))
        if angle2 <= angle_point <= angle1:
            points_in_sector.append(point)

    points_in_sector = list(points_in_sector)
    # Create a figure and an axis
    fig, ax = plt.subplots()

    # Create the wedge (sector) with the empty part
    sector = patches.Wedge((x[0], y[0]), R, angle2, angle1, fill=True, color='pink')
    ax.add_patch(sector)

    # Plot the points within the sector in red
    x_points, y_points = zip(*points_in_sector)
    ax.scatter(x_points, y_points, color='red', marker='.')

    # Set axis limits
    ax.set_xlim([x[0] - R - 5, x[0] + R + 5])
    ax.set_ylim([y[0] - R - 5, y[0] + R + 5])

    # Set aspect ratio to be equal
    ax.set_aspect('equal')
    ax.grid()
    for i_x, i_y in zip(x, y):
        ax.text(i_x, i_y, '({}, {})'.format(i_x, i_y))


    # Display the plot
    plt.show()

    return angle1, angle2 

a1, a2 = grafic(X,Y,R)
print(a1,a2)

# NOT TO BE USED AT THE MOMENT -- verify if the function rotatingPoint(id,unghi,R) gives the right result 
# def calculate_angle(p1, p2, p3):
#     # Calculate the vectors between the points
#     v1 = [p1[0] - p2[0], p1[1] - p2[1]]
#     v2 = [p3[0] - p2[0], p3[1] - p2[1]]
#     # Calculate the dot product of the vectors
#     dot_product = v1[0] * v2[0] + v1[1] * v2[1]
#     # Calculate the magnitude of the vectors
#     mag_v1 = math.sqrt(v1[0]**2 + v1[1]**2)
#     mag_v2 = math.sqrt(v2[0]**2 + v2[1]**2)
#     # Calculate the angle between the vectors in radians
#     angle = math.acos(dot_product / (mag_v1 * mag_v2))
#     # Convert the angle to degrees and return it
#     return math.degrees(angle)


# # Unghi Con - jumatatea stanga 
# p1 = [X[1],Y[1]]
# p2 = [X[0], Y[0]]
# p3 = [X[2], Y[2]]
# angle2 = calculate_angle(p1, p2, p3)
# print(angle2) 


# # Unghi Con - jumatatea dreapta 
# q1 = [X[1],Y[1]]
# q2 = [X[0], Y[0]]
# q3 = [X[3], Y[3]]
# angle3 = calculate_angle(p1, p2, p3)
# print(angle3)



