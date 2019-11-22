# coding: utf-8

import data_loader
import knn

train_data = data_loader.load_training_data()
test_data = data_loader.load_test_data()

test_labels = []
for index in range(0, len(test_data[0])):
    test_labels.append(knn.knn(test_data[0][index], train_data[0], train_data[1]))

print(len([tup for tup in zip(test_labels, test_data[1]) if tup[0] == tup[1]]) / len(test_data[0]))