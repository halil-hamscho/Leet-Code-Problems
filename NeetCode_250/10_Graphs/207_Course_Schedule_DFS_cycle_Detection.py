"""

Pattern:
- Directed Graph/Adjancency List

prereq[i] = [a, b]
b first then a
b -> a
Adjacency List?

2 Ways:
    - 1. DFS with Backtracking/Cycle Detection
        - Unvisited
        - Visiting
        - Visited
    - 2. Topological Sorting
        - indegree #
        - queue

Pattern: Directed Graph + DFS Cycle Detection

Intuition: DFS encounters a node that is still being explored in the current recursion path

visiting = current recursion path
visited = completely explored, safe

Time: O(V + E)
Each vertex is fully explored at most once, and each directed edge is examined at most once

Space: O(V + E)
Adjacency List: O(V + E)
visiting: O(V)
visited: O(V)
DFS recursion stack: O(V)

Important Lessons
1. Mark the current node
2. Backtrackingis essential
3. Dead end is not a cycle, it simply means DFS can finish exploring that path
"""
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        adjList = defaultdict(list)
        visiting = set()
        visited = set()

        for a, b in prerequisites:
            adjList[b].append(a)

        def dfs(node):
            # Check node's state
            if node in visiting:
                return False
            
            if node in visited:
                return True

            # Mark the current node as visiting
            visiting.add(node)

            # Explore it's neighbors
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False

            # Mark the current node as finished
            visiting.remove(node)
            visited.add(node)

            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False

        return True
    
if __name__ == "__main__":
    sol = Solution()
    result = sol.canFinish(numCourses=6, prerequisites=[[1,0],[1,2],[3,1],[3,2],[2,4],[4,5],[2,5]])