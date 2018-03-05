# Splits Sentiment Treebank test set into pos file and neg file.


if __name__ == "__main__":
    pos_count = 0
    neg_count = 0
    
    pos = []
    neg = []
    
    with open("treebank-test/test-full.txt") as file:
        for line in file:
            label = line.strip().split()[0]
            
            if label == "+1":
                pos_count += 1
                pos.append(line.strip())
            else:
                neg_count += 1
                neg.append(line.strip())
    
    print "pos count:", pos_count
    print "neg count:", neg_count
    print "total count:", pos_count+neg_count
    
    with open("treebank-test/test-neg.txt", "w") as file:
        for x in neg:
            file.write(x + "\n")
    