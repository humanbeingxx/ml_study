# coding: utf-8

import matplotlib.pyplot as plt

def get_learning_curve(start_rate, use_rate, model_generator, training_data, training_labels, test_data, test_labels):
    training_accurancies = []
    test_accurancies = []
    used = start_rate
    while used <= 1:
        used_len = int(len(training_data) * used)
        use_training_data = training_data[0:used_len]
        use_training_labels = training_labels[0:used_len]
        model = model_generator.fit(use_training_data, use_training_labels)
        training_predicts = model.predict(training_data)
        test_predicts = model.predict(test_data)
        training_accurancy = calc_accurancy(training_predicts, use_training_labels)
        test_accurancy = calc_accurancy(test_predicts, test_labels)
        # print(training_accurancy)
        # print(test_accurancy)
        training_accurancies.append((used_len, training_accurancy))
        test_accurancies.append((used_len, test_accurancy))
        used += use_rate
    plt.plot([tup[0] for tup in training_accurancies], [tup[1] for tup in training_accurancies])
    plt.plot([tup[0] for tup in test_accurancies], [tup[1] for tup in test_accurancies])
    plt.show()

def calc_accurancy(predicts, labels):
    return len([tup for tup in zip(predicts, labels) if tup[0] == tup[1]]) / len(labels)

if __name__ == "__main__":
    import sys
    sys.path.append('../RandomForest')
    import data_loader
    data = data_loader.load_data()
    training_data = data[0]
    training_labels = data[1]
    test_data = data[2]
    test_labels = data[3]

    from sklearn import ensemble
    from sklearn.model_selection import cross_val_score

    model_generator = ensemble.RandomForestClassifier()
    get_learning_curve(0.1, 0.1, model_generator, training_data, training_labels, test_data, test_labels)
