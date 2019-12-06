# coding: utf-8

import sys

sys.path.append("../utils")

import data_loader

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import sklearn.preprocessing as preprocessing
from sklearn.impute import SimpleImputer

data = data_loader.load_cluster_data("../../source_data/PCA/secom.data", 590, ' ')

missing_processor = SimpleImputer()
data = missing_processor.fit_transform(data)

pca = PCA(n_components=3)
pca_data = pca.fit_transform(data)

print(pca_data)
print(pca.explained_variance_ratio_)