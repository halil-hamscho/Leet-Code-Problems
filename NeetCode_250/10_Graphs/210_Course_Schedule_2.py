"""
Due to the fact that we need to return the ordering, Topological Sort is more intuitive

If we used DFS + Backtracking we 
explore the path
Ex. 0 -> 1 -> 2 then return [2, 1, 0] so we would have to reverse the string

"""
from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        adjList = defaultdict(list)
        indegree = [0] * numCourses

        # Populate adjList
        for a, b in prerequisites:
            adjList[b].append(a)
            indegree[a] += 1

        # Populate Starting Points of queue (indegre == 0)
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)

        completed = 0
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)

            for neighbor in adjList[node]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    completed += 1
                    queue.append(neighbor)

        if completed == numCourses:
            return result
        else:
            return []

if __name__ == "__main__":
    sol = Solution()
    result = sol.findOrder(numCourses=4, prerequisites=[[1,0],[2,0],[3,1],[3,2]])