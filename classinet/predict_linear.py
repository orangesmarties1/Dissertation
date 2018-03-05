import utility as u
import config as c
import numpy
import sys
import itertools
import os
import time
import datetime

def predict_word_dataset(word, dataset):
    """
    Predicts presence of word in each instance in dataset, and returns results array.
    """
    # Get weight vector for word

    if os.path.isfile(c.pred_data + word + '.txt'):
        results = u.get_lines(c.pred_data + word + '.txt')
        return results

    else:
        start_time = time.clock()
        print 'starting training for', word, 'at:', datetime.datetime.now().time()
        clf = u.get_clf(word, 'linear')
    
        # Predict presence of word in each sentence, saving results
        results = clf.predict(dataset)
        print len(results)
        print
    
        with open(c.pred_data + word + '.txt', 'w') as file:
            file.write(word + ' ')
            for i in results:
                file.write(str(i))
                file.write('\n')
        
        time_taken = (time.clock()-start_time)/60
        print 'Time taken to train and write predictions to file for', word,
        print 'is:', time_taken, 'minutes'           
        return results



if __name__ == "__main__":
    # Read features and target words
    features_index = u.read_features_file(c.output_dir + "feat-space.txt")
    feat_size = len(features_index) #5000
    target_words = u.get_target_words() # len = 700
    
    # Set up two matrices - one for directed (asymmetric matrix) and one for undirected (symmetric matrix) agreements
    #dimensions = len(target_words)
    #SM = [[0.0000 for j in xrange(dimensions)] for i in xrange(dimensions)]
    #AM = [[0.0000 for j in xrange(dimensions)] for i in xrange(dimensions)]
    
    # Get pairs
    #pairs = u.get_lines(c.output_dir + "target-word-high-pairs.txt")
    
    # Arrays to hold agreements
    pos_agr_a = []
    cond_prob_a = []


    
    # Iterate through each pair, and compute two types of agreement
    # counter
    ctr=0
    #for pair in pairs
    for pair in itertools.combinations(target_words, r=2):
        #if ctr == 2:
        #    break
        ctr+=1

        # Get individual words
        #pair = pair.split()[0:2]
        ti = pair[0] # i
        tj = pair[1] # j
        print ctr, "- i:", ti, "j:", tj
        
        # Get row and col for matrix
        row = target_words.index(ti)
        col = target_words.index(tj)
        #print row, col
        
        # Read pair test dataset int sents array - file could be with words in reversed order
        dir = c.output_dir + "agreement-data/"
        sents = []
        try:
            sents = u.get_lines(dir + ti + "-" + tj + ".txt")
        except:
            try:
                sents = u.get_lines(dir + tj + "-" + ti + ".txt")
            except:
                # exit program if no file found for these words
                print "No dataset for:", ti, tj
                #sys.exit("Can't find dataset file. Program terminating.")
                continue
        
        # Convert sents to binary feature vectors
        data = []
        for sentence in sents:
            vect = numpy.zeros(feat_size)
            for w in sentence.strip().split()[1:]:
                # ignore target words in feature vectors
                if w not in pair:
                    try:
                        vect[features_index[w]] = 1
                    except:
                        pass
            data.append(vect)
        #print len(data)

        
        # Predict word occurring in dataset for both words in pair
        ti_results = predict_word_dataset(ti, data)
        tj_results = predict_word_dataset(tj, data)
