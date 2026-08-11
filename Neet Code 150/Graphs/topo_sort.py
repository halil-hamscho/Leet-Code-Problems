'''
Topological Sorting for Directed Acyclic Graph(DAG) is a linear ordering
of vertices such that for every directed edge uv, vertex u comes before v
in the ordering. Topological Sorting for a graph is not possible is the graph is not a DAG

A way to think about Topological Sorting is that
it is a dependency problem
in which a  completion of one task depends upon the completion of
several other tasks whose order can vary

need a stack and a visited array of size n

A.
For each univisted verted in the graph do the following:
1. Call the DFS function with the vertex as a parameter
2. In the DFS function, mark the vertex as visited and recursively call the DFS function
for all unvisited neighbors of the vertex
3. Once all the neighbors have been visited, push the vertex onto the stack
B.
After all, vertices have been visited, pop elements from the stack and append them 
to the output list until the stack is empty
The resulting list is the topologically sorted order of the graph

The key here is to print all elements of stack from top to bottom

Time Complexity O (V + E) simply DFS with a working stack and a result Stack

Auxiliary Space O(V) the extra space is needed for the 2 stacks used
'''

def topologicalSortUtil(v, adj, visited, stack):
    # Mark the current node as visited
    visited[v] = True

    # Recur for all adjacent vertices
    # because it is an adjancency list
    for i in adj[v]:
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    # Push current vertex to stack which stores the result
    stack.append(v)

def topologicalSort(adj, V):
    stack = [] # stack to store the result

    visited = [False] * V

    # Call the recursive helper function to store
    # Topological Sort starting from all vertices one by one
    for i in range(V):
        if not visited[i]:
            topologicalSortUtil(i, adj, visited, stack)

    print("Topological Sorting of the graph:", end=" ")
    while stack:
        print(stack.pop())

if __name__ == "__main__":
    # Number of nodes
    V = 4

    # Edges
    edges = [[0,1], [1,2], [3,1], [3,2]]

    # graph represented as an adjacency list
    adj = [[] for _ in range(V)]

    for i in edges:
        adj[i[0]].append(i[1])
    
    topologicalSort(adj, V)

