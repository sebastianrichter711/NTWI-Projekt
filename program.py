# Importing the necessary libraries
from cmath import sqrt
from matplotlib import pyplot as plt
import numpy as np

# Preparing the data to be computed and plotted
points = np.array([
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
'''
points = np.array([
          [1, 4],
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
'''
# Preparing X and y from the given data
x = points[:, 0].reshape(len(points), 1)
y = points[:, 1].reshape(len(points), 1)

min_element = np.amin(x)
print(min_element)

max_element = np.amax(x)
print(max_element)

min_element_index = np.where(x == np.amin(x))
print(min_element_index[0])

max_element_index = np.where(x == np.amax(x))
print(max_element_index[0])

first_point = points[min_element_index[0]]
last_point = points[max_element_index[0]]
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

#for x in dt:
array_size = len(points)
print(array_size)

for el in range(array_size):
    if el != 0 and el != array_size-1:
        current_x_val = points[el][0]
        current_y_val = points[el][1]
        numerator = abs(a*current_x_val + b*current_y_val + c)
        xxx = pow(a,2) + pow(b,2)
        denominator = sqrt(xxx)
        distance = numerator/denominator
        if distance > max_distance:
            max_distance = distance
            current_index = el
        
searched_point = points[current_index]
print(searched_point)

print("Current index")
print(current_index)
# Plotting the data points and the best fit line
plt.scatter(x, y)
x_values = [first_point[0][0], searched_point[0]]
y_values = [first_point[0][1], searched_point[1]]
plt.plot(x_values, y_values, 'r')
x_values_2 = [searched_point[0], last_point[0][0]]
y_values_2 = [searched_point[1], last_point[0][1]]
plt.plot(x_values_2, y_values_2, 'r')
plt.title('Wykres granulacji linii łamanej')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()