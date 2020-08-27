# This code is simply creating a random collection of data points and
# using my K Means algorithm to group the data

import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from trying_kmeans import scrap_kmeans

# creation of a random points:
x = np.random.randint(50, size=50)
y = np.random.randint(50, size=50)
data = []
for value in zip(x,y):
    data.append(np.array(value))
data = np.array(data)

# creating an instance of the class:
model = scrap_kmeans(k=3)
# NOTE: data is of shape (-1,2). All inputs to model must be of shape (-1,2)
test = model.fit(data)

# available output data:
centroids = model.centroids
labels = model.true_labels
print("Centroids: ", centroids)
print('\n')
print("Labels: ", labels)
print('\n')
# dict of classified points with class as key and numpy array of points in class as values
print(test)

# plotting the points + centroids + classification of points
zer = test[0]
one = test[1]
two = test[2]

for point in zer:
    plt.scatter(point[0],point[1], c='red')
for points in one:
    plt.scatter(points[0],points[1], c='blue')
for points in two:
    plt.scatter(points[0],points[1], c='green')

plt.scatter(centroids[0][0], centroids[0][1], c='black', marker ="*", s=200)
plt.scatter(centroids[1][0], centroids[1][1], c='black', marker = '*', s=200)
plt.scatter(centroids[2][0], centroids[2][1], c='black', marker = '*', s=200)
plt.show()
