# Importing the necessary libraries
from cmath import sqrt
import matplotlib.pyplot as plt
import numpy as np


# points = np.array([
#         [-11, 8],
#         [-10, 6],
#         [-9, 7],
#         [-8, 4],
#         [-7, 2.5],
#         [-6, 0],
#         [-5, 3],
#         [-4, 0],
#         [-3, 1],
#         [-2, -4],
#         [-1, 2],
#         [0, 3],
#         [1, 5],
#         [2, 7],
#         [3, -3],
#         [4, 0.5],
#         [5, 2.5],
#         [6, 4],
#         [7, 0],
#         [8, -4]
# ])

# points = np.array([
#         [5,-0.2],
#         [4,0.3],
#         [3,-0.2],
#         [2,0.2],
#         [1,0],
#         [0, 0.3],
#         [0.1, 1],
#         [0, 2],
#         [-0.1, 3],
#         [0, 4],
#         [0.1, 5],
#         [1, 5],
#         [2, 5.1],
#         [3, 4.9],
#         [4, 5],
#         [5, 5]
# ])

points = np.array([
        [1, 4],
        [-11, -3],
        [5, 8],
        [2, 6],
        [1.5, 8],
        [-3, -3],
        [7, 11],
        [-1, 7],
        [3.25, -6],
        [8, 7],
        [4, 0],
        [-2, 1],
        [3, 5],
        [10, 2],
        [1.25, 6],
        [-10, 0],
        [3.5, 8],
        [6, 2],
        [7.5, 5],
        [9, -3]
])

MAX_DISTANCE = 3
searched_points = np.empty([0,2])

def find_most_distant_points(points, first_index, last_index):
    most_distant_points = np.empty([0,2])
    current_x_val=0.0
    current_y_val=0.0
    max_distance = 0.0
    max_el_index=0
    x=0.0
    #Line equation
    first_point = points[first_index]
    last_point = points[last_index]
    if (first_point[0] - last_point[0]) == 0:
        a=1
        x = first_point[0] 
    else:
        a = ((first_point[1] - last_point[1]) / (first_point[0] - last_point[0]))
    b = -1 #coefficient at y
    c = (first_point[1] - (a*first_point[0]))
    # print(a)
    # print(c)
    print("kolejne najdalsze odleglosci w petli z indeksami punktow: ")
    for el in range(first_index, last_index):
        if el != first_index and el != last_index:
            current_x_val = points[el][0]
            current_y_val = points[el][1]
            numerator = abs((a*current_x_val) + (b*current_y_val) + c)
            denominator = sqrt(pow(a,2) + pow(b,2))
            if (first_point[0] - last_point[0]) == 0:
                distance = x - current_x_val
            else:
                distance = numerator/denominator
            if distance > max_distance:
                max_distance = distance
                max_el_index = el
                print(max_el_index, max_distance)
    print("info o najdalszym punkcie: ")
    print (first_index, last_index, max_el_index, max_distance)
    print("\n")
    if max_distance > MAX_DISTANCE:
        most_distant_point = points[max_el_index]
        if max_el_index - first_index > 1:
            most_distant_points = np.append(most_distant_points, find_most_distant_points(points, first_index, max_el_index))
        most_distant_points = np.append(most_distant_points, most_distant_point)
        if last_index - max_el_index > 1:
            most_distant_points = np.append(most_distant_points, find_most_distant_points(points, max_el_index, last_index))
    return most_distant_points

# Preparing the data to be computed and plotted
def broken_line_granulation(searched_points,points):

    # Preparing X and y from the given data
    x = points[:, 0].reshape(len(points), 1)
    y = points[:, 1].reshape(len(points), 1)
    
    sorted_points = points
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
    searched_points = np.append(searched_points, first_point)
    searched_points = np.append(searched_points, find_most_distant_points(sorted_points, 0, array_size-1))
    print("As")
    print(searched_points[0])
    searched_points = np.append(searched_points, last_point)
    array_length = int(len(searched_points)/2)
    # print("dlugosc tablicy szukanych punktow: ", array_length)
    searched_points = np.reshape(searched_points, (array_length, 2))

    sorted_searched_points = searched_points

    print(sorted_searched_points)

    sorted_searched_points_array_size = len(sorted_searched_points)
    # print("Array size:")
    # print(sorted_searched_points_array_size)

    # Plotting the data points and the best fit line
    plt.scatter(x, y)

    #for i in range(array_size-1):
    #    x_val = [sorted_points[i][0], sorted_points[i+1][0]]
    #    y_val = [sorted_points[i][1], sorted_points[i+1][1]]
    #    plt.plot(x_val,y_val,'y')
            
    #x_first_last = [first_point[0], last_point[0]] - to draw a line from a start point to end point 
    #y_first_last = [first_point[1], last_point[1]]
    #plt.plot(x_first_last,y_first_last,'b')

    #for k in range(sorted_searched_points_array_size-1):
    #    x_value = [sorted_searched_points[k][0], sorted_searched_points[k+1][0]]
    #    y_value = [sorted_searched_points[k][1], sorted_searched_points[k+1][1]]
    #    plt.plot(x_value,y_value,'r')
    
    x_values=[]
    y_values=[]
    sorted_x_values=[]
    sorted_y_values=[]
    
    for i in range(array_size):
        x_values.append(sorted_points[i][0])
        y_values.append(sorted_points[i][1]) 
    
    for k in range(sorted_searched_points_array_size):
        sorted_x_values.append(sorted_searched_points[k][0])
        sorted_y_values.append(sorted_searched_points[k][1])
    
        
    plt.title('Wykres granulacji linii łamanej')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.plot(x_values, y_values, 'o-', color='blue', label='Linia wejściowa')
    plt.plot(sorted_x_values, sorted_y_values, 'o-', color='red', label='Linia przybliżona')
    plt.legend()
    plt.show()
    
broken_line_granulation(searched_points, points)