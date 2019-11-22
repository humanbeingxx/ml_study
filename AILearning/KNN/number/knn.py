# coding: utf-8

import numpy
from collections import Counter
import functools

def knn(newData, dataSet, labels):
    dataSize = len(dataSet)
    diffMat = (numpy.tile(newData, (dataSize, 1)) - dataSet) ** 2
    distances = diffMat.sum(axis = 1)
    distances = distances ** 0.5

    withLabels = list(zip(distances, labels))
    withLabels = sorted(withLabels, key=functools.cmp_to_key(_cmp))[0:100]
    kLabels = [tup[1] for tup in withLabels]
    return Counter(kLabels).most_common(1)[0][0]

def _cmp(tup1, tup2):
    if tup1[0] > tup2[0]:
        return 1
    if tup1[0] < tup2[0]:
        return -1
    return 0