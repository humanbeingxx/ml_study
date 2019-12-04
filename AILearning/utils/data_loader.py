# coding: utf-8

import numpy as np

def load_data(path, feature_num, splitter):
    with open(path) as input:
        lines = input.readlines()
        data_size = len(lines)
        training_data = np.zeros((data_size, feature_num))
        training_labels = np.zeros(data_size)
        index = 0
        for line in lines:
            split = line.split(splitter)
            training_data[index, :] = split[0: -1]
            training_labels[index] = split[-1]
            index += 1
        return training_data, training_labels

def load_cluster_data(path, feature_num, splitter = "\t"):
    with open(path) as input:
        lines = input.readlines()
        data_size = len(lines)
        data = np.zeros((data_size, feature_num))
        index = 0
        for line in lines:
            line = line.replace("\n", "")
            split = line.split(splitter)
            data[index, :] = split[0: len(split)]
            index += 1
        return data
