import sys
from datetime import datetime
import test_compare


def generateDiffSet(data):
    column_num = len(data[0])
    diff_set = set()
    for i in range(column_num - 1, -1, -1):
        column = [(ele[0], ele[1][i]) for ele in enumerate(data)]
        start = datetime.now()
        diff = generateDiffSetOneColumn(column)
        print("generateDiffSetOneColumn cost {}, diff size {}".format((datetime.now() - start).seconds, len(diff)))
        start = datetime.now()
        if diff:
            diff_set.update(diff)
        print("update diff cost {}, diff size {}".format((datetime.now() - start).seconds, len(diff)))
    return diff_set


def generateDiffSetOneColumn(column_data):
    not_x = [ele for ele in column_data if ele[1] != 'x']
    dict = {}
    for ele in not_x:
        if ele[1] not in dict:
            dict[ele[1]] = [ele[0]]
        else:
            dict[ele[1]].append(ele[0])
    diff = list(dict.values())

    diff_set = set()
    if(len(diff) <= 1):
        return diff_set
    for i in range(0, len(diff) - 1):
        for j in range(i+1, len(diff)):
            diff_set.update(generatePair(diff[i], diff[j]))
    return diff_set

def generatePair(A, B):
    pairs = set()
    for a in A:
        for b in B:
            if a > b:
                pairs.add((b, a))
            else:
                pairs.add((a, b))
    return pairs


if __name__ == "__main__":
    for i in range(0, 10):
        data = test_compare.generate_data()

        force_diff = test_compare.force_compare(data)

        diff_set = generateDiffSet(data)

        new_diff = list(diff_set)
        new_diff.sort()

        if not force_diff == new_diff:
            sys.exit(1)
        
    data = test_compare.generate_big_data()
    generateDiffSet(data)

