# coding: utf-8

import apriori

def generateRules(L, support_data, minConf=0.7):
    bigRuleList = []
    for i in range(1, len(L)):
        # 获取频繁项集中每个组合的所有元素
        for freqSet in L[i]:
            H1 = [frozenset([item]) for item in freqSet]
            if (i > 1):
                rules_from_conseq(freqSet, H1, support_data, bigRuleList, minConf)
            else:
                calc_conf(freqSet, H1, support_data, bigRuleList, minConf)
    return bigRuleList


def calc_conf(freqSet, H1, support_data, bigRuleList, minConf):
    retList = []
    for item in H1:
        conf = support_data[freqSet] / support_data[freqSet - item]
        if conf >= minConf:
            bigRuleList.append((freqSet - item, item, conf))
            retList.append(item)
    return retList

def rules_from_conseq(freqSet, H, support_data, bigRuleList, minConf):
    hmp1 = apriori.aprioriGen(H)
    if len(freqSet) == len(hmp1[0]):
        return
    hmp1 = calc_conf(freqSet, hmp1, support_data, bigRuleList, minConf)
    if len(hmp1) == 1:
        return
    else:
        rules_from_conseq(freqSet, hmp1, support_data, bigRuleList, minConf)

if __name__ == "__main__":
    origin_data = [[1,3,4],[2,3,5],[1,2,3,5],[2,5]]
    L, support_data = apriori.apriori(origin_data, 0.5)
    rules = generateRules(L, support_data, 0.5)
    print(rules)