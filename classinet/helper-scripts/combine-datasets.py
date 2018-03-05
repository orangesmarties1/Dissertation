# Simply combines Large Movie Review datasets (test and train) into one larger file.


import lib.utility as u


if __name__ == "__main__":
    
    sents1 = set(u.get_lines("imdb-sentences-neg.txt"))
    sents2 = set(u.get_lines("imdb-sentences-test-neg.txt"))
    l1 = len(sents1)
    l2 = len(sents2)
    
    all = sents1.union(sents2)
    l3 = len(all)
    
    #print l1, l2, l3
    
    #with open("imdb-all-sentences-neg.txt", "w") as file:
    #    for s in all:
    #        if len(s.split()) > 1:
    #            file.write(s + "\n")