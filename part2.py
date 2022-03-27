"""
James Yoo

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