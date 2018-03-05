# Tests similarity of the weight vectors learnt from the logistic regression.


import lib.utility as u
import numpy
import os


if __name__ == "__main__":
    dr = "output-100/weight-vectors-final-large"
    
    targets = []
    with open("output-100/target-words-sample2.txt") as file:
        for line in file:
            targets.append(line.strip().split()[0])
    
    weights = {}
    # open each txt file in directory (dr) and save contents to weights dictionary
    for f in os.listdir(dr):
        if f.endswith("txt"):
            with open(dr + "/" + f) as file:
                line = file.readline()
                l = line.strip().split()
                word = l[0]
                if word not in targets:
                    continue
                # we use the intercept too, as the first value in array for similarity computation
                weights[word] = numpy.array([float(x) for x in l[1:]])
    
    print len(weights)
    
    # compute similarity between with each item in dictionary
    for word, vector in weights.iteritems():
        print "----", word, "----"
        
        sims = {}
        for word2, vector2 in weights.iteritems():
            if word2 != word:
                sim = u.cosine_sim(vector, vector2)
                sims[word2] = sim
        
        c = 0
        # print in order of most related
        # reverse should be True for cosine sim, False for Euclidean dist
        for key in sorted(sims, key=sims.get, reverse=True):
            if c == 7:
                break
            print key, sims[key]
            c += 1
    