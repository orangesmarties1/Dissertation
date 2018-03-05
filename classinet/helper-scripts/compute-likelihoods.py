# Computes likelihoods of targets based on occurrences in corpus.


import lib.utility as u


if __name__ == "__main__":
    corpus_pos = u.get_lines("../data/imdb-sentences-pos.txt")
    corpus_neg = u.get_lines("../data/imdb-sentences-neg.txt")
    corpus = corpus_pos + corpus_neg
    
    # get total count of all words
    total_count = 0
    counts = {}
    for line in corpus:
        for word in set(line.strip().split()):
            if word.isalpha():
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                total_count += 1
    
    targets = u.get_target_words()
    likelihoods = {}
    for t in targets:
        likelihoods[t] = counts[t] / float(total_count)
    
    #for key in sorted(likelihoods, key=likelihoods.get, reverse=False):
    #    print key, likelihoods[key]
    
    with open("target-likelihoods.txt", "w") as file:
        for key, value in likelihoods.iteritems():
            file.write(key + " " + str(value) + "\n")
    
    