# Here we try to figure out how often positive instances are expanded with 'positive' words
# and the same for negative instances.


import math


if __name__ == "__main__":
    # Read targets (but store in separate arrays for pos/neg)
    pos_targets = {}
    neg_targets = {}
    half = 99
    c = 0
    with open("../_700/target-words-test.txt") as file:
        for line in file:
            #print c
            line = line.strip().split()
            term = line[0]
            score = float(line[1])
            
            if c > half:
                pos_targets[term] = score
            else:
                neg_targets[term] = score
            c += 1
    
    # Now read in expanded data and log what we're expanding it with
    # let's try by just having a look at percentage of 'correct' expansion in terms of sentiment
    pos_percentages = []
    neg_percentages = []
    
    z = 0.01
    mp = "test-mutual-predicted.txt"
    all = "test-all-neighbs.txt"
    nb = "test-bayesian.txt"
    with open("../_700/tree-test/" + nb) as file:
        for line in file:
            data = line.strip().split()
            
            pos_terms = 0
            neg_terms = 0
            
            for x in data[1:]:
                term = x.split(":")[0]
                if term in pos_targets: 
                    # then check that it's sufficiently weighted (to iron out the features
                    # that aren't heavily associated with either pos/neg)
                    if pos_targets[term] >= z:
                        pos_terms += 1
                elif term in neg_targets:
                    # and check weight again
                    if neg_targets[term] <= (-1*z):
                        neg_terms += 1
            
            # get label
            label = data[0]
            
            # work out percentage of 'correct' expanded features based on current class
            total = float(pos_terms + neg_terms)
            # skip if total is 0
            if total != 0:
                if label == "+1":
                    percentage = (pos_terms / total) * 100
                    pos_percentages.append(percentage)
                else:
                    percentage = (neg_terms / total) * 100
                    neg_percentages.append(percentage)
    
    print "Pos average percentage"
    print sum(pos_percentages)/float(len(pos_percentages))
    
    print "Neg average percentage"
    print sum(neg_percentages)/float(len(neg_percentages))
    
    