# Takes a random sample of target words to test with.


import lib.utility as u
import random


if __name__ == "__main__":
    targets = u.get_target_words()
    
    #print targets
    
    # get sample of n random ints to index targets with
    n = 50
    r = set()
    max = len(targets)-1
    while len(r) < n:
        i = random.randint(0, max)
        r.add(i)
    #print r
    
    # get sample targets using set created above
    # and print them to file
    sample_targets = [targets[i] for i in r]
    with open("_700/target-words-s.txt", "w") as file:
        for t in sample_targets:
            file.write(t + "\n")
    