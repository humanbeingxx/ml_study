# coding: utf-8

import numpy

def parse_dating_data(dataPath):
    with open(dataPath) as input:
        data = input.readlines()
        features = numpy.zeros((len(data), 3))
        labels = numpy.zeros(len(data))
        index = 0
        for line in data:
            split = line.replace("\n", "").split("\t")
            features[index, :] = split[0:3]
            labels[index] = split[3]
            index += 1
    return features, labels

def norm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normData = (dataSet - minVals) / ranges
    return normData