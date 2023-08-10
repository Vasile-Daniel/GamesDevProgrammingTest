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

# Create a figure and an axis
fig, ax = plt.subplots()

# Create the wedge (sector) with the empty part
sector = patches.Wedge((x0, y0), R, angle2, angle1, fill=True, color='pink')
ax.add_patch(sector)

# Set axis limits
ax.set_xlim([x0 - R - 5, x0 + R + 5])
ax.set_ylim([y0 - R - 5, y0 + R + 5])

# Set aspect ratio to be equal
ax.set_aspect('equal')

# Display the plot
plt.show()