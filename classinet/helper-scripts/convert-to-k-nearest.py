# Takes in file of predicted features, and returns new file with only top k expanded features remaining.


if __name__ == "__main__":
    original_data = []
    # read file into array
    with open("output-700/tree-test/test-expanded-1.txt") as file:
        for line in file:
            original_data.append(line.strip().split())
    
    new_data = []
    
    k = 10
    #count = 0
    for data_item in original_data:
        #if count == 5:
        #    break
        
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
        
        # iterate through expanded feats, sorted by value, and append top k to feats array
        c = 0
        for i in sorted(expanded_feats, key=expanded_feats.get, reverse=True):
            if c == k:
                break
            weight = 1 / float(c + 1)
            
            # could also compute feat value by multiplying by weight?
            #new_feat_value = float(expanded_feats[i]) * weight
            
            # add to feats with new value
            #feats.append(i + ":" + str(weight))
            feats.append(i + ":" + str(expanded_feats[i]))
            
            c += 1
        
        feats.insert(0, label)
        #print feats
        
        # then add feature vector with selected feats to new_data array
        new_data.append(feats)
        
        #count += 1
    
    #print new_data
    
    # print new data to new file
    with open("output-700/tree-test/test-expanded-41.txt", "w") as file:
        for data in new_data:
            for x in data:
                file.write(x + " ")
            file.write("\n")
    