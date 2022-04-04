from pprint import pprint

"""
James Yoo

I only added edge weights to the classes as for the bonus
I did all the other requirements

Specs:
Part 2:
Create the following classes: a class for adjacency lists and a class for adjacency matrices
Each class should be initialized as an empty adjacency list or matrix. 
I recommend initializing the matrix as a nXn matrix based on the number of nodes in the graph. 
It is important to note that if a new node is added, the matrix will have to change to an n+1Xn+1 matrix.

The classes should have a function to initialize the graph based on a prior edge list (ie the function code above set up to accept data via a class).
-----------<BONUS
The edge_tuples you receive for this section are no longer pairs, now they are triplets like (1,4,7) where the first value is the first node, 
the second value is the second node and the third value is the cost to traverse this edge.  
You will get extra credit for implementing edge costs into your program.
>-----------
The classes should also have:
    1.  A function that given a new edge_pair adds it to the data structure. Note that the case of the edge pair (->, <- or <>) 
    depends on how the original data structure was initialized. It may be a good idea to specify that during initialization of an instance of the class.
    2.  A function which returns the node with the most edges in the cases of (these should work for any type graph):
            A:  edges leaving the node
            B:  edges pointing toward the node
            C:  edges with the most nodes pointing both towards and away from the node
    
    3.  A set of functions that given a starting node returns 
            A:  a BFS search of the graph
            B:  a DFS search of the graph
            C:  given an ending node as well, generate one path from the starting node to the ending node
            -----------<BONUS
            D:  a Single Source shortest path from that node to every other node in O(elogn) time for the adjacency list implementation 
            and O(n^2) for the matrix implementation (n means nodes and e means edges)
            You should use the above edge cost bonus question for calculating shortest paths
            /Bonus>-----------

"""

"""
Adjacency matrix class start
"""
class adjacency_matrix_class():

    # Constructor to initialize the matrix, the use can enter a premade adjacency matrix similarily in part 1. It is expected that the user enters an edge weight
    # the logic is the same from part 1, the only difference is that the edge weights are added on in a seperate matrix
    def __init__(self, *args, **kwargs):
        self.adj_matrix = []
        self.weights = []
        size = self.count_nodes(*args)
        list_to_append = []

        for keyword in kwargs:
            node_direction = kwargs[keyword]

        for value in range(size + 1):
            list_to_append.append(0)
        for value in range(size + 1):
            self.adj_matrix.append(list_to_append[:])
            self.weights.append(list_to_append[:])

        for edge_value in args:
            if node_direction == "->" or node_direction == "<>":
                self.adj_matrix[edge_value[0]][edge_value[1]] = 1
                self.weights[edge_value[0]][edge_value[1]] = edge_value[2]
            if node_direction == "<-" or node_direction == "<>":
                self.adj_matrix[edge_value[1]][edge_value[0]] = 1
                self.weights[edge_value[1]][edge_value[0]] = edge_value[2]

    """
    Helper function to count the number of nodes in the matrix to initialize the adjacency matrix for the constructor

    @param: *args - any number of tuples with two values in each tuple of type int
    @return: returns the size of the adjacency matrix
    """
    def count_nodes(self, *args):
        set_of_nodes = set()
        for edge_pair in args:
            set_of_nodes.add(edge_pair[0])
            set_of_nodes.add(edge_pair[1])
        return len(set_of_nodes)

    """
    Function to add edge into the adjacency matrix. 

    @param: node1, node2 are the node pairs for the edge
            edge_weight is the cost to tranverse between node1 and node2 
            self - help references the adjacency_matrix
            kwargs - dictionary of direction must be 1 key - val pair
    @return: None
    """
    def add_edge(self, node1, node2, edge_weight, **kwargs):

        #get the direction for the edge
        for keyword in kwargs:
            node_direction = kwargs[keyword]

        
        size = len(self.adj_matrix)
        #enters the if chain if the nodes are larger than the values in the matrix, which will require a resizing in the matrix
        if size <= node1 or size <= node2:

            # add an extra column to each row
            for row in range(size):
                self.adj_matrix[row].append(0)
                self.weights[row].append(0)

            # add an extra row
            self.adj_matrix.append([])
            self.weights.append([])

            # fill up the new rows with 0's
            for new_row in range(size+1):
                self.adj_matrix[size].append(0)
                self.weights[size].append(0)

        #update the adjacency list to the edge
        if node_direction == "->" or node_direction == "<>":
            self.adj_matrix[node1][node2] = 1
            self.weights[node1][node2] = edge_weight
        if node_direction == "<-" or node_direction == "<>":
            self.adj_matrix[node2][node1] = 1
            self.weights[node2][node1] = edge_weight

    """
    Function to search for the node that has the most nodes leaving  

    @param: self - help references the adjacency_matrix
    @return: node - the node which has the most nodes leaving from 
    """
    def most_leaving_node(self):
        most_edge_leaving = 0
        node = 0
        size = len(self.adj_matrix)
        for row in range(size):
            current_edges_leaving_node = 0
            for col in range(size):
                current_edges_leaving_node += self.adj_matrix[row][col]
            if current_edges_leaving_node > most_edge_leaving:
                most_edge_leaving = current_edges_leaving_node
                node = row
        return node

    """
    Function to search for the node that has the most nodes pointed to itself  

    @param: self - help references the adjacency_matrix
    @return: node - the node which has the most nodes pointed at 
    """
    def most_pointed_node(self):
        count_most_pointed = 0
        node = 0
        size = len(self.adj_matrix)
        for col in range(size):
            current_edges_pointed_node = 0
            for row in range(size):
                current_edges_pointed_node += self.adj_matrix[row][col]
            if current_edges_pointed_node > count_most_pointed:
                count_most_pointed = current_edges_pointed_node
                node = col
        return node

    """
    Function to search for the node with the most nodes pointing both towards and away from the node. 

    @param: self - help references the adjacency_matrix
    @return: node - the node which has the most nodes pointing both towards and away from the node 
    """
    def most_bidirected_nodes(self):
        count_bidirected_pointed = 0
        node = 0
        size = len(self.adj_matrix)
        for row in range(size):
            current_edges_pointed_node = 0
            for col in range(size):
                if self.adj_matrix[row][col] == self.adj_matrix[col][row]:
                    current_edges_pointed_node += self.adj_matrix[row][col]
            if current_edges_pointed_node > count_bidirected_pointed:
                count_bidirected_pointed = current_edges_pointed_node
                node = row
        return node

    """
    Function to perform a BFS on the adjacency matrix given a start position 
    I am assuming the user enters a valid starting node

    @param: self - help references the adjacency_matrix
            start - a starting node 
    @return: visited - the path taken in the BFS 
    """
    def BFS(self, start):
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        while queue:
            s = queue.pop(0)
            print(s)
            for nextnode in range (len(self.adj_matrix)):
                if nextnode not in visited and self.adj_matrix[start][nextnode] != 0:
                    queue.append(nextnode)
                    visited.append(nextnode)
            if len(queue) != 0:
                start = queue[0]
        return visited

    """
    Recursive Function to perform a DFS on the adjacency matrix given a start position 
    I am assuming the user enters a valid starting node

    @param: self - help references the adjacency_matrix
            start - a starting node
            visited - path taken through DFS, initialized as None
    @return: visited - the path taken in the DFS 
    """
    def DFS(self, start, visited = None):
        if visited is None:
            visited = []
        visited.append(start)

        print(start)

        for nextnode in range (len(self.adj_matrix)):
            if nextnode not in visited and self.adj_matrix[start][nextnode] != 0:
                self.DFS( nextnode, visited)

        return visited
    
    """
    A function to generate a path from a given start and a given end using a modified BFS

    @param: self - help references the adjacency_matrix
            start - a starting node
            end - an ending node
    @return: visited - the path taken in the path generated 
    """
    def generate_path(self, start, end):
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        while queue:
            s = queue.pop(0)
            for nextnode in range (len(self.adj_matrix)):
                if nextnode not in visited and self.adj_matrix[start][nextnode] != 0:
                    if nextnode == end:
                        visited.append(nextnode)
                        print(visited)
                        return visited
                    queue.append(nextnode)
                    visited.append(nextnode)
            if len(queue) != 0:
                start = queue[0]
        print("No path available")
        return -1

    # Simple function print the matrix
    def print_matrix(self):
        print("Adjacency Matrix: ")
        size = len(self.adj_matrix)
        for row in range(0, size + 1):
            output_matrix = ""
            for col in range(0, size + 1):
                if row == 0 and col != 0:
                    output_matrix += "   " + str(col-1)
                elif col == 0 and row != 0:
                    output_matrix += "   " + str(row-1)
                else:
                    output_matrix += "   " + \
                        str(self.adj_matrix[row - 1][col - 1])
            print(output_matrix)
        print()

    #simple function to print the matrix weight
    def print_weight(self):
        size = len(self.weights)
        print("Matrix Weights: ")
        for row in range(0, size + 1):
            output_weight = ""
            for col in range(0, size + 1):
                if row == 0 and col != 0:
                    output_weight += "   " + str(col-1)
                elif col == 0 and row != 0:
                    output_weight += "   " + str(row-1)
                else:
                    output_weight += "   " + \
                        str(self.weights[row - 1][col - 1])
            print(output_weight)
        print()

"""
Adjacency list class start
"""
class adjacency_list_class():
    """
    # Constructor to initialize the adjacency list, the use can enter a premade adjacency list similarily in part 1. It is expected that the user enters an edge weight
    # the logic is the same from part 1, the only difference is that the edge weights implmented and the user MUST ENTER A WEIGHT
    The first value in an adjacency list is the connected node, while the second value is the weight of the node
    """
    def __init__(self, *args, **kwargs):
        self.adj_list = dict()
        node_direction = ""

        for keyword in kwargs:
            node_direction = kwargs[keyword]
        
        for edge_pair in args:
            if node_direction == "->" or node_direction == "<>": 
                node = edge_pair[0]

                if node in self.adj_list:
                    self.adj_list[node].append([edge_pair[1], edge_pair[2]])

                else:
                    self.adj_list[node] = [[edge_pair[1], edge_pair[2]]]
            if node_direction == "<-" or node_direction == "<>":
                node = edge_pair[1]

                if node in self.adj_list:
                    self.adj_list[node].append([edge_pair[0], edge_pair[2]])

                else:
                    self.adj_list[node] = [[edge_pair[0], edge_pair[2]]]

    """
    Function to add edge into the adjacency list. 

    @param: node1, node2 are the node pairs for the edge
            edge_weight is the cost to tranverse between node1 and node2 
            self - help references the adjacency_list
            kwargs - specifies a key - val pair for the direction
    @return: None
    """
    def add_edge(self, node1, node2, edge_weight, **kwargs):
        for keyword in kwargs:
            node_direction = kwargs[keyword]

        if node_direction == "->" or node_direction == "<>": 

            if node1 in self.adj_list:
                self.adj_list[node1].append([node2, edge_weight])

            else:
                self.adj_list[node1] = [[node2, edge_weight]]
        if node_direction == "<-" or node_direction == "<>":

            if node2 in self.adj_list:
                self.adj_list[node2].append([node1, edge_weight])

            else:
                self.adj_list[node2] = [[node1, edge_weight]]
    
    #simple function to print an adjcency list
    def print_adjacency_list(self):
        pprint(self.adj_list)


    """
    Function to search for the node that has the most nodes leaving  

    @param: self - help references the adjacency_list
    @return: node - the node which has the most nodes leaving from 
    """
    def most_leaving_node(self):
        most_left_node = 0
        most_left_count = 0

        for key in self.adj_list:
            current_left_node = 0
            for value in self.adj_list[key]:
                current_left_node += 1
            if current_left_node > most_left_count:
                most_left_count = current_left_node
                most_left_node = key

        return most_left_node

    """
    This function will assume the nodes are all in order/consecutive numbers
    Function to search for the node that has the most nodes pointed to itself  

    @param: self - help references the adjacency_list
    @return: node - the node which has the most nodes pointed at 
    """
    def most_pointed_node (self):
        pointed = []
        for i in range (len(self.adj_list)):
            pointed.append(0)

        for key in self.adj_list:
            for value in self.adj_list[key]:
                pointed[value[0]] += 1
        
        max_val = 0
        most_pointed_node = 0
        for node, counts_pointed in enumerate (pointed):
            if counts_pointed > max_val:
                max_val = counts_pointed
                most_pointed_node = node

        return most_pointed_node
    
    """
    Function to search for the node with the most nodes pointing both towards and away from the node. 

    @param: self - help references the adjacency_list
    @return: node - the node which has the most nodes pointing both towards and away from the node 
    """
    def most_bidirected_node(self):
        def check_bidriected(node, check_node):
            for value in self.adj_list[check_node]:
                if value[0] == node:
                    return True
            return False

        pointed = []
        for i in range (len(self.adj_list)):
            pointed.append(0)
        
        for key in self.adj_list:
            for value in self.adj_list[key]:
                if self.adj_list[value[0]] is None:
                    continue
                elif check_bidriected(key, value[0]):
                    pointed[key] += 1
        
        max_val = 0
        most_pointed_node = 0
        for node, counts_pointed in enumerate (pointed):
            if counts_pointed > max_val:
                max_val = counts_pointed
                most_pointed_node = node

        return most_pointed_node
    
    """
    Function to perform a BFS on the adjacency list given a start position 
    I am assuming the user enters a valid starting node

    @param: self - help references the adjacency_list
            start - a starting node 
    @return: visited - the path taken in the BFS 
    """
    def BFS(self, start): 
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        while queue:
            s = queue.pop(0)
            print(s)
            for key in self.adj_list[s]:
                if key[0] not in visited:
                    queue.append(key[0])
                    visited.append(key[0])
            if len(queue) != 0:
                start = queue[0]
        return visited
    
    """
    Recursive Function to perform a DFS on the adjacency list given a start position 
    I am assuming the user enters a valid starting node

    @param: self - help references the adjacency_list
            start - a starting node
            visited - path taken through DFS, initialized as None
    @return: visited - the path taken in the DFS 
    """
    def DFS(self, start, visited = None):
        if visited is None:
            visited = []
        visited.append(start)

        print(start)

        for key in self.adj_list[start]:
            if key[0] not in visited:
                self.DFS(key[0], visited)

        return visited 
    
    """
    A function to generate a path from a given start and a given end using a modified BFS

    @param: self - help references the adjacency_list
            start - a starting node
            end - an ending node
    @return: visited - the path taken in the path generated 
    """
    def generate_path(self, start, end):
        visited = []
        queue = []
        visited.append(start)
        queue.append(start)
        while queue:
            s = queue.pop(0)
            for key in self.adj_list[s]:
                if key[0] not in visited:
                    if key[0] == end:
                        visited.append(key[0])
                        print(visited)
                        return visited
                    queue.append(key[0])
                    visited.append(key[0])
            if len(queue) != 0:
                start = queue[0]
        print("No path available")
        return -1

"""
I am assuming the user is entering nodes in consecutive numeric orders meaning that if there are nodes 0, 1, 2, 3 then 
the user will not try to edge some node 99 into the matrix, but rather node 4

constructor will accept a created edge list
The edge list MUST HAVE EDGE WEIGHTS
"""
if __name__ == "__main__":
    adjacencyMatrix = adjacency_matrix_class((1, 2, 7), (1, 3, 8), (2, 3, 7), (2, 4, 5), (3, 4, 6), (3, 6, 3), (4, 1, 2), (4, 5, 6), (5, 2, 4), direction="<>")
    adjacencyMatrix.add_edge(4, 1, 5, direction="->")
    adjacencyMatrix.add_edge(6, 2, 4, direction="<-")
    adjacencyMatrix.add_edge(1, 2, 4, direction="<-")
    adjacencyMatrix.add_edge(7, 5, 2, direction="<>")
    adjacencyMatrix.add_edge(0, 5, 1, direction="<-")
    adjacencyMatrix.add_edge(4, 0, 1, direction="<>")

    # print(adjacencyMatrix.most_leaving_node())
    #print(adjacencyMatrix.most_pointed_node())
    # print(adjacencyMatrix.most_bidirected_nodes())

    adjacencyMatrix.print_matrix()
    #adjacencyMatrix.print_weight()

    #adjacencyMatrix.DFS(0)
    #print()
    #adjacencyMatrix.BFS(0)
    #print()
    #adjacencyMatrix.generate_path(0, 2)
    #print()
    #adjacencyMatrix.generate_path(0, 9)
    #print()
    adjacenyList = adjacency_list_class((1, 2, 7), (1, 3, 8), (2, 3, 7), (2, 4, 5), (3, 4, 6), (3, 6, 3), (4, 1, 2), (4, 5, 6), (5, 2, 4), direction="<>")
    adjacenyList.add_edge(1, 7, 5, direction = "->")
    adjacenyList.add_edge(4, 0, 1, direction="<>")
    adjacenyList.add_edge(4, 7, 1, direction="<>")

    adjacenyList.print_adjacency_list()
    #print(adjacenyList.most_leaving_node())
    #print(adjacenyList.most_pointed_node())
    #print(adjacenyList.most_bidirected_node())
    #adjacenyList.BFS(0)
    #print()
    #adjacenyList.DFS(0)
    # print()
    # adjacencyMatrix.generate_path(0, 2)
    # print()
    # adjacencyMatrix.generate_path(0, 9)
    # print()