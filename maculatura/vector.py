import pylab as plt
import numpy as np
#plt.style.use('ggplot') # because it's just better ;)

v_origin = [.2, .3]
v = [1., 1.]
angular_uncert = 20. # angular uncertainty of vector in degrees
v_angle = np.arctan2( v[1] ,v[0] ) # starting angle

# plot the arrow
fig = plt.figure(1)
ax = plt.gca()
ax.arrow(v_origin[0], v_origin[1] ,v[0], v[1], 
    head_width=0.05, 
    head_length=0.1, 
    lw=2, 
    fc='#777777', 
    ec='#777777', 
    length_includes_head=True)

# plot the sector line
uncert = (angular_uncert/2.) *np.pi / 180.
r = np.linalg.norm( v ) # length of vector
t = np.linspace( v_angle - uncert , v_angle+uncert , 100) # angular range of sector
x = r* np.cos(t) + v_origin[0] # sector x coords
y = r* np.sin(t) + v_origin[1] # sector y coords
ax.plot( x,y, lw=2, ls='--') # plot the sector
ax.plot( v_origin[0], v_origin[1], 'o', ms=10, c='Limegreen' ) # plot the origin

# adjust the figure
ax.set_xlim(0, 1.6)
ax.set_ylim(0, 1.6)
ax.set_aspect('equal')
fig.show()