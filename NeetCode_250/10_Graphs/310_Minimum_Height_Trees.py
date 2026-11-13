"""
Algorithm: Leaf Pruning

So if we repeatedly remove leaves until one or two nodes remain then we found our most optimal roots


Time Complexity: O(V + E)
adjList O(E)
degree array O(V)
initial leaves O(V)
Leaf Pruning O(V + E)

Space: O(V + E)
adjList: O(V + E)
degree: O(V)
queue: O(V)

Pattern: leaf pruning using BFS

Insight: instead of testing every node as a root, repeatedly eliminate leaves unitl reaching the center of the tree

Invariant: Each pruning round removes the outermost layer while preserving the tree's center

Center of a tree 

processing one layer at a time ensures we remove leaves symmetrically from the outside inward

Main Pattern: BFS with degree tracking to progressively eliminate nodes until only the tree's center remains
"""
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:

        if n == 1:
            return [0]

        adjList = defaultdict(list)
        degree = [0] * n

        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)
            degree[a] += 1
            degree[b] += 1

        queue = deque()

        for i in range(len(degree)):
            if degree[i] == 1:
                queue.append(i)

        remaining = n
        while remaining > 2:
            size = len(queue)

            for _ in range(size):
                node = queue.popleft()
                remaining -= 1

                for neighbor in adjList[node]:
                    degree[neighbor] -= 1
                    
                    if degree[neighbor] == 1:
                        queue.append(neighbor)

        return list(queue)

if __name__ == "__main__":
    sol = Solution()
    edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
    result = sol.findMinHeightTrees(6, edges)