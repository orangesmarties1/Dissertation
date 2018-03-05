# Takes in file of expanded features, and returns new file with prefixed expanded features.


if __name__ == "__main__":
    original_data = []
    # read file into array
    with open("output-700/tree-test/test-expanded-nb-a.txt") as file:
        for line in file:
            original_data.append(line.strip().split())
    
    new_data = []
    
    count = 0
    for data_item in original_data:
        #if count == 3:
        #    break
        
        #print count
        
        label = data_item[0]
        feats = []
        expanded_feats = {}
        
        # iterate through feats in vector and separate into original and expanded
        for feat_value in data_item[1:]:
            x = feat_value.split(":")
            feat = x[0]
            value = x[1]
            
            if value == "1":
                feats.append(feat + ":1")
            else:
                expanded_feats[feat] = value
        
        #print feats
        
        # iterate through expanded feats and prefix them
        c = 0
        for key, value in expanded_feats.iteritems():
            prefixed_key = "exp_" + key
            #print prefixed_key
            feats.append(prefixed_key + ":" + value)
        
        feats.insert(0, label)
        #print feats
        
        # then add feature vector with selected feats to new_data array
        new_data.append(feats)
        
        count += 1
    
    #print new_data
    
    # print new data to new file
    with open("output-700/tree-test/test-expanded-nb-a-prefix.txt", "w") as file:
        for data in new_data:
            for x in data:
               file.write(x + " ")
            file.write("\n")
    