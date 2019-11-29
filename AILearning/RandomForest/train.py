# coding: utf-8

import data_loader
from sklearn import ensemble
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing

data = data_loader.load_data()
train_data = data[0]
train_labels = data[1]
test_data = data[2]
test_labels = data[3]

classifier = ensemble.RandomForestClassifier()
train_data = preprocessing.scale(train_data)

classifier = classifier.fit(train_data, train_labels)

test_data = preprocessing.scale(test_data)
predicts = classifier.predict(test_data)

print(predicts)
print(test_labels)
print(len([tup for tup in zip(predicts, test_labels) if tup[0] == tup[1]]) / len(test_labels))