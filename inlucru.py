############################################
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math 
################################################

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
    matrix[i][0] = id[i] # number 
    matrix[i][1] = x_origin[i] # abscissa 
    matrix[i][2] = y_origin[i] # ordinate 
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
    # ######################################################### 
    # P(x1,y1) for the "left" cone -- the half left cone direction 
    x1 = x0 - np.cos(angle) * pox - np.sin(angle) * poy 
    y1 = y0 - np.cos(angle) * poy + np.sin(angle) * pox

    #  P(x2,y2) for the "right" cone -- the half right cone direction 
    x2 = x0 - np.cos(angle) * pox + np.sin(angle) * poy 
    y2 = y0 - np.cos(angle) * poy - np.sin(angle) * pox

    # Calculate angles for the points
    angle1 = np.degrees(np.arctan2(y2 - y0, x2 - x0))
    angle2 = np.degrees(np.arctan2(y1 - y0, x1 - x0))

    # Find the points within the sector
    points_in_sector = []
    for point in points:
        xp, yp = point
        # distance between center of the circle and point
        d = np.sqrt((xp-x0)**2 + (yp-y0)**2) 
        # print(point)
        angle_point = np.degrees(np.arctan2(yp - y0, xp - x0))
        if (angle2 <= angle_point <= angle1) and (d < R):
            points_in_sector.append(point)
            

    points_in_sector = list(points_in_sector)

    # Create a figure and an axis
    fig, ax = plt.subplots()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("The points in the area of the cone sector")

    # Create the wedge (sector) with the empty part
    sector = patches.Wedge((x0, y0), R, angle2, angle1, fill=True, color='pink')
    ax.add_patch(sector)



    # Plot the points within the sector 
    for k in range(len_x):
        # for i in range(len(x_points)): 
        #     if ((x_origin[k] != x_points[i]) and (y_origin[k] != y_points[i])):
        ax.scatter(x_origin[k], y_origin[k], color='black', marker='.')
    # Plot the points within the sector in red
    x_points, y_points = zip(*points_in_sector)
    ax.scatter(x_points, y_points, color='red', marker='.')

    ax.scatter(x0, y0, color='blue', marker='.')
    ax.scatter(x1, y1, color='blue', marker='*')
    ax.scatter(x2, y2, color='blue', marker='*')
    ax.scatter(x, y, color='green', marker='*')


    # Set axis limits
    # ax.set_xlim([x0 - R - 5, x0 + R + 5])
    # ax.set_ylim([y0 - R - 5, y0 + R + 5])

    # Set aspect ratio to be equal
    ax.axis([0, 70, 0, 70])
    ax.set_aspect('equal')

    ax.grid()
    
    abscisa = np.trunc([x0, x2, x1, x]) 
    ordonata = np.trunc([y0, y2, y1, y])

    for i_x, i_y in zip(abscisa, ordonata):
        ax.text(i_x, i_y, '({}, {})'.format(i_x, i_y))

    for j_x, j_y in list(points_in_sector):
        ax.text(j_x, j_y, '({}, {})'.format(j_x, j_y))

    for k_x, k_y in zip(x_origin,y_origin):
        ax.text(k_x, k_y, '({}, {})'.format(k_x, k_y))

    # Display the plot
    plt.show()

    return abscisa, ordonata  
# call the function rotatingPoint() 
rezult = rotatingPoint(13,angle,R)


