import matplotlib.pyplot as plt 
import numpy as np


arrX = [28, 27, 16, 40, 8, 6, 28, 39, 12, 36,22, 33,41, 41, 14,6, 46,17,28,2] 
arrY = [42, 46, 22,50, 6, 19, 5, 36, 34, 20, 47,19, 18,34, 29, 49, 50, 40, 26, 12]
direction = 5*["North", "East", "South", "West"]
givenP = zip(arrX,arrY)
beta = 45
beta1 = beta * np.pi/180
R = 20


len_d = len(direction)
len_X = len(arrX) # length of vector X 
len_Y = len(arrY) # length of vector Y 
arrNr = [None]*len_X

for i in range(len_X):
    arrNr[i] = i+1 

for i in range(len_X):
    myList = [arrX[i], arrY[i], arrNr[i], direction[i]] 
    print(myList)

# myList = zip(arrX,arrY, arrNr, direction)
# print(myList)


print(f"The length of direction =  {len_d}")    
print(f"The length of vector X = {len_X}")
print(f"The length of vecotr Y = {len_Y}")

# GRAPHIC 
plot1 = plt.plot(arrX, arrY, '*', color='tab:red')
plt.title('P(x,y)')
plt.xlabel('X')
plt.ylabel('Y')
plt.axis([0, 50, 0, 60])
plt.grid()
for i_x, i_y in zip(arrX, arrY):
    plt.text(i_x, i_y, '({}, {})'.format(i_x, i_y))
plt.show()
