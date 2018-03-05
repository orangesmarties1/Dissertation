# Simply counts pos/neg instances in given dataset.


if __name__ == "__main__":
    pos_count = 0
    neg_count = 0
    
    with open("tree-test/test-full2.txt") as file:
        for line in file:
            label = line.strip().split()[0]
            
            if label == "+1":
                pos_count += 1
            else:
                neg_count += 1
    
    print "pos count:", pos_count
    print "neg count:", neg_count
    print "total count:", pos_count+neg_count
    