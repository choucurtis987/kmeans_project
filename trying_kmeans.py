import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

class scrap_kmeans:

    def __init__(self, k=2):
        self.k = k

    # takes a numpy array of shape(-1,2) as argument:
    def fit(self,data):
        centroids = set()

        # finding the first random centroids:
        while self.k:
            num = np.random.randint(0,len(data))
            # print("data: " , data.shape)
            # print("data: " , data[num].shape)
            centroid = tuple(data[num])
            centroids.add(centroid)
            if len(centroids) == self.k:
                break

        points = [np.array(point) for point in data]
        # starting centroids:
        first_centroids = np.array( [np.array(centroid) for centroid in centroids] )
        # print("first centroids shape: " , first_centroids.shape)


        # classifying the points:
        # centroids and points take a list of arrays as argument:
        def classify(centroids, points):
            num = 0
            blank = []
            classification = {}
            self.true_labels = []

            for i in range(self.k):
                classification[i] = []

            while True:
                for centroid in centroids:
                    # print("centroid: " , centroid.shape)
                    # print("points[num]: " , points[num].shape)
                    euclidean_distance = float( np.linalg.norm(centroid - points[num]) )
                    # adding distances to a list to find the min:
                    blank.append(euclidean_distance)

                classification[ blank.index(min(blank))].append(list(points[num]))
                self.true_labels.append( blank.index(min(blank)) )
                num += 1
                blank = []
                if num == len(points):
                    break

            return classification

        # takes dict as argument:
        def update(classification):
            # new centroids
            blank = []
            # loop through dict
            for i in classification:
                classification[i] = np.array(classification[i])
                # find the mean of xs and ys giving a new centroid
                new_centroids_x = np.mean( classification[i][:,0] )
                new_centroids_y = np.mean( classification[i][:,1] )
                new_centroids = np.array([new_centroids_x,new_centroids_y])

                # add that centroid to a list
                blank.append(new_centroids)

            return blank

        # first classification of points based on random centroids:
        classification = classify(first_centroids, points)
        # storage of all centroids:
        storage = []

        # this while statement optimizes the centroid to the point where a new centroid no longer changes the
        # classification of the points:
        while True:

            if not storage:
                centroids = update(classification)
                # print("\ncentroid shape: ", len(centroids), "\n")
                new_classification = classify(centroids, points)
                storage.append(centroids)

            test = classify(storage[-1], points)

            if storage:
                centroids = update(test)

                new_classification = classify(centroids, points)
                storage.append(centroids)
                for i in new_classification:
                    new_classification[i] = np.array(new_classification[i])
                a = new_classification[i] == test[i]

            # np.all is a conditional to compare numpy arrays
            if np.all(a):
                break

        # this finds the true centroid or reassures it
        blank = []
        for i in new_classification:
            new_x = new_classification[i][:,0].mean()
            new_y = new_classification[i][:,1].mean()
            new_centroid = [new_x,new_y]
            blank.append(new_centroid)
        storage.append(blank)

        # process of changing centroids, uncomment to see
        # for num, i in enumerate(storage):
        #     print(f'{num}: {i}')

        self.centroids = np.array(storage[-1])
        self.true_labels = np.array(self.true_labels)

        return new_classification
