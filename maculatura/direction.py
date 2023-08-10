import matplotlib.pyplot as plt 
import numpy as np


angle = 45 
angle = angle * np.deg2rad(angle)
A = 20

# R = A/np.cos(angle)
R = A/np.sin(angle)

print(R)
