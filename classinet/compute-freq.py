# Computes frequency of features (from feature space) in Large Movie Review dataset.


import lib.utility as u
import math


if __name__ == "__main__":
    corpus_neg = u.get_lines("imdb-all-sentences-neg.txt")
    corpus_pos = u.get_lines("imdb-all-sentences-pos.txt")
    corpus = corpus_neg + corpus_pos
    
    # get total count of all docs
    total_docs = len(corpus)
    print "total docs:", total_docs
    
    # get features from feat-space file
    features = {}
    with open("output-700/feat-space.txt") as file:
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
            file.write(key + ":" + str(value) + "\t")
    
    