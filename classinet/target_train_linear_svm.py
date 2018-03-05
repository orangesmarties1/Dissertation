# Train binary predictors for each target word using scikit-learn library (logistic regression).
# CHANGED line 64 weight_vector_dir to weight_vect_dir

import config as c
import nltk
import numpy
import math
from sklearn import svm
import pickle
import os
import read as r
import get as g

def train_clf(target):
    # Load feature space and target words
    features_index = r.read_features_file(c.output_dir + "feat-space.txt")
    feature_size = len(features_index) #5000 features
    target_words = g.get_target_words()
    target_count = 0
    

    target_count += 1
    print target
        
    # Path to train data
    path = c.train_data_dir + target + ".txt"
        
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
    
    # Train predictor using scikit-learn lSVM classification
    clf = svm.SVC(kernel='linear', C = 1.0, probability = False)
    clf.fit(data, labels)
    
    # Dump trained classifiers to pickle files
    output = open(c.clf_dir + target + ".pkl", "wb")
    # PIckle dictionary using protocol 0
    pickle.dump(clf, output)

      
    print 'Training done for', target
    #print ""
    