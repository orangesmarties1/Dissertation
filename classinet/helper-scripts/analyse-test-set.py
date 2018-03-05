# Analyses sentences in Sentiment Treebank test dataset (based on length) and splits
# into four groups.


if __name__ == "__main__":
    # read in test sentences
    sents = []
    with open("tree-test/test-full.txt") as file:
        for line in file:
            sents.append(line.strip().split())
    
    # get average sentence length and lower and upper threshold in dataset
    sum_words = 0
    sent_count = len(sents)
    for s in sents:
        sum_words += len(s)
    
    avg_length = sum_words / sent_count
    # experimenting showed +/- 6 either side of avg gives best split
    lower_threshold = avg_length - 6
    upper_threshold = avg_length + 6
    
    print lower_threshold, avg_length, upper_threshold
    
    # partition sentences into four groups, based on their length
    sents_dict = {}
    sents_dict[0] = []
    sents_dict[1] = []
    sents_dict[2] = []
    sents_dict[3] = []
    
    for s in sents:
        l = len(s)
        if l < lower_threshold:
            sents_dict[0].append(s)
        elif l < avg_length:
            sents_dict[1].append(s)
        elif l < upper_threshold:
            sents_dict[2].append(s)
        else:
            sents_dict[3].append(s)
    
    print len(sents_dict[0]), len(sents_dict[1]), len(sents_dict[2]), len(sents_dict[3])
    
    # output sentences to new files
    #file_base = "treebank-test-split-"
    #for i in xrange(1,5):
    #    file_name = file_base + str(i) + ".txt"
    #    print file_name
    #    
    #    with open(file_name, "w") as file:
    #        for s in sents_dict[i-1]:
    #            for w in s:
    #                file.write(w + " ")
    #            file.write("\n")
    
    