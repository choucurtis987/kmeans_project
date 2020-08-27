# Scrappy KMeans Project
- [My K-Means Algorithm](/trying_kmeans.py) 
- [Basic use of K-Means algorithm](/basic_use_of_kmeans.py)
- [Using K-Means algorithm with grayscale images](/use_of_kmeans_with_img.py)

## My K-Means Algorithm Built From Scratch
- Ultilizes a variety of Python data structures and OOP to group data together into K amount of groups
- Has features similar to sklearn KMeans where centroids and an array of labels can be displayed 
- Returns a Python dictionary where the key is group number(class) and value is an array of array points in that class/group
- Can be used on grayscale images that can be reshaped into shape (-1,2)

## Intro to KMeans Clustering (How it works)
- KMeans is an unsupervised machine learning algorithm. 
- K represents the number of clusters/centroids the dataset has. 
- Centroids are simply just the mean point or center of a group of points
- The algorithm begins by selecting K amount of random centroids where it then finds the eudlidean distance between the data points and K number of centroids. The points closest to a certain centroid will be classified as a cluster with that centroid. The algorithm will then find the mean of all the points in that cluster and the mean will be the new centroid. It will continuously do this until the mean of all clusters stop changing and are optimized.  

## Purpose of KMeans
- "group similar data points together and discover underlying patterns" as stated by AndreyBu 
- ex. market segmentation, image segmentation, fraud detection, etc 

## Abstract
- under construction (see images folder for old abstract)
<!--
<img src="/images/readme1.png" width="1000" height="400">
<img src="/images/readme2.png" width="1000" height="400">
<img src="/images/readme3.png" width="1000" height="400">
-->
## Future Directions
- Build a more accurate model that classfies and groups data more accurately
- Decrease runtime allowing model to operate on larger images/data
- Modify algorithm so that input shapes can be of (-1,1) making it more flexible
- Modify algorithm so that RGB images can inputtted 
