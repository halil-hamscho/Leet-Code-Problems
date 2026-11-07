1. Graph Terminology

- Vertex (Node)
- Edge
- Directed
- Un-directed
- In-degree
- Out-degree    
- Connected
- Disconnected

2. How are graphs given in coding interviews?

    4 ways they are given
        1. Array of Edges
            - [x, y] edge going from x to y
        2. Adjacency List
            - hashmap: key:value is vertex:edge
        3. Adjacency Matrix
            - adjMatrix[i][j] = 1 denotes edge from i to j
        4. Matrix
            - 0's and 1's

3. Graph Algorithms

    1. Depth-First-Search
        - typically keeps visited cells marked (once cell is processed, no need to process it again)
        - eexplores each reachable node once
        - often O(V + E)
    2. Breadth-First-Search
    3. Dijkstra's Algorithm
    4. Topological Sort

    IDIOM
    1. Check -> Mark -> Explore
        - Check: is the node valid, and have we alread visited it
        - Mark: mark the node as visited
        - Explore: recursively visit its neighbors

    Marking Coordinates 3 Ways

    1. Hash Set
        visited = set()

        if (row, col) in visited: 
            return

        visited.add((row,col))
    
    2. 2D Visited Array
        visited = [[False] * COLS for _ in range(ROWS)]

        if visited[row][col]:
            return
        
        visited[row][col] = True

    3. Modify Grid
        if grid[row][col] == "#":
            return
        
        grid[row][col] = "#"

4. Directed and Undirected Edges

5. Indegree is the number of edges that can be used to reach a node

6. Outdegree is the number of edges that are used to leave a node

7. Connected: when there exists a path connecting every single vertex
    - there exists a path between every pair of vertices

8. Disconnected: when there is at least one pair of vertices thta has no path that connects them together

Types of Graphs

    - Undirected (refers to direction of edges)
    - Directed
    - Sparse (number of edges is much smaller than the max possible number of edges between its vertices)
    - Dense (graph in which the number of edges is close to teh maximum possible number of edges)
    - Weighted Graph
    - Unweighted (refers to value or cost of edges)
    - Acyclic (a finite directed graph with no directed cycles)
    - Cyclic (graph that contains atleast one cycle)

Important Connections   What DFS Does
733 Flood Fill          Changes connected cells
463 Island Perimeter    Counts exposed edges
200 # of Islands        Marks connected components
695 Max area of island  Counts cells in each component