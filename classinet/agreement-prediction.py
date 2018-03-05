# Compute agreement for each pair of target words, using their predictions on
# a test set unique to the pair and a confusion matrix
# Start run: Sep 8th, 18:00
# End run: Sep 9th, 01:30


import lib.utility as u
import config as c
import numpy
import sys
import itertools
#from sklearn.metrics import confusion_matrix


def create_confusion_matrix(list1, list2):
    """
    Creates and returns a confusion matrix between two predictors, whose outputs
    are given in list1 and list2.
    """
    # the four values of the confusion matrix
    yy = 0
    yn = 0
    ny = 0
    nn = 0
    for index in xrange(len(list1)):
        val1 = int(list1[index])
        val2 = int(list2[index])

        # And add 1 to the correct counter depending on situation
        if val1 == 1:
            if val2 == 1:
                yy += 1
            else:
                yn += 1
        else:
            if val2 == 1:
                ny += 1
            else:
                nn += 1

    return [[yy, yn],[ny, nn]]


def get_word_dataset(word):
    """
    Predicts presence of word in each instance in dataset, and returns results array.
    """
    file_name = c.rbf_data + word + '.txt'

    # Get predicted classes for word
    results = u.get_lines(file_name)
    results = results[1:]

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

        
        # Predict word occurring in dataset for both words in pair
        ti_results = get_word_dataset(ti)
        tj_results = get_word_dataset(tj)
        
        # Create confusion matrix C with prediction results
        C = create_confusion_matrix(ti_results, tj_results)
        
        # Get access to each cell in confusion matrix
        yy = C[0][0]
        yn = C[0][1]
        ny = C[1][0]
        nn = C[1][1]
        total = float(yy + yn + ny + nn)
        
        # Compute agreements using confusion matrix values
        # Overall agreement
        agreement = (yy + nn) / total
        # Positive agreement

        pos_agreement = float("{0:.4f}".format(yy / float(yy + yn + ny)))
        # Conditional probability agreement
        jgiveni = yy / float(yy + yn)
        igivenj = yy / float(yy + ny)
        
        #print "agreement:", agreement
        #print "positive agreement:", pos_agreement
        #print "p(", tj, "|", ti, "):", jgiveni
        #print "p(", ti, "|", tj, "):", igivenj
        #print ""
        
        # Append agreement values to arrays
        # quite confusing, but remember the edge from x -> y is P(y|x)
        pos_agr_a.append(ti + " " + tj + " " + str(pos_agreement))
        cond_prob_a.append(ti + " " + tj + " " + str(jgiveni))
        cond_prob_a.append(tj + " " + ti + " " + str(igivenj))
        
        # Old method (using matrices) to save agreement values
        # for symmetric matrix undirected graph (we use positive agreement)
        #SM[row][col] = pos_agreement
        #SM[col][row] = pos_agreement
        # for asymmetric matrix for directed graph (we use conditional probs)
        #AM[row][col] = jgiveni
        #AM[col][row] = igivenj
        
        ctr+=1
    
    
    # Write edges to files directly from arrays
    # Positive agreement used for undirected edges
    # Undirected egdes weren't used in my project.
    #with open(c.output_dir + "edges-undirected-rbf.txt", "w") as file:
    #     for x in pos_agr_a:
    #        file.write(x + "\n")
    
    # Conditional probabilities used for directed edges
    with open(c.output_dir + "edges-directed-rbf.txt", "w") as file:
        for x in cond_prob_a:
            file.write(x + "\n")
    