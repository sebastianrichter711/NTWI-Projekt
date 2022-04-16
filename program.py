# Importing the necessary libraries
from cmath import sqrt
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
dt = np.array([
          [0.05, 0.11],
          [0.12, 0.29],
          [0.19, 0.07],
          [0.22, 0.09],
          [0.26, 0.10],
          [0.37, 0.34],
          [0.28, 0.32],
          [0.32, 0.30],
          [0.36, 0.39],
          [0.37, 0.42],
          [0.40, 0.40],
          [0.07, 0.19],
          [0.02, 0.04],
          [0.15, 0.19],
          [0.43, 0.48],
          [0.44, 0.41],
          [0.47, 0.49],
          [0.50, 0.57],
          [0.53, 0.59],
          [0.58, 0.60]
])

# Preparing X and y from the given data
x = dt[:, 0].reshape(len(dt), 1)
y = dt[:, 1].reshape(len(dt), 1)

min_element = np.amin(x)
print(min_element)

max_element = np.amax(x)
print(max_element)

min_element_index = np.where(x == np.amin(x))
print(min_element_index[0])

max_element_index = np.where(x == np.amax(x))
print(max_element_index[0])

first_point = dt[min_element_index[0]]
last_point = dt[max_element_index[0]]
print("Points")
print(first_point[0])
print(last_point[0])

'''
#Distance between points
x_sum = last_point[0][0] - first_point[0][0]
y_sum = last_point[0][1] - first_point[0][1]
pow_x_sum = pow(x_sum,2)
pow_y_sum = pow(y_sum,2)
distance = sqrt(pow_x_sum + pow_y_sum)
print(distance)
'''

#Line equation
a = (first_point[0][1] - last_point[0][1]) / (first_point[0][0] - last_point[0][0])
b = 1 #coefficient at y
c = first_point[0][1] - (a*first_point[0][0])
print(a)
print(c)

current_index=0
current_x_val=0.0
current_y_val=0.0
max_distance = 0.0



# Plotting the data points and the best fit line
plt.scatter(x, y)
#plt.plot(X, y_line, 'r')
plt.title('Wykres granulacji linii łamanej')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()