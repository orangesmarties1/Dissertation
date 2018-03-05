# Train binary predictors for each target word using scikit-learn library (logistic regression).
# CHANGED line 64 weight_vector_dir to weight_vect_dir

import config as f
import nltk
import numpy
import math
from sklearn import svm
from sklearn.grid_search import GridSearchCV
from sklearn.svm import SVC
from sklearn import preprocessing
import os
from time import time
import read as r
import get as g



def train_clf(target):
    # Load feature space and target words
    print 'hello'

    
    # Load feature space and target words
    features_index = r.read_features_file(f.output_dir + "feat-space.txt")
    feature_size = len(features_index) #5000 features
    target_words = g.get_target_words()
    target_count = 0
    

    target_count += 1
    print target
        
    # Path to train data
    path = f.train_data_dir + target + ".txt"
        
    # Open train data file and build binary feature vectors vectors
    # Arrays for vectors and labels
    data = []
    labels = []
    with open(path) as file:
        for line in file:
            # create binary feature vector
            vect = numpy.zeros(feature_size)
            l = line.strip().split()
            for word in l[1:]:
                # don't include target word in feature vector
                if word != target:
                    try:
                        vect[features_index[word]] = 1
                    except:
                        #print "Not found in features:", word
                        pass
            data.append(vect)
                
            # add label to array
            if l[0] == "+1":
                labels.append(1)
            else:
                labels.append(0)
    
    # Train predictor using scikit-learn SVM classification
    print 'Fitting the classifier to the training set'
    t0 = time()
    #data = preprocessing.scale(data)
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1] }
    clf = GridSearchCV(svm.SVC(kernel = 'rbf', class_weight='balanced'), param_grid)
    print 'so far so good'
    clf = clf.fit(data, labels)
    print 'fitting done'
    total_time = time() - t0
    print 'Done in ', total_time/60, 'minutes'
    print 'Best estimator found by grid search:'

    print clf.best_estimator_
    print
    print 'Best params found: '
    print clf.best_params_
    

train_clf('ill')