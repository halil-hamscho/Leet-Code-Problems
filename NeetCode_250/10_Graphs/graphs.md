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
        Goal: follow one path as deeply as possible before exploring alternatives
        - typically keeps visited cells marked (once cell is processed, no need to process it again)
        - eexplores each reachable node once
        - often O(V + E)
    2. Breadth-First-Search
        - Natural for shortest paths with equal movement costs
        Goal: explore cells in increasing order of distance from its starting point. Thefore the first time BFS reaches a cell, it has found the shortest path to that cell
        - Most commonly used to find the shortest path in a graph
        - Initialize (Queue) -> Process (while queue: pop) -> Explore
            for neighbor in get_neighbors(node):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    3. Dijkstra's Algorithm
    4. Topological Sort
    5. Union Find
    
    Cycle Detection
        1. DFS with cycle detection (backtracking)
            - 3 States
                1. Unvisited: haven't explored this node
                2. Visiting: the node is currently in our DFS recursion path
                3. Visited: we completely explored this node and descendants
            Key Rule: encountering a visting node means a cycle exists

                visiting.add(node)

                for neighbor in adjList[node]:
                    dfs(neighbor)

                visiting.remove(node)
                visited.add(node)

            - "Did I return to something I'm still exploring?"
            
        2. Topological Sorting
            - Indegree: # of incoming edges (prerequisites)
            - Queue: courses with indegree of 0
            Key Rule: if we cannot process all vertices a cycle exists

            If a directed graph has no cycles, repeatedly removing
            nodes with indegree zero will eventually remove every node

            completed = 0
            while queue:
                node = queue.popleft()
                completed += 1

                for neighbor in adjList[node]:
                    indegree[neighbor] -= 1

                    if indegree[neighbor] == 0:
                        completed += 1
                        queue.append(neighbor)

            - "Can I keep completing tasks until none remain?"
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

General BFS Template

from collectiosn import deque

queue = deque([start])
visited = {start}

while queue:
    node = queue.popleft()

    # Process the current node

    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

994 Rotting Oranges
    - add rotten oranges to queue, then explore one level at a time

417 Pacific Atlantic Water FLow
    - start with BFS from all cells bordering each ocean
    - determine which cells can reach the ocean 

More on Topological Sorting
    - The same way
        Visited Set: Gurantees that we've already discovered or processed a particular node, depending on when we mark it

    Topological Sorting (Kahn's Algorithm) gurantees that all predecessors of a node have been processed before we process that node, provided that the graph is
        - a Directed Acyclical Graph (DAG)

    visited tells us something about an individual node
    Topological Order: tells us something about the dependencies between nodes 

Union Find
- a data structure that efficiently answers 2 questions

1. Find: which connected component does a node belong to?
2. Union: Can we merge the connected components containing 2 nodes?

Example: 1, 2, 3, 4, 5
    Process
        - edge [1, 2] (1, 2), 3, 4, 5
        - edge [3, 4] (1, 2) (3, 4), 5
        - edge [2, 3] (1, 2, 3, 4), 5

Union Find maintains that connectivity information as edges are processed
    - particularly useful when a problem involves repeatedly connecting nodes
        and checking whether they already belong to the same component
Union Find typically maintains an array called parent

1. Find(x)
    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    Invariant: every node eventually leads to the root of it's connected component

    With Path Compresion
    def find(x):
        if parent[x] == x:
            return x

        root = find(parent[x])
        parent[x] = root

        return root

    or Python Shortcut
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        
        return parent[x]

2. Union(a, b)
    def union(a, b):
        rootA = find(a)
        rootB = find(b)

        if rootA == rootB:
            return False

        parent[rootB] = rootA
        return True

    - Here we connect the roots to merge components completely

    Optimization: Union by Rank or Union by Size
    - We want to keep the tree depth shallow
    - we maintain an additional array

    parent = list(range(n + 1))
    size = [1] * (n + 1)

    if size[rootA] < size[rootB]:
        parent[rootA] = rootB
        size[rootB] += size[rootA]

    else:
        parent[rootB] = rootA
        size[rootA] += size[rootB]
    
    return True

    With Path compression and union byu size, union find achieves nearly constant time per operation
    - it is amortized time complexity of O(alpha(N)) where alpha is the inverse Ackermann function, which grows extraordinarily slowly

Graph Problem
- Traverse Connected Component -> BFS or DFS
- Count Connected Components -> BFS, DFS, or Union Find
- Detect cycles in an undirected graph -> DFS or Union Find
- Process edges while maintaining connectivity -> Union Find
- Find shortest paths in an unweighted graph -> BFS