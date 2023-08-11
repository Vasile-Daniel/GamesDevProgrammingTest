import numpy as np 


for i in range(360):
    # angle = i * np.pi / 180
    angle1 = np.degrees(np.arctan2(y2 - y0, x2 - x0))
    angle2 = np.degrees(np.arctan2(y1 - y0, x1 - x0))
    
    cs1 = np.cos(angle1)
    sn1= np.sin(angle1)
    cs2 = np.cos(angle2)
    sn2 = np.sin(angle2)


    angle3_1 = np.atan2(sn, cs)  # ALWAYS USE THIS
    angle3_1 *= 180 / np.pi
    if angle3_1 < 0: angle3_1 += 360
    print(angle3_1)