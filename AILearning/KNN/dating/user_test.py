# coding: utf-8

import dating_data_process
import knn
import matplotlib
import matplotlib.pyplot as plt

features, labels = dating_data_process.parse_dating_data("../../source_data/KNN/datingTestSet2.txt")

features = dating_data_process.norm(features)

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.scatter(features[:, 0], features[:, 1], 15.0 * labels, 15.0 * labels)
# plt.show()

training = features[0:int(len(features) * 0.8)]
training_labels = labels[0:int(len(features) * 0.8)]
tests = features[int(len(features) * 0.8):len(features)]
check_labels = labels[int(len(features) * 0.8):len(features)]

test_labels = []
for test_case in tests:
    test_labels.append(knn.knn(test_case, training, training_labels))

test_labels
check_labels

print(len([tup for tup in zip(test_labels, check_labels) if tup[0] == tup[1]]) / len(check_labels))
