# Importing the necessary libraries
from cmath import sqrt
from matplotlib import pyplot as plt
import numpy as np

'''
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
        [-10, -3],
        [4, 8],
        [2, 6],
        [1.5, 8],
        [-3, -3],
        [6, 11],
        [-1, 7],
        [3, -6],
        [7, 7],
        [4, 0],
        [-2, 1],
        [3, 5],
        [9, 3],
        [1.25, 6],
        [-10, 0],
        [3, 8],
        [5, 2],
        [7, 5],
        [8, -3]
])

MAX_DISTANCE = 3

def find_most_distant_points(points, first_index, last_index):
    most_distant_points = np.zeros([0,2])
    current_x_val=0.0
    current_y_val=0.0
    max_distance = 0.0
    max_el_index=0
    #Line equation
    first_point = points[first_index]
    last_point = points[last_index]
    a = ((first_point[1] - last_point[1]) / (first_point[0] - last_point[0]))*(-1)
    b = 1 #coefficient at y
    c = (first_point[1] - (a*first_point[0]))*(-1)

    for el in range(first_index, last_index):
        if el != first_index and el != last_index:
            current_x_val = points[el][0]
            current_y_val = points[el][1]
            numerator = abs((a*current_x_val) + (b*current_y_val) + c)
            denominator = sqrt(pow(a,2) + pow(b,2))
            distance = numerator/denominator
            if distance > max_distance:
                max_distance = distance
                max_el_index = el
    
    # print (first_index, last_index, max_el_index)
    if max_distance > MAX_DISTANCE:
        most_distant_point = points[max_el_index]
        most_distant_points = np.append(most_distant_points, most_distant_point)
        if max_el_index - first_index > 1:
            most_distant_points = np.append(most_distant_points, find_most_distant_points(points, first_index, max_el_index))
        if last_index - max_el_index > 1:
            most_distant_points = np.append(most_distant_points, find_most_distant_points(points, max_el_index, last_index))
    return most_distant_points

# Preparing the data to be computed and plotted
def broken_line_granulation(points):

    # Preparing X and y from the given data
    x = points[:, 0].reshape(len(points), 1)
    y = points[:, 1].reshape(len(points), 1)

    sorted_points = points[points[:,0].argsort()]
    print(sorted_points)
    print("\n")
    array_size = len(points)
    # print("Array size:")
    # print(array_size)

    first_point = sorted_points[0]
    last_point = sorted_points[array_size-1]
    # print("Points")
    # print(first_point)
    # print(last_point)

    '''
    #Distance between points
    x_sum = last_point[0] - first_point[0]
    y_sum = last_point[1] - first_point[1]
    pow_x_sum = pow(x_sum,2)
    pow_y_sum = pow(y_sum,2)
    distance = sqrt(pow_x_sum + pow_y_sum)
    print("Distance:")
    print(distance)
    '''

    searched_points = find_most_distant_points(sorted_points, 0, array_size-1)
    searched_points = np.append(searched_points, first_point)
    searched_points = np.append(searched_points, last_point)
    array_length = int(len(searched_points)/2)
    # print("dlugosc tablicy szukanych punktow: ", array_length)
    searched_points = np.reshape(searched_points, (array_length, 2))

    sorted_searched_points = searched_points[searched_points[:,0].argsort()]

    # print("Sorted Searched points")
    print(sorted_searched_points)

    sorted_searched_points_array_size = len(sorted_searched_points)
    # print("Array size:")
    # print(sorted_searched_points_array_size)

    # Plotting the data points and the best fit line
    plt.scatter(x, y)

    for i in range(array_size-1):
        x_val = [sorted_points[i][0], sorted_points[i+1][0]]
        y_val = [sorted_points[i][1], sorted_points[i+1][1]]
        plt.plot(x_val,y_val,'y')
        
    #x_first_last = [first_point[0], last_point[0]] - to draw a line from a start point to end point 
    #y_first_last = [first_point[1], last_point[1]]
    #plt.plot(x_first_last,y_first_last,'b')

    for k in range(sorted_searched_points_array_size-1):
        x_value = [sorted_searched_points[k][0], sorted_searched_points[k+1][0]]
        y_value = [sorted_searched_points[k][1], sorted_searched_points[k+1][1]]
        plt.plot(x_value,y_value,'r')
        
    plt.title('Wykres granulacji linii łamanej')
    plt.xlabel('X')
    plt.ylabel('Y')

    plt.show()
    
broken_line_granulation(points)