# coding: utf-8

import sys

sys.path.append("../utils")

import data_loader
import learn_curve
from sklearn import ensemble
from sklearn import preprocessing

training_data_path = "../../source_data/Boosting/horseColicTraining.txt"
test_data_path = "../../source_data/Boosting/horseColicTest.txt"

training_data = data_loader.load_data(training_data_path, 21, "\t")
test_data = data_loader.load_data(test_data_path, 21, "\t")

classifier = ensemble.AdaBoostClassifier(n_estimators=100)

training_features = preprocessing.scale(training_data[0])
test_features = preprocessing.scale(test_data[0])

learn_curve.get_learning_curve(0.1, 0.01, classifier, training_features, training_data[1], test_features, test_data[1])
