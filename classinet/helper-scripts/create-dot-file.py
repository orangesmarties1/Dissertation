# This script takes an input file of edges and converts into a DOT file
# and then (optionally) runs to DOT file to create an SVG of the graph

# Example of how to run DOT file:
# dot -o graphs/directed-5.svg -T svg dot/directed-5.dot


import os


if __name__ == "__main__":
    directed = True
    outname = "directed-5-m"
    
    # set pieces of graph
    opening = "graph {"
    arrow = "--"
    closing = "}"
    
    # if directed graph, change a few things
    if directed:
        opening = "digraph {"
        arrow = "->"
    
    # read lines from file, convert to DOT syntax and save into array
    edges = []
    with open("output-700/edges-directed-5-m.txt") as file:
        for line in file:
            l = line.strip().split()
            # get each node and weight from line
            node1 = l[0]
            node2 = l[1]
            weight = l[2]
            edges.append(node1 + " " + arrow + " " + node2 + " [label=" + weight[:5] + "]")
    
    #print opening
    #for e in edges:
    #    print e
    #print closing
    
    # print to dot file with specified name
    with open("dot/700/" + outname + ".dot", "w") as file:
        file.write(opening + "\n")
        for e in edges:
            file.write(e + "\n")
        file.write(closing)
    
    # call command to run DOT file
    #os.system("dot -o graphs/700/" + outname + ".svg -T svg dot/700/" + outname + ".dot")
    