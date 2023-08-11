"""
    
PROIECT INCHEIAT CU TOATE CORECTARILE IVITE 
IN ACEASTA "REZERVA" AM PASTRAT ABSOLUT TOATE print(), ... 
. . .  INCLUSIV CELE CARE NU SUNT NECESARE IN PROIECTUL FINAL 
"""

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
number = list(range(1,21))

len_x = len(x_origin)
angle = 45 # degree  
R = 20 
nr = 2

# ########## PROBLEM SOLVING ##################################################################################################
matrix = list(zip(number,x_origin,y_origin,direction))
# print(matrix)


# Find the points on the circle on the left and side part of direction (North, Weast, South, East)        
def visiblePoints(idd,unghi,R):
    angle = (unghi * np.pi) /180 # angle = deg2rad(unghi)

    obj = matrix[idd-1]
    print("Object")
    print(obj)
    x0 = obj[1]
    y0 = obj[2]

    if (obj[3] == "North"):
        x = obj[1]
        y = obj[2]+R
        # print(obj[3])
    elif (obj[3] == "West"):
        x = obj[1]-R
        y = obj[2]
        # print(obj[3])
    elif (obj[3] == "South"):
        x = obj[1]
        y = obj[2]-R
        # print(obj[3])
    elif (obj[3] == "East"):
        x = obj[1]+R
        y = obj[2]
        # print(obj[3])

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
    print("angle 1")
    print(angle1)
    print("angle 2")
    print(angle2)

    # CORRECTION OF NEGATIVE ANGLES for 'West' dirrection
    # Correction angel 1  

    if (obj[3] == "West"):
        angle1a = np.arctan2(y2 - y0, x2 - x0)

        cs1 = np.cos(angle1a)
        sn1 = np.sin(angle1a)


        angle1 = math.atan2(sn1, cs1)  # ALWAYS USE THIS
        angle1 *= 180 / np.pi
        if angle1 < 0: 
            angle1 += 360
        print("angle 1 corectat")
        # print(angle1)

        # Correction angel 2
        angle2a = np.arctan2(y1 - y0, x1 - x0)

        cs2 = np.cos(angle2a)
        sn2 = np.sin(angle2a)

        angle2 = math.atan2(sn2, cs2)  # ALWAYS USE THIS
        angle2 = angle2 * 180 / np.pi # angle2 *= 180 / np.pi
        if angle2 < 0: 
            angle2 += 360
        print("angel 2 corectat ")
        print(angle2)




    # Find the points within the sector
    points_in_sector = []
    for point in points:
        xp, yp = point
        # distance between center of the circle and the point
        d = np.sqrt((xp-x0)**2 + (yp-y0)**2) 
        # print(point)
        angle_point = np.degrees(np.arctan2(yp - y0, xp - x0))
        if (angle2 <= angle_point <= angle1) and (d < R) and (point != (x0,y0)) :
            points_in_sector.append(point)
            print("except 1")
            print(point)

                 

    points_in_sector = list(points_in_sector)
    # print(points_in_sector)

    result = []
    for i in range(len(matrix)):
        for j in range(len(points_in_sector)):
            if (points_in_sector[j]  == matrix[i][1:3]):
                # print(matrix[i])
                result.append(matrix[i])

    # Create a figure and an axis
    fig, ax = plt.subplots()
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_title("The points in the area of the cone sector")

    # Create the wedge (sector) with the empty part
    sector = patches.Wedge((x0, y0), R, angle2, angle1, fill=True, color='pink')
    ax.add_patch(sector)

    # Plot all points ( including within the sector )
    for k in range(len_x):
        # for i in range(len(x_points)): 
        #     if ((x_origin[k] != x_points[i]) and (y_origin[k] != y_points[i])):
        ax.scatter(x_origin[k], y_origin[k], color='black', marker='.')

        
    # Plot the points within the sector in red
    # use "try - except" because if thre id not point in sector I will have the error  
    # ##### x_points, y_points = zip(*points_in_sector)
    # ##### ^^^^^^^^^^^^^^^^^^
    # ##### ValueError: not enough values to unpack (expected 2, got 0)
    # try:
    #     x_points, y_points = zip(*points_in_sector)
    #     ax.scatter(x_points, y_points, color='red', marker='.')
    # except:
    #     points_in_sector = []

    try:
        x_points, y_points = zip(*points_in_sector)
        ax.scatter(x_points, y_points, color='red', marker='.')
    except:
        x_points, y_points = [], []


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
    return result 
    



# call the function visiblePoints() 
# for i in range(20,21):
rezult = visiblePoints(nr,angle,R)
print(rezult)

