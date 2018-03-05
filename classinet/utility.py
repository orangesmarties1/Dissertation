# Some methods commonly used in various scripts.


import config as c
import numpy
import pprint, pickle
import target_train_linear_svm as t
import target_train_rbf as r


def predict(x, w, b):
    """
    Returns classifier prediction for x using w (weights) and b (bias).
    """
    return sigmoid(numpy.dot(x, w) + b)


def sigmoid(x):
    """
    Returns the y value for x in sigmoid function.
    """
    y = 1 / float(1 + numpy.exp(-1 * x))
    return y


def get_clf(word, kernel):
    
    if kernel == 'linear':
        t.train_clf(word)
    elif kernel == 'rbf':
        r.train_clf(word)
    
    pkl_file = open(c.clf_dir + word + '.pkl', 'rb')
    clf = pickle.load(pkl_file)
    print 'classifier loaded to pickle file'
    pprint.pprint(clf)

    return clf


def get_weight_matrix(target_words):
    """
    Creates weight matrix where rows are weight vectors of all target_words.
    Returns both the weight matrix and an array of bias terms.
    """
    weights = []
    bias = []
    for word in target_words:
        w = get_weight_vector(word, False)
        weights.append(w[1:])
        bias.append(w[0])
    
    return numpy.array(weights), bias


# returns array of target words from file
def get_target_words():
    """
    Simply returns array of target words.
    """
    t = []
    with open(c.output_dir + "target-words.txt") as file:
        for line in file:
            # only take first item (word) in line
            t.append(line.strip().split()[0])
    return t


def read_features_file(file_name):
    """
    Returns a dict of features from file_name in format {'feature': 'id'}.
    """
    # read features in as a set
    f = set()
    with open(file_name) as file:
        for line in file:
            for w in line.strip().split():
                f.add(w)
    
    # convert to hash table for quicker access
    index = {}
    counter = 0
    for (id, val) in enumerate(list(f)):
        index[val] = id

    return index


def cosine_sim(x, y):
    """
    Returns cosine similarity of two vectors x and y.
    """
    d = numpy.dot(x, y)
    x = numpy.linalg.norm(x)
    y = numpy.linalg.norm(y)
    return (d / (x * y))


def euclidean_dist(x, y):
    """
    Returns Euclidean distance of two vectors x and y.
    """
    a = x / numpy.linalg.norm(x)
    b = y / numpy.linalg.norm(y)
    return numpy.linalg.norm(a-b)


def get_lines(file_name):
    """
    Returns array of stripped lines from file_name.
    """
    s = []
    with open(file_name) as file:
        #s = file.readlines()
        for line in file:
            s.append(line.strip())
    return s
