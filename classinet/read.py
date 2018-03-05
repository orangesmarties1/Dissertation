def read_features_file(file_name):
    """
    Returns a dict of features from file_name in format {'feature': 'id'}.
    """
    # read features in as a set
    f = set()
    with open(file_name) as file:
        for line in file:
            for w in line.strip().split():
                f.add(w)
    
    # convert to hash table for quicker access
    index = {}
    counter = 0
    for (id, val) in enumerate(list(f)):
        index[val] = id

    return index