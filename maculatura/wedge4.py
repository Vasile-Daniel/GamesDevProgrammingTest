import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Define the radius and coordinates of the center and two points
R = 20
x0, y0 = 28, 42
x1, y1 = 13.857864376269049, 56.14213562373095
x2, y2 = 42.14213562373095, 56.14213562373095

# Calculate angles for the points
angle1 = np.degrees(np.arctan2(y1 - y0, x1 - x0))
angle2 = np.degrees(np.arctan2(y2 - y0, x2 - x0))

# Define the list of points
x_origin = [28, 27, 16, 40, 8, 6, 28, 39, 12, 36, 22, 33, 41, 41, 14, 6, 46, 17, 28, 2]
y_origin = [42, 46, 22, 50, 6, 19, 5, 36, 34, 20, 47, 19, 18, 34, 29, 49, 50, 40, 26, 12]
points = zip(x_origin, y_origin)

# Find the points within the sector
points_in_sector = []
for point in points:
    xp, yp = point
    angle_point = np.degrees(np.arctan2(yp - y0, xp - x0))
    if angle2 <= angle_point <= angle1:
        points_in_sector.append(point)

points_in_sector = list(points_in_sector)

# Create a figure and an axis
fig, ax = plt.subplots()

# Create the wedge (sector) with the empty part
sector = patches.Wedge((x0, y0), R, angle2, angle1, fill=True, color='green')
ax.add_patch(sector)

# Plot the points within the sector in red
x_points, y_points = zip(*points_in_sector)
ax.scatter(x_points, y_points, color='red', marker='.')

# Set axis limits
ax.set_xlim([x0 - R - 5, x0 + R + 5])
ax.set_ylim([y0 - R - 5, y0 + R + 5])

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Display the plot
plt.show()