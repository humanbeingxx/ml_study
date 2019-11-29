# coding: utf-8

from collections import Counter
from math import log


def calculate_shannon(data_set):
    labels = [data[-1] for data in data_set]
    counts = Counter(labels).most_common()
    data_size = len(data_set)
    result = 0.0
    for count in counts:
        p = float(count[1]) / data_size
        result -= p * log(p, 2)
    return result


def splitDataSet(data_set, index, specified_value):
    specified_data = [data for data in data_set if data[index] == specified_value]
    return [data[0: index] + data[index + 1: len(data)] for data in specified_data]

def calculate_feature_shanon(data_set, index):
    feature_values = [data[index] for data in data_set]
    data_size = len(data_set)
    value_counts = Counter(feature_values).most_common()

    result = 0.0
    for count_pair in value_counts:
        value = count_pair[0]
        count = count_pair[1]
        p = float(count) / data_size
        split_data_set = splitDataSet(data_set, index, value)
        shannon = calculate_shannon(split_data_set)
        result += p * shannon
    return result


def chooseBestSplit(data_set):
    feature_num = len(data_set[0]) - 1
    data_size = len(data_set)
    bestIndex = -1
    bestInfo = 1
    for index in range(0, feature_num):
        shannon = calculate_feature_shanon(data_set, index)
        if shannon < bestInfo:
            bestInfo = shannon
            bestIndex = index
    
    return bestIndex

        

if __name__ == "__main__":
    data_set = [[1,2,3], [1,2,3], [1,3,4]]
    print(splitDataSet(data_set, 1, 2))
    print(calculate_shannon(data_set))
    print(chooseBestSplit(data_set))