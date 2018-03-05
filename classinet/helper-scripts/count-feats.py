# Simply prints out how many feats in feat space file.


if __name__ == "__main__":
    count = 0
    
    with open("output-700/feat-space.txt") as file:
        line = file.readline()
        for f in line.split():
            count += 1
    
    print count