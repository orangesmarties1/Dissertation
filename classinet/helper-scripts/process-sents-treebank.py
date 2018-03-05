# Reads in Sentiment Treebank dataset, converts to simple string represenation and
# saves as sentences
# Note: we ignore neutral sentences (those with overall sentiment of 2)


import re
import string
from nltk.tree import Tree


def clean_(s):
    """
    Takes in s (in treebank structure), parses, cleans and returns.
    """
    # Use tree data structure to parse properly
    t = Tree.fromstring(s.lower())
    
    # Sreate string from leaves in t
    s = ""
    for l in t.leaves():
        s += l + " "
    
    # remove extra whitespace before punctuation, and at end of string
    s = re.sub("\s{1}([,.'!:;]){1}", "\\1", s)
    # replace '--' and '-' with space (otherwise it combines two words together)
    s = re.sub("--", " ", s)
    s = re.sub("-", " ", s)
    # remove rest of punctuation
    s = s.translate(string.maketrans("",""), ".,?!'`-\/#><*():;+=[]@%&\$\"")
    # replace all numbers (including things like 1970s, 13th, 7ft) with <num>
    s = re.sub("(\s|^)*[\d]+[stndrdfh]*(\s|$)*", " <NUM> ", s)
    # fix "is n't" so it becomes "isn't" and other words ending in "n't"
    s = re.sub("([a-z]+) nt", "\\1nt", s)
    
    return s.strip()


if __name__ == "__main__":
    # Input data (d) and output file to save to (o)
    d = "../data/stanfordTrees/train.txt"
    o = "../data/treebank-sentences-train-values.txt"
    
    sentences = []
    # Read in treebank sentences, clean and append to array with correct label
    with open(d) as file:
        for line in file:
            # find the sentences with non-ascii characters and skip over them
            try:
                line.decode('ascii')
            except UnicodeDecodeError:
                print "unicode error..."
                continue
            
            # Get the sentence sentiment (the 2nd character in string)
            sentiment = int(line[1])
            label = ""
            
            # skip if neutral sentiment, or apply +1/-1 label for others
            if sentiment == 2:
                continue
            elif (sentiment == 0 or sentiment == 1):
                label = "-1"
            elif (sentiment == 3 or sentiment == 4):
                label = "+1"
            
            sentences.append(label + " " + clean_(line))
    
    #pos_count = 0
    #for s in sentences:
    #    if s[0] == "+":
    #        pos_count += 1
    #
    #print "number_of_sentences  positive_sentences  negative_sentences"
    #print len(sentences), pos_count, len(sentences)-pos_count
    
    # Write sentences to output file with label
    with open(o, "w") as file:
        for s in sentences:
            s = s.split()
            # write label first
            file.write(s[0] + " ")
            # write each word with value
            for w in s[1:]:
                file.write(w + ":1 ")
            file.write("\n")
    