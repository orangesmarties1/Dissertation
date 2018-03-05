# Sentiment classifier (using logistic regression) for evaluation of ClassiNet and other algorithms.


import lib.utility as u
import numpy
from sklearn.linear_model import LogisticRegression


def calculate_accuracy(labels, results, title):
    """
    Calculates and prints classification accuracy (overall, positive, and negative).
    """
    pos_correct = 0
    pos_total = 0
    neg_correct = 0
    neg_total = 0
    total = len(labels)
    
    # Array for indices of incorrect classifications
    incorrect = []
    
    # Count results
    for i in xrange(total):
        #print i
        if labels[i] == 1:
            if results[i] == labels[i]:
                pos_correct += 1
            else:
                #print "incorrect", i
                incorrect.append(i)
            pos_total += 1
        else:
            if results[i] == labels[i]:
                neg_correct += 1
            else:
                #print "incorrect", i
                incorrect.append(i)
            neg_total += 1
    
    print "# Results for:", title
    print "Accuracy:", ((pos_correct + neg_correct) / float(total))*100
    print "Pos accuracy:", (pos_correct / float(pos_total))*100
    print "Neg accuracy:", (neg_correct / float(neg_total))*100
    print ""
    
    return incorrect


if __name__ == "__main__":
    train_data_file = "train-2000.txt"
    test_data_file = "test-full.txt"
    #test_data_file = "output-700/expanded-data/test-all-neighb.txt"
    
    # Get feature space
    features_index = u.read_features_file("feat-space-sent-prefix.txt")
    feature_size = len(features_index)
    
    # Get idf values for features
    term_idf = {}
    with open("term-idf.txt") as file:
        for line in file:
            line = line.strip().split()
            term_idf[line[0]] = float(line[1])
    
    
    ## SCL addition
    # load in the learnt features for train and test into separate arrays
    # gamma = scaling factor
    gamma = 2.2
    
    train_new_feats = []
    with open("scl-proj-feats-train2.txt") as file:
        for line in file:
            v = []
            line = line.strip().split()
            for x in line:
                v.append(gamma * float(x))
            train_new_feats.append(v)
    
    test_new_feats = []
    with open("scl-proj-feats-test.txt") as file:
        for line in file:
            v = []
            line = line.strip().split()
            for x in line:
                v.append(gamma * float(x))
            test_new_feats.append(v)
    ## end SCL addition
    
    
    # Get train data
    print "Getting train data..."
    train_data = []
    train_labels = []
    f = 0.2 # factor to weight feature values
    threshold = 0.65
    count = 0
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
            
            # get SCL learnt new feats for current instance
            new_feats = train_new_feats[count]
            # concatenate with original feat vect
            new_vect = numpy.concatenate((vect, new_feats))
            
            train_data.append(new_vect)
            
            # add label to array
            if l[0] == "+1":
                train_labels.append(1)
            else:
                train_labels.append(0)
            
            count += 1
    
    
    # run model on train data
    # Scikit-learn Logistic Regression
    # train a model to predict using dataset created above
    print "Training model..."
    logreg = LogisticRegression(fit_intercept=False)
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
    # arrays for splits of test data (depending on sentence length)
    test_data_1 = []
    test_labels_1 = []
    test_data_2 = []
    test_labels_2 = []
    test_data_3 = []
    test_labels_3 = []
    test_data_4 = []
    test_labels_4 = []
    # set to false to do only overall evaluation
    test_split = False
    
    f = 0.1 # factor to weight feature values
    threshold = 0
    count = 0
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
            
            # get SCL learnt new feats for current instance
            new_feats = test_new_feats[count]
            # concatenate with original feat vect
            new_vect = numpy.concatenate((vect, new_feats))
            
            # add vect to array
            test_data.append(new_vect)
            
            # add label to array
            if l[0] == "+1":
                test_labels.append(1)
            else:
                test_labels.append(0)
            
            count += 1
    
    # Predict results of full test set
    print "Testing model...\n"
    y = logreg.predict(test_data)
    
    # Calculate accuracy of full set
    # method returns list of incorrect classifications (we just ignore here)
    _wrong = calculate_accuracy(test_labels, y, "all")
    
    #print len(_wrong)
    
    # Print indices of misclassified to file
    #with open("output-700/mis-scl.txt", "w") as file:
    #    for x in _wrong:
    #        file.write(str(x) + "\n")
    
    
    # Calculate accuracy for all splits - if in that mode
    if test_split:
        # predict split 1
        y_1 = logreg.predict(test_data_1)
        _ = calculate_accuracy(test_labels_1, y_1, "split-1")
        
        # predict split 2
        y_2 = logreg.predict(test_data_2)
        _ = calculate_accuracy(test_labels_2, y_2, "split-2")
        
        # predict split 3
        y_3 = logreg.predict(test_data_3)
        _ = calculate_accuracy(test_labels_3, y_3, "split-3")
        
        # predict split 4
        y_4 = logreg.predict(test_data_4)
        _ = calculate_accuracy(test_labels_4, y_4, "split-4")
    