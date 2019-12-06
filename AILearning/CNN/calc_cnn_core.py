# coding: utf-8

import numpy as np


def calc_core(data, core):
    size = (data.shape[0] - core.shape[0] + 1,
            data.shape[1] - core.shape[1] + 1)
    new_data = np.zeros(size)
    for j in range(size[1]):
        for i in range(size[0]):
            sub_data = data[i: i + core.shape[0], j: j + core.shape[1]]
            new_data[i][j] = (sub_data * core).sum()
    return new_data


def calc_one_point(part_data, core):
    sum_value = 0
    for i in range(0, core.shape[0]):
        for j in range(0, core.shape[1]):
            sum_value += part_data[i][j] * core[i][j]
    return sum_value / core.sum()


if __name__ == "__main__":
    data = np.array([[1, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0], [0, 0, 1, 0]])
    core1 = np.array([[1, -1], [1, -1]])
    core2 = np.array([[1, 1], [-1, -1]])
    
    print(calc_core(data, core1))
    print(calc_core(data, core2))
