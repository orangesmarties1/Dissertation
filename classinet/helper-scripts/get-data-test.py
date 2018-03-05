# Get test data for sample of target words to evaluate accuracy.
# Similar to get-data-train.py, but more to do here as we have to ensure not to select those already in train
# set, meaning there are fewer potential sentences.


import lib.utility as u
import config as c
import random


if __name__ == "__main__":
    # Hard coded list of words to test with
    target_words = ['wonderful', 'love', 'excellent', 'great', 'classic', 'terrible', 'boring', 'worst', 'stupid', 'crap']
    
    # Store all sentences in memory
    sentences_with = u.get_lines(c.output_dir + "sentences-with.txt")
    sentences_without = u.get_lines(c.output_dir + "sentences-without.txt")
    all_sentences = sentences_with + sentences_without
    
    # For each target word, find sample sentences (pos and neg)
    # N is number of pos/neg instances to select
    N = 500
    i = 0
    for word in target_words:
        #print "for:", word
        
        # Shuffle data first
        random.shuffle(sentences_with)
        random.shuffle(all_sentences)
        
        # Get train set in an array to check we don't get a sentence we already have
        train_set = u.get_lines(c.train_data_dir + word + ".txt")
        
        # Get positive instances (containing word)
        pos_data = []
        count = 0
        for s in sentences_with:
            # stop when we have enough
            if count == N:
                break
            
            # monitor whether it's been used already
            used = False
            
            words = s.split()
            # if sentence contains word and meets length threshold
            if (word in words and len(words) >= 8):
                # check it's not in training set
                for x in train_set:
                    if s.strip() in x:
                        used = True
                        break
                
                if not used:
                    pos_data.append(s.strip())
                    count += 1
        
        print count
        # add another loop, only if we didn't get enough longer sentences
        if count < N:
            print "finding shorter sentences..."
            for s in sentences_with:
                if count == N:
                    break
                
                # monitor whether it's been used already
                used = False
                
                words = s.split()
                # if sentence contains word and meets length threshold
                if (word in words and len(words) >= 5):
                    # check it's not in training set
                    for x in train_set:
                        if s.strip() in x:
                            used = True
                            break
                    
                    if not used and s.strip() not in pos_data:
                        pos_data.append(s.strip())
                        count += 1
            print count
        
        # Get negative instances (not containing word)
        # Practically same procedure as above, but this time there are much more sentences to choose from
        neg_data = []
        count = 0
        for s in all_sentences:
            # stop when we have enough
            if count == N:
                break
            
            # monitor whether it's been used already
            used = False
            
            words = s.split()
            # if sentences meets length threshold
            if (len(words) >= 10:
                # check it's not in training set
                for x in train_set:
                    if s.strip() in x:
                        used = True
                        break
                
                if not used:
                    neg_data.append(s.strip())
                    count += 1
        
        #print "p:", len(pos_data), "n:", len(neg_data)
        
        i += 1
        
        # Write the test data to file
        #with open(c.output_dir + "target-test-data/" + word + ".txt", "w") as file:
        #    for s in pos_data:
        #        file.write("+1 " + s + "\n")
        #    for s in neg_data:
        #        file.write("-1 " + s + "\n")
    