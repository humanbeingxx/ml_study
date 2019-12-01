# coding: utf-8

def calc_accurancy_callback(predicts, labels, pos_value, neg_value):
    tp = len([tup for tup in zip(predicts, labels) if tup[0] == tup[1] and tup[0] == pos_value])
    tn = len([tup for tup in zip(predicts, labels) if tup[0] == tup[1] and tup[0] == neg_value])
    tp = tn = fp = fn = 0
    for tup in zip(predicts, labels):
        if tup[0] == tup[1]:
            if tup[0] == pos_value:
                tp += 1
            elif tup[0] == neg_value:
                tn += 1
        else:
            if tup[0] == 1 and tup[1] == 0:
                fp += 1
            elif tup[0] == 0 and tup[1] == 1:
                fn += 1
    accurancy = tp / (tp + fp)
    callback = tp / (tp + fn)
    return accurancy, callback

def calc_f(predicts, labels, pos_value, neg_value):
    accurancy,callback = calc_accurancy_callback(predicts, labels, pos_value, neg_value)
    return 2 * accurancy * callback / (accurancy + callback)


if __name__ == "__main__":
    predicts = [0,0,1,1,0]
    labels = [0,1,1,1,0]
    print(calc_f(predicts, labels, 1, 0))