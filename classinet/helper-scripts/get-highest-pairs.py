# Gets highest related pairs and prints to new file.


import lib.utility as u
import numpy


if __name__ == "__main__":
    sim_a = u.get_lines("output-700/list-sim.txt")
    agr_a = u.get_lines("output-700/list-agr.txt")
    
    # create dict of tuples from two arrays (so we can sort together)
    d = {}
    for i in xrange(len(sim_a)):
        d[i] = (float(sim_a[i]), float(agr_a[i]))
    
    #print d
    
    # sort dict and take top half highest and put into new arrays
    sim_a_top = []
    agr_a_top = []
    half = len(d)/float(2)
    i=0
    for key in sorted(d, key=d.get, reverse=True):
        if i > half:
            break
        #print d[key]
        sim_a_top.append(d[key][0])
        agr_a_top.append(d[key][1])
        
        i+=1
    
    #print sim_a_top
    #print agr_a_top
    
    # print new arrays to files
    #with open("output-700/list-sim-top.txt", "w") as file:
    #    for x in sim_a_top:
    #        file.write(str(x) + "\n")
    #with open("output-700/list-agr-top.txt", "w") as file:
    #    for x in agr_a_top:
    #        file.write(str(x) + "\n")
    