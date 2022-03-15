"""
James Yoo
"""
def make_adjacency_list(*args):
    
    adjacency_list = dict()

    for edge_pair in args:

        node = edge_pair[0]

        if node in adjacency_list:
            adjacency_list[node].append(edge_pair[1])

        else:
            adjacency_list[node] = [edge_pair[1]]

    return adjacency_list

def count_nodes(*args):


    set_of_nodes = set()

    for edge_pair in args:

        set_of_nodes.add(edge_pair[0])

        set_of_nodes.add(edge_pair[1])

    return set_of_nodes, len(set_of_nodes)

def make_adjacency_matrix(*args):


    count = count_nodes(*args)[1]

    adjacency_matrix = []

    list_to_append = []

    for value in range (count + 1):
        list_to_append.append(0)

    for value in range (count+1):
        adjacency_matrix.append(list_to_append[:])

    for edge_value in args:
        adjacency_matrix[edge_value[0]][edge_value[1]] = 1
    pprint(adjacency_matrix)
    return 0 


"""
1 | 2, 3
2 | 3, 4
3 | 4, 6
4 | 1, 5
5 | 2, 4 
"""
from pprint import pprint
if __name__ ==  "__main__":
    #(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)
    pprint(make_adjacency_list((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4)))
    make_adjacency_matrix((1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (3, 6), (4, 1), (4, 5), (5, 2), (5,4))