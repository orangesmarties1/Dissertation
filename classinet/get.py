import config as c
# returns array of target words from file
def get_target_words():
    """
    Simply returns array of target words.
    """
    t = []
    with open(c.output_dir + "target-words.txt") as file:
        for line in file:
            # only take first item (word) in line
            t.append(line.strip().split()[0])
    return t