import matplotlib.pyplot as plt
import numpy as np
from trying_kmeans import scrap_kmeans
import skimage.io
import skimage.transform
import sys
import numpy as np

model = scrap_kmeans(3)
# use in terminal with image file name as parameter:
# ex. python use_of_kmeans_with_img.py desired_image.jpg
# image must be in same directory as this py script
image = skimage.io.imread(sys.argv[1] , as_gray=True)
# since runtime will increase with larger images, use a small image for shorter runtime:
# input image shape to model must be a shape that be resized to (-1,2)
new_image = skimage.transform.resize(image=image, output_shape=(300,300))
# display original image(new_image) before KMeans:
plt.imshow(new_image, cmap='gray')
plt.show()

shaped = new_image.reshape(-1, 2)

model.fit(shaped)

labels = model.true_labels
centroids = model.centroids

res = centroids[labels.flatten()]
res2 = res.reshape(new_image.shape)
# will display input image highlighting k number of dominant grayscale colors:
plt.imshow(res2, cmap='gray')
plt.show()

# save the KMeans segmented image:
fname = "kmeans-" + sys.argv[1]
plt.imsave(fname, res2, cmap='gray')
