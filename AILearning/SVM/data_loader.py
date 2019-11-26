# coding: utf-8

import os
import numpy as np

training_data_path = "../../source_data/SVM/trainingDigits"
test_data_path = "../../source_data/SVM/testDigits"


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

def load_one_vs_ten_training_data():
    files = os.listdir(training_data_path)
    label_dict = {}
    for i in range(0, 10):
        label_dict[i] = (np.zeros((len(files), 1024)), np.zeros(len(files)))
    index = 0
    for filename in files:
        _add_data_for_index(int(filename[0]), filename, training_data_path, label_dict, index)
        index += 1
    return label_dict


def load_one_vs_ten_test_data():
    files = os.listdir(test_data_path)
    label_dict = {}
    for i in range(0, 10):
        label_dict[i] = (np.zeros((len(files), 1024)), np.zeros(len(files)))
    index = 0
    for filename in files:
        _add_data_for_index(int(filename[0]), filename, test_data_path, label_dict, index)
        index += 1
    return label_dict


def _add_data_for_index(specified_label, filename, filename_prefix, label_dict, index):
    features = _parse_feature_from_file(filename_prefix + "/" + filename)
    data_size = len(features)
    label_dict[specified_label][0][index] = features
    label_dict[specified_label][1][index] = np.ones(data_size)
    for tup in label_dict.items():
        if tup[0] == specified_label:
            continue
        data = tup[1]
        data[0][index] = features
        data[1][index] = np.ones(data_size) * -1


def _parse_feature_from_file(filename):
    with open(filename) as input:
        feature = np.zeros((1, 1024))
        line_index = 0
        for line in input.readlines():
            line = line.replace("\n", "")
            feature[:, line_index:line_index+32] = [int(c) for c in line]
            line_index += 32
        return feature

if __name__ == "__main__":
    data = load_one_vs_ten_training_data()
    print(len([label for label in data[1][1] if label == 1]))
    show_features = data[1][0][0]
    for i in range(0, 32):
        print(show_features[i*32:i*32+32])

    test_data = load_one_vs_ten_test_data()
    print(len([label for label in test_data[1][1] if label == 1]))
    show_features = test_data[1][0][0]
    for i in range(0, 32):
        print(show_features[i*32:i*32+32])