# This code is simply creating a random collection of data points and using the custom K Means algorithm to group the data

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import trying_kmeans

# creation of a random points:
x = np.random.randint(50, size=50)
y = np.random.randint(50, size=50)
data = []
for value in zip(x,y):
    data.append(np.array(value))
data = np.array(data)

# creating an instance of the class:
instance = trying_kmeans.scrap_kmeans()
test = instance.fit(data)

# plotting the points + centroids + classification of points
centroids = instance.centroids
zer = test[0]
one = test[1]
for point in zer:
    plt.scatter(point[0],point[1], c='red')
for points in one:
    plt.scatter(points[0],points[1], c='blue')
plt.scatter(centroids[0][0], centroids[0][1], c='green', marker ="*", )
plt.scatter(centroids[1][0], centroids[1][1], marker = '+')

plt.show()
