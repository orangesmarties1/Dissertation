# Get feature space for Sentiment Classification task.


import classinet.lib.utility as u


if __name__ == "__main__":
    targets = u.get_target_words()
    
    # Feats dict - to count number of occurrences too
    f_dict = {}
    
    # Get features from Sentiment Treebank train set
    with open("../data/tree-train/treebank-train.txt") as file:
        for line in file:
            for word in line.strip().split()[1:]:
                if word.isalpha():
                    try:
                        f_dict[word] += 1
                    except:
                        f_dict[word] = 1
    
    # Add target words, if not already there
    for w in targets:
        if w not in f_dict:
            #print w, "not in feats!"
            f_dict[w] = 1
    
    # Also add target words prefixed with "exp_"
    prefix = True
    if prefix:
        for w in targets:
            #print "exp_"+w
            f_dict["exp_"+w] = 1
    
    # Get top N features
    #feats = []
    #N = 50000
    #i = 0
    #for word in sorted(f_dict, key=f_dict.get, reverse=True):
    #    if f_dict[word] == 1:
    #        break
    #    #print word, f_dict[word]
    #    feats.append(word)
    #    i += 1
    
    #print "There are", len(f_dict), "features..."
    
    # Print feat space to file
    with open("feat-space-sent.txt", "w") as file:
        for feat in f_dict:
            file.write(feat + " ")
    