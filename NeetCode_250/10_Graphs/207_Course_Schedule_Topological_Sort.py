"""

Topological Sort:
    - Detects Cycles through unresolved dependencies
    - Uses indegree and a queue

    Kahn's algorithm detects cycles because nodes involved in a cycle
    can never have their remaining indegree reduced to zero

Pattern: Topological Sorting using BFS and indegree

Intuition: Repeatedly process nodes with indegree of 0

Invariant: a node enters the queue only when all of its dependencies (indegree of 0) have been satisfied

Time: O(V + E)
- adjList: O(E)
- queue: O(V)
- BFS: O(V + E)

Space: O(V + E)
- adjList: O(V + E)
- queue: O(V)
- indegree: O(V)


"""
from collections import defaultdict
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        # Populate adjList (b to a)
        for a, b in prerequisites:
            indegree[a] += 1
            adjList[b].append(a)

        queue = deque([]) # Traverse Using Topo Sort
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0
        while queue:
            node = queue.popleft()
            completed += 1

            for neighbor in adjList[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if completed == numCourses:
            return True
        else:
            return False
        

if __name__ == "__main__":
    sol = Solution()
    result = sol.canFinish(numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]])