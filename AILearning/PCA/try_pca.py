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

scaler = preprocessing.MinMaxScaler()

data = scaler.fit_transform(data)

model = PCA(n_components=4)
pca_data = model.fit_transform(data)

print(pca_data)