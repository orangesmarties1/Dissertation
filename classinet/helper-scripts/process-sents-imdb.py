# Reads in Large Movie Review dataset (containing IMDB reviews), processes
# and saves into sentences


import os
import nltk
import re
import string


def clean_sentence(s):
    """
    Cleans s of numerous unwanted characters (and converts to lower) and returns.
    """
    # to lower case
    s = s.lower()
    # replace '--' with space (otherwise it combines two words together)
    s = re.sub("--", " ", s)
    # replace html tags with space
    s = re.sub("<.+>", " ", s)
    # remove rest of punctuation
    #s = s.translate(string.maketrans("",""), ".,?!'`-\/#><*():;+=[]@%&\$\"")
    s = s.translate(string.maketrans("",""), string.punctuation)
    # replace all numbers (including things like 1970s, 13th, 7ft) with <num>
    s = re.sub("(\s|^)*[\d]+[stndrdfh]*(\s|$)*", " <NUM> ", s)
    
    return s


if __name__ == "__main__":
    # Input data (d) and output file to save to (o)
    d = "../data/aclImdb/test/neg"
    o = "../data/imdb-sentences-test-neg.txt"
    
    # Read in reviews, break into sentences and clean
    sentences = []
    for f in os.listdir(d):
        # Split into sentences
        with open(d + "/" + f) as file:
            line = file.readline()
            # try to tokenize into sentences - if there's a non-ascii character, it will throw error
            try:
                l = nltk.sent_tokenize(line)
                for s in l:
                    sentences.append(clean_sentence(s))
            except:
                # pass if error
                print "error in file", f
                pass
    
    id = 0
    # Write sentences to output file
    with open(o, "w") as out:
        for s in sentences:
            #out.write(str(id) + ":" + s + "\n")
            out.write(s + "\n")
            id+=1
    