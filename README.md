# Scrappy KMeans Project
- [trying_kmeans.py (FINAL VERSION)](/trying_kmeans.py) 
- [basic use of kmeans algorithm](/basic_use_of_kmeans.py)

## My K-Means Algorithm Built From Scratch
- The algorithm ultilizes a variety of Python data structures and OOP to group data together
- Ultilizes Python Libraries such as Numpy and Matplotlib
- Groups a set of datapoints together based on K amount of groups
- Returns a Python dictionary where the key is group number and value is an array of array points

## Intro to KMeans Clustering (How it works)
- KMeans is an unsupervised machine learning algorithm. 
- K represents the number of clusters/centroids the dataset has. 
- Centroids are simply just the mean point or center of a group of points
- The algorithm begins by selecting K amount of random centroids where it then finds the eudlidean distance between the data points and K number of centroids. The points closest to a certain centroid will be classified as a cluster with that centroid. The algorithm will then find the mean of all the points in that cluster and the mean will be the new centroid. It will continuously do this until the mean of all clusters stop changing and are optimized.  

## Purpose of KMeans
- "group similar data points together and discover underlying patterns" as stated by AndreyBu 
- ex. market segmentation and fraud detection 

## Abstract
- a visualization of what the algorithm does
<img src="/images/readme1.png" width="1000" height="400">
<img src="/images/readme2.png" width="1000" height="400">
<img src="/images/readme3.png" width="1000" height="400">

## Future Directions
- Build a more accurate model that classfies and groups data more accurately
- Implement recursion?
