# Computes idf of features to use for feature values for sentiment classifier dataset.


import lib.utility as u
import math


if __name__ == "__main__":
    corpus = u.get_lines("train-sample.txt")
    
    # get total count of all docs
    total_docs = len(corpus)
    
    # get features from feat-space file
    features = {}
    with open("feat-space-sent-prefix.txt") as file:
        line = file.readline()
        for term in line.strip().split():
            features[term] = 0
    
    # go through corpus and count in how many docs each term appears
    for line in corpus:
        # we need to remove all the labels and ":1" after each term on each line
        line = set(line.split()[1:])
        
        # go through each line as a set - so no duplicates
        for term in line:
            term = term.split(":")[0]
            try:
                features[term] += 1
            except:
                #print term, "not in feature space"
                continue
    
    
    # Print term frequencies to file
    with open("term-freqs.txt", "w") as file:
        for key, value in features.iteritems():
            print key, value
    
    
    #with open("term-idf2.txt", "w") as file:
    #    i = 0
    #    for key in sorted(features, key=features.get, reverse=True):
    #        #if i == 100:
    #        #    break
    #        t_count = features[key]
    #        idf = 1.0 * (math.log10((total_docs + 1)/(float(t_count) + 1)))
    #        
    #        #print key, features[key], idf
    #        file.write(key + " " + str(idf) + "\n")
    #        
    #        i += 1
    