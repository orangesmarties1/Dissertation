# Sentiment classifier (using logistic regression) for evaluation of ClassiNet and other algorithms.

# MULTICLASS for new updates - using neutral, positive, negative


import lib.utility as u
import numpy
from sklearn.linear_model import LogisticRegression


def calculate_accuracy(labels, results):
    """
    Calculates and prints classification accuracy (overall, positive, negative, neutral).
    """
    total = len(labels)
    
    pos_correct = 0
    pos_total = 0
    
    neg_correct = 0
    neg_total = 0
    
    neut_correct = 0
    neut_total = 0

    #
    # 0 = negative, 1 = positive, 2 = neutral
    #

    # Count results
    for i in xrange(total):
        #print i
        this_label = labels[i]

        if this_label == 0:
            # it's a negative...
            if results[i] == this_label:
                neg_correct += 1
            neg_total += 1
        elif this_label == 1:
            # it's a positive
            if results[i] == this_label:
                pos_correct += 1
            pos_total += 1
        else:
            # it's a neutral
            if results[i] == this_label:
                neut_correct += 1
            neut_total += 1
    
    print pos_total, neg_total, neut_total

    print "Accuracy:", ((pos_correct + neg_correct + neut_correct) / float(total))*100
    print "Pos accuracy:", (pos_correct / float(pos_total))*100
    print "Neg accuracy:", (neg_correct / float(neg_total))*100
    print "Neut accuracy:", (neut_correct / float(neut_total))*100
    print ""


if __name__ == "__main__":
    train_data_file = "train-output1.txt"
    #test_data_file = "wordnet-expanded-test.txt"
    #test_data_file = "output-700/expanded-data/test-expand-short-path1.txt"
    test_data_file = "test-output1.txt"
    
    # Get feature space
    features_index = u.read_features_file("feat-space-sent-prefix.txt")
    feature_size = len(features_index)
    
    # Get idf values for features
    term_idf = {}
    with open("term-idf.txt") as file:
        for line in file:
            line = line.strip().split()
            term_idf[line[0]] = float(line[1])
    
    # Get train data
    print "Getting train data..."
    train_data = []
    train_labels = []
    f = 0.2 # factor to weight feature values
    threshold = 0.65

    with open(train_data_file) as file:
        for line in file:
            # create binary feature vectors and add to array
            vect = numpy.zeros(feature_size)
            l = line.strip().split()
            for i in l[1:]:
                # we have to split on the ":" because of how we've set up the data
                i = i.split(":")
                word = i[0]
                value = float(i[1])
                
                # get idf value from dict
                try:
                    idf = term_idf[word]
                except:
                    idf = 1.0
                
                # original features will have value of 1
                # and expanded features will have value < 1
                if value == 1:
                    try:
                        vect[features_index[word]] = value * idf
                    except:
                        pass
                elif value >= threshold:
                    try:
                        vect[features_index[word]] = value * f * idf
                    except:
                        pass
            
            train_data.append(vect)

            # add label to array
            if l[0] == "positive":
                train_labels.append(1)
            elif l[0] == "negative":
                train_labels.append(0)
            else:
                train_labels.append(2)
    
    
    # run model on train data
    # Scikit-learn Logistic Regression
    # train a model to predict using dataset created above
    print "Training model..."
    logreg = LogisticRegression(
        fit_intercept=True,
        multi_class='multinomial',
        solver='newton-cg'
    )
    
    logreg.fit(train_data, train_labels)
    
    w = logreg.coef_
    try:
        b = logreg.intercept_[0]
    except:
        b = 0.0
    
    # Get test dataset
    print "Getting test data..."
    # array for all test data
    test_data = []
    test_labels = []
    
    f = 0.15 # factor to weight feature values
    threshold = 0
    with open(test_data_file) as file:
        for line in file:
            # create binary feature vectors and add to array
            vect = numpy.zeros(feature_size)
            l = line.strip().split()
            # log length of sentence
            s_len = 0
            
            for i in l[1:]:
                i = i.split(":")
                word = i[0]
                value = float(i[1])
                
                # get idf value from dict
                try:
                    idf = term_idf[word]
                except:
                    idf = 1.0
                
                # original features will have value of 1
                # and expanded features will have value < 1
                if value == 1:
                    try:
                        vect[features_index[word]] = value * idf
                    except:
                        pass
                    # add one to length of sentence
                    s_len += 1
                elif value >= threshold:
                    try:
                        vect[features_index[word]] = value * f * idf
                    except:
                        pass
            
            # Get label, then add vect and label to array
            test_data.append(vect)

            # add label to array
            if l[0] == "positive":
                test_labels.append(1)
            elif l[0] == "negative":
                test_labels.append(0)
            else:
                test_labels.append(2)
    
    
    # Predict results of full test set
    print "Testing model...\n"
    y = logreg.predict(test_data)
    
    print "Results..."
    print y
    print "Labels..."
    print test_labels

    # Calculate accuracy
    calculate_accuracy(test_labels, y)
    
    