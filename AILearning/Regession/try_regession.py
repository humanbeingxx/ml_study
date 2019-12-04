# coding: utf-8

from sklearn import linear_model
import matplotlib.pyplot as plt
import sys

sys.path.append("../utils")

import learn_curve
import data_loader

data = data_loader.load_data("../../source_data/Regression/data.txt", 2, "\t")


def show_data():
    plt.scatter(data[0][:, 1], data[1])
    plt.show()


def train():
    training_data = data[0][0:140]
    training_value = data[1][0:140]

    model = linear_model.LinearRegression()
    model.fit(training_data, training_value)


def predict(model, data, test_value):
    test_data = data[0][141:200]
    test_value = data[1][141:200]

    predicts = model.predict(test_data)
    plt.scatter(test_data[:, 1], test_value)
    plt.scatter(test_data[:, 1], predicts)
    plt.show()


def diff_calculator(predicts, values):
    return sum([pow(tup[0] - tup[1], 2) for tup in zip(predicts, values)]) / 2


if __name__ == "__main__":
    training_data = data[0][0:140]
    training_value = data[1][0:140]
    test_data = data[0][141:200]
    test_value = data[1][141:200]
    learn_curve.get_learning_curve_regession(
        0.5,
        0.1,
        linear_model.LinearRegression(),
        training_data,
        training_value,
        test_data,
        test_value,
        diff_calculator
    )
