# coding: utf-8

import numpy as np
import random

path = "../../source_data/RandomForest/sonar-all-data.txt"

label_mapping = {"R":1, "M":2}

def load_data(train_data_rate = 0.7):
    with open(path) as input:
        lines = input.readlines()
        random.shuffle(lines)
        train_data_size = int(len(lines) * train_data_rate)
        test_data_size = len(lines) - train_data_size
        train_data = np.zeros((train_data_size, 60))
        train_labels = np.zeros(train_data_size)
        test_data = np.zeros((test_data_size, 60))
        test_labels = np.zeros(test_data_size)

        index = 0
        for line in lines[0: train_data_size]:
            line = line.replace("\n", "")
            split = line.split(",")
            train_data[index, :] = split[0: -1]
            train_labels[index] = label_mapping[split[-1]]
            index += 1
        
        index = 0
        for line in lines[train_data_size: len(lines)]:
            line = line.replace("\n", "")
            split = line.split(",")
            test_data[index, :] = split[0: -1]
            test_labels[index] = label_mapping[split[-1]]
            index += 1

    return train_data, train_labels, test_data, test_labels

if __name__ == "__main__":
    data = load_data()
    print(data[0])
    print(data[1])
    print(data[2])
    print(data[3])