import random
import sys
from datetime import datetime

# random.seed(0)


def force_compare(data):
    data_length = len(data)
    ele_length = len(data[0])
    same_pair = []
    for i in range(0, data_length):
        for j in range(i + 1, data_length):
            is_same = True
            for one_pair in zip(data[i], data[j]):
                if one_pair[0] != 'x' and one_pair[1] != 'x' and one_pair[0] != one_pair[1]:
                    is_same = False
                    break
            if is_same:
                same_pair.append((i, j))
    return same_pair


def generate_data():
    meta = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'x']
    data = []
    for i in range(0, 10):
        one_data = []
        for i in range(0, 5):
            randi = random.randint(0, 30)
            if randi >= 7:
                one_data.append('x')
            else:
                one_data.append(meta[randi])
        data.append(one_data)
    return data


def generate_big_data():
    meta = []
    for i in range(0, 300):
        meta.append(str(i))
    meta.append('x')
    data = []
    for i in range(0, 10000):
        one_data = []
        for i in range(0, 15):
            randi = random.randint(0, 600)
            if randi >= 300:
                one_data.append('x')
            else:
                one_data.append(meta[randi])
        data.append(one_data)
    return data


def collection_based_compare(data):
    ele_length = len(data[0])
    merged = set()
    for index in range(0, ele_length):
        column_data = [line[index] for line in data]
        start = datetime.now()
        same_pairs = process_column(column_data)
        print(str.format("process_column cost {}",
                (datetime.now() - start).seconds))
        if not merged:
            merged = same_pairs
        else:
            start = datetime.now()
            merged = merge_same(merged, same_pairs)
            print(str.format("merge cost {}", (datetime.now() - start).seconds))
        merged = remove_single(merged)
        print("finish one column")
    return merged


def merge_same(merged, same_pairs):
    return merged & same_pairs


def process_column(column_data):
    x_set = set()
    no_x_set = {}
    for i in range(0, len(column_data)):
        if column_data[i] == 'x':
            x_set.add(i)
        else:
            if not column_data[i] in no_x_set:
                no_x_set[column_data[i]] = set()
            no_x_set[column_data[i]].add(i)
    # mix_x_set = {}
    # for key in no_x_set:
    #     mix_x_set[key] = no_x_set[key] | x_set
    # mix_x_set_values = list(mix_x_set.values())
    print("before generate")
    return generate_same_pair_each_column(no_x_set.values(), x_set)

    # return remove_single(mix_x_set_values)

def generate_same_pair_each_column(no_x_set, x_set):
    no_x_pairs = generate_same_pair(no_x_set)
    all_ele = set()
    for one_set in no_x_set:
        all_ele = all_ele | one_set
    print("finish no_x_set")
    mix_x_pairs = generate_same_pair([all_ele | x_set])
    print("finish mix_x_pairs")
    return no_x_pairs | mix_x_pairs


def remove_single(data):
    data = set(filter(not_single, data))
    return data


def not_single(data):
    return len(data) > 1


def generate_same_pair(collections):
    pairs = set()
    for collection in collections:
        collection = sorted(list(collection))
        length = len(collection)
        for i in range(0, length):
            for j in range(i + 1, length):
                pairs.add((collection[i], collection[j]))
    return pairs


def check_same_result(data):
    start = datetime.now()
    force_same = force_compare(data)
    force_same = set(force_same)
    force_cost = (datetime.now() - start).seconds
    print(str.format("force cost {}", force_cost))

    start = datetime.now()
    collection_based = collection_based_compare(data)
    collection_based = generate_same_pair(collection_based)
    collection_based_cost = (datetime.now() - start).seconds
    print(str.format("collection_based_cost {}", collection_based_cost))

    return force_same == collection_based


if __name__ == "__main__":
    data = generate_big_data()

    new_same = collection_based_compare(data)

    # for i in range(0, 1):
    #     checked = check_same_result(data)
    #     if not checked:
    #         sys.exit(1)
