# Splits Sentiment Treebank train set into different sizes.


if __name__ == "__main__":
    
    # get full train dataset
    full = set()
    with open("tree-train/size-split/train-full-copy.txt") as file:
        for line in file:
            full.add(line)
    
    # get the 2000 dataset we've already used
    used = set()
    with open("tree-train/size-split/train-2000.txt") as file:
        for line in file:
            used.add(line)
    
    # available sentences are those in full not in used - set difference
    available = full.difference(used)
    
    print "full:", len(full)
    print "used:", len(used)
    print "available:", len(available)
    
    # print available to file, all pos then all neg for ease of sampling
    # first split them into pos and neg
    available_pos = []
    available_neg = []
    for sent in available:
        label = sent[0]
        if label == "+":
            available_pos.append(sent.strip())
        else:
            available_neg.append(sent.strip())
    
    # now print to files
    with open("tree-train/size-split/train-available-pos.txt", "w") as file:
        for sent in available_pos:
            file.write(sent + "\n")
    with open("tree-train/size-split/train-available-neg.txt", "w") as file:
        for sent in available_neg:
            file.write(sent + "\n")
    
    