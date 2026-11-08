"""
# Definition for a Node.

The give node will always be the first node with val 1

Pattern: Graph traversal + cloning
Algorithm: BFS

Time: O(V + E)
V = Number of Vertices (nodes)
E = Number of Edges (connections)

Every Node is Cloned exactly once -> V
We process all edges/neighbors -> E

Space: O(V)
- Map and Queue take up O(V)

Python Concepts:
- BFS, deque, dictionary keys

When ever we are asked to clone something,
always think, can I keep a mapping between the original and the copy

"""
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        clones = {} # Original Node: Cloned Node
        queue = deque() # What we need to traverse

        clones[node] = Node(node.val)
        queue.append(node)

        while queue:
            n = queue.popleft()
            copy = clones[n]
            for neighbor in n.neighbors:

                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                copy.neighbors.append(clones[neighbor])

        return clones[node]


if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    # Establish Connections
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    sol = Solution()
    result = sol.cloneGraph(node1)
        