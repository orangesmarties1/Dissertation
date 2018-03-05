# FTS (frequent term sets) implementation for feature expansion.

# Note:
# support is defined as: number of docs containing term set T / total docs
# confidence is defined as: number of docs containing term t in class c / total docs containing t
# class orientation is defined as: if term t has confidence in class c, then it's orientation is class c


import itertools


def count_pos_neg_occurrences():
    """
    Creates and returns w, a dict containing word occurrences in format:
    word: [pos_count, neg_count].
    """
    # Word occurrence dict
    w = {}
    
    # Iterate pos and neg data, adding one to corresponding value in dict
    # for each word we encounter
    for label in xrange(0,2):
        for x in corpus[label]:
            x_set = set(x)
            for j in x_set:
                try:
                    word_list = w[j]
                except:
                    word_list = [0, 0]
                word_list[label] += 1
                w[j] = word_list
    
    # remove <NUM> feat
    del w["<NUM>:1"]
    
    return w


def compute_confidences():
    """
    Computes confidence for each word in pos and neg, then saves their class
    orientation in c, where:
    0  means none (balanced occurrences)
    +1 means positive orientation
    -1 means negative orientation
    """
    # Class orientation dict
    c = {}
    
    # Iterate each word, and compute its orientation
    for key, value in words.iteritems():
        pos_count = value[0]
        neg_count = value[1]
        total_count = float(pos_count+neg_count)
        
        # Compute both confidences
        pos_conf = pos_count / total_count
        neg_conf = neg_count / total_count
        
        # Determine orientation based on confidences
        class_orient = 0
        if pos_conf > conf:
            class_orient = 1
        elif neg_conf > conf:
            class_orient = -1
        
        c[key] = class_orient
    
    #print c
    return c


def get_frequent_sets():
    """
    Finds frequent single and double term sets in corpus and returns them
    as s_1 and s_2, respectively.
    """
    # Single term sets
    s_1 = set()
    #print "finding single term sets..."
    
    # Iterate terms to find frequent single term sets
    for term, value in words.iteritems():
        # Get support and class orientation for current term
        this_support = value[0]+value[1]
        this_class = word_classes[term]
        #print term, this_support, this_class
        
        # If support is >= threshold and class orientation is not 0 (meaning it's above threshold
        # for some class) then we add it as a frequent term
        if this_support >= min_sup and this_class != 0:
            s_1.add(term)
    
    #print s_1
    
    # Double term sets
    s_2 = set()
    #print "finding double term sets..."
    
    # Iterate pairs to find frequent double term sets
    for pair in itertools.combinations(s_1, r=2):
        # Get each word
        a = pair[0]
        b = pair[1]
        
        # Skip pair if different class orientation
        a_class = word_classes[a]
        b_class = word_classes[b]
        if a_class != b_class:
            continue
        
        # If same orientation, compute support for pair by iterating through corpus
        pair_support = 0
        for i in xrange(0,2):
            for sent in corpus[i]:
                if a in sent and b in sent:
                    pair_support += 1
        
        # Add as frequent term is support >= threshold
        if pair_support >= min_sup:
            s_2.add(pair)
    
    #print s_2
    
    return s_1, s_2


if __name__ == "__main__":
    print "#Frequent term set feature expansion#"
    print ""
    
    # Save sentences from data file to array (split between pos and neg)
    corpus = [[], []]
    with open("fts-train-sample.txt") as file:
        for line in file:
            l = line.strip().split()
            if l[0] == "+1":
                corpus[0].append(l[1:])
            else:
                corpus[1].append(l[1:])
    
    total_docs = len(corpus[0]) + len(corpus[1])
    print "total in D:", total_docs
    
    # Set min support to 1% of total docs
    # and confidence to 0.5
    min_sup = 0.01 * total_docs
    conf = 0.5
    print "min support =", min_sup
    print "conf =", conf
    print ""
    
    # Count occurrences of words in both pos and neg, to use for confidence computation
    words = count_pos_neg_occurrences()
    
    # Compute confidences and class orientations for each word
    word_classes = compute_confidences()
    
    # Compute frequent term sets using class orientations
    set1, set2 = get_frequent_sets()
    print "num singles:", len(set1)
    print "num pairs:", len(set2)
    
    # Now we do feature expansion using frequent term sets computed
    # Get sentences to expand
    sents = []
    labels = []
    with open("../data/tree-test/test-full.txt") as file:
        for line in file:
            line = line.strip().split()
            labels.append(line[0])
            sents.append(line[1:])
    
    #print len(sents)
    
    # Iterate over sentences
    for x in xrange(len(sents)):
        #print "expanding sentence:", x
        label = labels[x]
        sent = sents[x]
        #print "before:", label, sent
        
        new_feats = set()
        # Iterate each word in instance and look for it in frequent double term sets. If found
        # then we add the other in the pair (provided it's not already in the sentence)
        for w in sent:
            for pair in set2:
                if w in pair:
                    # Get the other pair (whichever is not w)
                    w2 = pair[0] if pair[1] == w else pair[1]
                    #print w, w2
                    if w2 not in sent:
                        new_feats.add(w2)
        
        #print "new feats:", new_feats
        
        # Add new feats to sentence
        for y in new_feats:
            if y not in sent:
                y = y.split(":")[0]
                sent.append(y + ":0.9")
        
        #print ""
    
    # Print expanded sentences to file
    with open("test-expanded-fts4.txt", "w") as file:
        i = 0
        for sent in sents:
            # get the label for sentence and add it first
            label = labels[i]
            file.write(label + " ")
            for f in sent:
                file.write(f + " ")
            file.write("\n")
            i += 1
    