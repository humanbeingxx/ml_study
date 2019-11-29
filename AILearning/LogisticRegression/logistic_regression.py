# coding: utf-8

from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt


def load_data():
    with open("../../source_data/Logistics/HorseColicTraining.txt") as input:
        data = input.readlines()
        dataSize = len(data)
        features = np.zeros((dataSize, 21))
        labels = np.zeros(dataSize)
        index = 0
        for line in data:
            split = line.split("\t")
            features[index, :] = split[0: 21]
            labels[index] = split[-1]
            index += 1
        return features, labels


def load_test():
    with open("../../source_data/Logistics/HorseColicTest.txt") as input:
        data = input.readlines()
        dataSize = len(data)
        features = np.zeros((dataSize, 21))
        labels = np.zeros(dataSize)
        index = 0
        for line in data:
            split = line.split("\t")
            features[index, :] = split[0: 21]
            labels[index] = split[-1]
            index += 1
        return features, labels


def resclae(data_set):
    return preprocessing.scale(data_set)


def train(features, labels):
    model = LogisticRegression(max_iter=100, C=1)
    return model.fit(features, labels)


if __name__ == "__main__":
    traing_curve = []
    test_curve = []
    number = 5
    for i in range(1, 70):
        features, labels = load_data()
        features = features[0: number * i]
        labels = labels[0: number * i]
        test_features, check_labels = load_test()
        model = train(features, labels)
        predicts = model.predict(test_features)
        test_accurancy = len([predict for predict, check in zip(predicts, check_labels) if predict == check]) / len(check_labels)
        train_predicts = model.predict(features)
        train_accurancy = len([predict for predict, check in zip(train_predicts, labels) if predict == check]) / len(labels)
        traing_curve.append([i * number, train_accurancy])
        test_curve.append([i * number, test_accurancy])

    plt.ylim(0, 1)
    plt.scatter([e[0] for e in traing_curve] + [e[0] for e in test_curve], [e[1] for e in traing_curve] + [e[1] for e in test_curve])
    plt.show()