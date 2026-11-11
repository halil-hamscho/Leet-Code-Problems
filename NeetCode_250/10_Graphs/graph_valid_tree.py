from typing import List

"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes)
write a function to check whether these edges make up a valid tree.

Valid Tree:
    - No cycles
    - Connected: every node must be reachable from every other node

For cycle detection in an undirected graph:
    - When examining neighbor
        1. If it is the parent, ignore it
        2. If it is already visited, and is not the parent, a cycle exits
        3. Otherwise, discover it and continue traversing

Mark nodes as visited when you enqueue them, not when you dequeue them

In an undirected graph, checking neighbor == parent allows us to ignore the
reverse direction of the edge we just traversed. This prevents us from 
mistakenly detecting a cycle when revisiting the parent
While still allowing us to detect actual cycles when encountering other previously visited nodes

Pattern: BFS with cycle detection in an undirected graph

Insight: A valid tree must be connected and no cycles

Time: O(V + E)
- adjList: O(V + E)
- BFS O(V + E)

Space: O(V + E)
- adjList: O(V + E)
- queue: O(V)
- set: O(V)

"""
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        adjList = defaultdict(list)
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        queue = deque([(0, -1)])
        visited = {0}

        while queue:
            node, parent = queue.popleft()

            for neighbor in adjList[node]:

                if neighbor == parent:
                    continue
                
                if neighbor in visited:
                    return False

                visited.add(neighbor)
                queue.append((neighbor, node))

        return len(visited) == n


if __name__ == "__main__":
    sol = Solution()
    result = sol.validTree(n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]])

