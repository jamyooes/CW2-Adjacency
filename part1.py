"""
James Yoo

I have completed everything including the bonus

Specs:
Part 1: 
Create two functions, one which will convert any number of tuple edge_pairs 
into an adjacency list and one which will convert them to an adjacency matrix.

The difference is that now, the functions will check for an input from the user 
which will indicate the direction of an edge tuple. It will take in a key value pair 
which will be named "direction" and expected inputs are:
    '->' for left to right 
    '<-' for right to left 
    '<>' for both directions
So your functions should be able to check for and do all of these. 
You can either use if elif else logic for this and input separate logic 
for each case or use helper functions or possibly a slightly more clever approach...
Once you've created these functions, you're going to do the following:

Bonus: Bonus point opportunity, create an additional matrix function using a numpy array.
Please note that a numpy array is not mutable, so it isn't recommended 
that you use it in the class functions below.
"""

"""
Function to create an adjacency list

@param: *args - any number of tuples with 2 values in each tuple of type int
        **kwargs - a dictionary that contains the direction
                  sample input for **kwargs is: direction = "->" for left directed nodes
@return: returns an adjacency list
"""
def make_adjacency_list(*args, **kwargs):
    node_direction = ""         # Variable to keep tarck of direction of the edge
    adjacency_list = dict()     # holds the adjacency list

    # gets the node_direction for the premade adjacency list
    for keyword in kwargs:
        node_direction = kwargs[keyword]

    # this loop inserts all the edges into the adjacency_list based on the direction the nodes are pointed
    for edge_pair in args:
        
        if node_direction == "->" or node_direction == "<>": 
            node = edge_pair[0]

            if node in adjacency_list:
                adjacency_list[node].append(edge_pair[1])

            else:
                adjacency_list[node] = [edge_pair[1]]
        if node_direction == "<-" or node_direction == "<>":
            node = edge_pair[1]

            if node in adjacency_list:
                adjacency_list[node].append(edge_pair[0])

            else:
                adjacency_list[node] = [edge_pair[0]]
    return adjacency_list

"""
Helper function to count the number of unique nodes to create the adjacency matrix
@param: *args - any number of tuples with two values in each tuple of type int
@return: returns the number of unique nodes
"""
def count_nodes(*args):


    set_of_nodes = set()

    for edge_pair in args:

        set_of_nodes.add(edge_pair[0])

        set_of_nodes.add(edge_pair[1])

    return len(set_of_nodes)


"""
Function to create an adjacency matrix given any number of int tuples and a direction
@param: *args - any number of tuples with two values in each tuple of type int
@return: returns the adjacency matrix, formatted in that the topmost row and leftmost column will represent the nodes
"""
def make_adjacency_matrix(*args, **kwargs):
    for keyword in kwargs:
        node_direction = kwargs[keyword]
        
    count = count_nodes(*args)

    adjacency_matrix = []

    list_to_append = []

    for value in range (count + 1):
        list_to_append.append(0)

    for value in range (count+1):
        adjacency_matrix.append(list_to_append[:])

    for edge_value in args:
        if node_direction == "->" or node_direction == "<>":
            adjacency_matrix[edge_value[0]][edge_value[1]] = 1
        if node_direction == "<-" or node_direction == "<>":
            adjacency_matrix[edge_value[1]][edge_value[0]] = 1

    #this is just to print the adjacency matrix, for me to read easier
    print("Adjacency Matrix: ")
    size = len(adjacency_matrix)
    for row in range(0, size + 1):
        output_matrix = ""
        for col in range(0, size + 1):
            if row == 0 and col != 0:
                output_matrix += "   " + str(col-1)
            elif col == 0 and row != 0:
                output_matrix += "   " + str(row-1)
            else:
                output_matrix += "   " + \
                    str(adjacency_matrix[row - 1][col - 1])
        print(output_matrix)
    print()

    return(adjacency_matrix)

import numpy as np
"""
Bonus using numpy arrays
Function to create an adjacency matrix given any number of int tuples and a direction
@param: *args - any number of tuples with two values in each tuple of type int
@return: returns the adjacency matrix, formatted in that the topmost row and leftmost column will represent the nodes
"""
def make_numpy_adjacency_matrix(*args, **kwargs):
    for keyword in kwargs:
            node_direction = kwargs[keyword]

    count = count_nodes(*args)

    adjacency_matrix = np.zeros((count + 1, count + 1), dtype = int)

    for edge_value in args:
        if node_direction == "->" or node_direction == "<>":
            adjacency_matrix[edge_value[0]][edge_value[1]] = 1
        if node_direction == "<-" or node_direction == "<>":
            adjacency_matrix[edge_value[1]][edge_value[0]] = 1

    #this is just to print the adjacency matrix, for me to read easier
    print("Numpy Matrix: ")
    size = len(adjacency_matrix)
    for row in range(0, size + 1):
        output_matrix = ""
        for col in range(0, size + 1):
            if row == 0 and col != 0:
                output_matrix += "   " + str(col-1)
            elif col == 0 and row != 0:
                output_matrix += "   " + str(row-1)
            else:
                output_matrix += "   " + \
                    str(adjacency_matrix[row - 1][col - 1])
        print(output_matrix)
    print()

    return adjacency_matrix    

"""
Testing
"""
from pprint import pprint
if __name__ ==  "__main__":
    pprint(make_adjacency_list((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4), direction = "<>"))
    make_adjacency_matrix((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4), direction = "<>")
    make_numpy_adjacency_matrix((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4), direction = "<>")