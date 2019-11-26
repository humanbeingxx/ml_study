# coding: utf-8

import numpy as np
import data_loader
from sklearn import svm


def _test_svm():
    X = [[0, 0],[1, 1]]
    y = [0, 1]
    model = svm.SVC(gamma="scale")
    model = model.fit(X, y)
    print(model.support_vectors_)

def _test_one_against_one():
    X = [[0, 0], [1, 1], [2, 2], [3, 3]]
    y = [1, 2, 3, 4]
    model = svm.SVC(gamma="scale", decision_function_shape="ovr")
    model = model.fit(X, y)
    print(model.support_vectors_)
    print(model.predict([[-0.1, -0.1], [1.1, 1.1], [2.1, 2.1], [4, 4]]))


def training():
    traing_data = data_loader.load_training_data()
    model = svm.SVC(gamma="scale", decision_function_shape="ovo").fit(traing_data[0], traing_data[1])
    return model


if __name__ == "__main__":
    # _test_svm()
    # _test_one_against_one()
    model = training()
    test_data = data_loader.load_test_data()
    predicts = model.predict(test_data[0])
    print(len([tup for tup in zip(test_data[1], predicts) if tup[0] == tup[1]]) / len(test_data[1]))