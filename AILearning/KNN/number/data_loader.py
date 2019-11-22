# coding: utf-8

import os
import numpy as np

training_data_path = "../../../source_data/KNN/trainingDigits"
test_data_path = "../../../source_data/KNN/testDigits"


def load_training_data():
    files = os.listdir(training_data_path)
    features = np.zeros((len(files), 1024))
    labels = np.zeros(len(files))
    index = 0
    for filename in files:
        feature, label = _load_one_file(filename, training_data_path)
        features[index] = feature
        labels[index] = label
        index += 1
    return features, labels


def _load_one_file(filename, prefix):
    label = int(filename[0])
    filename = prefix + "/" + filename
    with open(filename) as input:
        feature = np.zeros((1, 1024))
        index = 0
        for line in input.readlines():
            line = line.replace("\n", "")
            feature[:, index:index+32] = [int(c) for c in line]
            index += 32
    return feature, label

def load_test_data():
    files = os.listdir(test_data_path)
    features = np.zeros((len(files), 1024))
    labels = np.zeros(len(files))
    index = 0
    for filename in files:
        feature, label = _load_one_file(filename, test_data_path)
        features[index] = feature
        labels[index] = label
        index += 1
    return features, labels


if __name__ == "__main__":
    feature, label = _load_one_file("0_0.txt")
    print(feature)
    print(label)
