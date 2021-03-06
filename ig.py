import networkx as nx
import os
from random import randint

###########################################
# Change this variable to the path to
# the folder containing all three input
# size category folders
###########################################
path_to_inputs = "./all_inputs"

###########################################
# Change this variable if you want
# your outputs to be put in a
# different folder
###########################################
path_to_outputs = "./outputs"

def main():
    '''
        Main method which iterates over all inputs and calls `solve` on each.
        The student should modify `solve` to return their solution and modify
        the portion which writes it to a file to make sure their output is
        formatted correctly.
    '''
    rowdy_small = []
    small_busnum = 5
    small_capacity = 5
    small = nx.Graph()
    while(len(rowdy_small) < 100):
        curr = set()
        for i in range(0,4):
            curr_int = str(randint(0, 24))
            if(curr_int not in curr):
                curr.add(curr_int)
                if (curr_int not in list(small.nodes)):
                    small.add_node(curr_int)
        if(curr not in rowdy_small):
            rowdy_small.append(curr)
    for i in rowdy_small:
        for m in i:
            for n in i:
                if m != n:
                    small.add_edge(m, n)
    medium_busnum = 25
    medium_capacity = 10
    medium = nx.Graph()
    rowdy_medium = []
    while(len(rowdy_medium) < 1000):
        curr = set()
        for i in range(0,9):
            curr_int = str(randint(0, 249))
            if(curr_int not in curr):
                curr.add(curr_int)
                if (curr_int not in list(medium.nodes)):
                    medium.add_node(curr_int)
        if(curr not in rowdy_medium):
            rowdy_medium.append(curr)
    for i in rowdy_medium:
        for m in i:
            for n in i:
                if m != n:
                    medium.add_edge(m, n)
   # print(list(medium.nodes))
   # print(list(medium.edges))
    large_busnum = 25
    large_capacity = 20
    large = nx.Graph()
    rowdy_large = []
    while(len(rowdy_large) < 2000):
        curr = set()
        for i in range(0,19):
            curr_int = str(randint(0, 499))
            if(curr_int not in curr):
                curr.add(curr_int)
                if (curr_int not in list(large.nodes)):
                    large.add_node(curr_int)
        if(curr not in rowdy_large):
            rowdy_large.append(curr)
    for i in rowdy_large:
        for m in i:
            for n in i:
                if m != n:
                    large.add_edge(m, n)
    #print(list(large.nodes))
    #print(list(large.edges))
    nx.write_gml(small, "input_small.gml")
    nx.write_gml(medium, "input_medium.gml")
    nx.write_gml(large, "input_large.gml")
    sp = open("small_paramater", "w+")
    sp.write(str(small_busnum))
    sp.write("\n")
    sp.write(str(small_capacity))
    sp.write("\n")
    for i in rowdy_small:
        sp.write("{}".format(i))
        sp.write("\n")
    mp = open("medium_paramater", "w+")
    mp.write(str(medium_busnum))
    mp.write("\n")
    mp.write(str(medium_capacity))
    mp.write("\n")
    for i in rowdy_medium:
        mp.write("{}".format(i))
        mp.write("\n")
    lp = open("large_paramater", "w+")
    lp.write(str(large_busnum ))
    lp.write("\n")
    lp.write(str(large_capacity))
    lp.write("\n")
    for i in rowdy_large:
        lp.write("{}".format(i))
        lp.write("\n")

if __name__ == '__main__':
    main()
