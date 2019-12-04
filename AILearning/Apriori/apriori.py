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

if __name__ == "__main__":
    origin_data = [[1,2,3],[0,1,2],[1,2],[3,2,0,1]]
    # origin_data = [[1],[1,2],[3,3,4]]
    # part_data = createC1(origin_data)
    # for item in part_data:
    #     print(item)
    # retList,_ = scanD(origin_data, part_data, 0.5)
    # print(retList)
    data = createC1(origin_data)
    print(scanD(origin_data, data, 0.1))
    data = aprioriGen(data)
    print(scanD(origin_data, data, 0.1))
    data = aprioriGen(data)
    print(scanD(origin_data, data, 0.1))
    data = aprioriGen(data)
    print(scanD(origin_data, data, 0.1))

