# Importing the necessary libraries
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

# Plotting the data points and the best fit line
plt.scatter(x, y)
#plt.plot(X, y_line, 'r')
plt.title('Wykres granulacji linii łamanej')
plt.xlabel('X')
plt.ylabel('Y')

plt.show()