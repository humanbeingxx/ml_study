# coding: utf-8


def createC1(dataSet):
    C1 = []
    for data in dataSet:
        for item in data:
            if not [item] in C1:
                C1.append([item])

    return list(map(frozenset, C1))


def scanD(D, Ck, minSupport):
    ssCnt = {}
    for c in Ck:
        for d in D:
            if c.issubset(d):
                if c in ssCnt:
                    ssCnt[c] += 1
                else:
                    ssCnt[c] = 1

    dataSize = float(len(D))
    supportData = {}
    retList = []
    for key in ssCnt:
        support = ssCnt[key] / dataSize
        if support >= minSupport:
            retList.append(key)
        supportData[key] = support

    return retList, supportData


def aprioriGen(Lk):
    retList = []
    len_lk = len(Lk)
    for i in range(0, len_lk):
        for j in range(i + 1, len_lk):
            set_sub = Lk[j] - Lk[i]
            if len(set_sub) == 1:
                newData = Lk[i] | set_sub
                if not newData in retList:
                    retList.append(newData)

    return retList


def apriori(origin_data, minSupport=0.5):
    L = []
    support_data = {}
    data_k = createC1(origin_data)
    for i in range(0, len(data_k) - 1):
        data_k, support_k = scanD(origin_data, data_k, minSupport)
        if data_k:
            L.append(data_k)
        if support_k:
            support_data.update(support_k)
        data_k = aprioriGen(data_k)
    return L, support_data


if __name__ == "__main__":
    origin_data = [[1, 2, 3], [1, 3], [1, 2], [3, 2, 0, 1]]
    L, support_data = apriori(origin_data, 0.3)
    print(L)
    print(support_data)
