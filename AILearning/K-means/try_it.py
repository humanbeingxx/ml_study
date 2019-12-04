# coding: utf-8

import sys

sys.path.append("../utils")

import data_loader
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

data = data_loader.load_cluster_data("../../source_data/K-means/testSet.txt", 2, "\t")

model = KMeans(4).fit(data)

predicts = model.predict(data)

# plt.scatter(data[:, 0], data[:, 1], c=model)
# plt.show()

centers = model.cluster_centers_

plt.scatter(data[:, 0], data[:, 1], c=predicts)
plt.scatter(centers[:, 0], centers[:, 1])
plt.show()