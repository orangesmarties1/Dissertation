# Gets average sentence length in corpus.


if __name__ == "__main__":
    sum = 0
    count = 0
    
    with open("imdb-sentences-pos.txt") as file:
        for line in file:
            sum += len(line.strip().split())
            count +=1
    
    with open("imdb-sentences-neg.txt") as file:
        for line in file:
            sum += len(line.strip().split())
            count +=1
    
    # print avg
    print sum/count
    