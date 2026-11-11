"""


"""
from collections import deque, defaultdict

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """
        In this implementation we are running BFS every single time from start to target
        Time: O(V + E + Q(V + E))
        - adjList: O(V + E)
        - Q = number of queries
        """
        
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)

        result = []
        def bfs(start, target):
            visited = {start}
            queue = deque([start])
            while queue:
                node = queue.popleft()

                for neighbor in adjList[node]:

                    if neighbor in visited:
                        continue

                    if neighbor == target:
                        return True

                    visited.add(neighbor)
                    queue.append(neighbor)

            return False

        for start, target in queries:
            result.append(bfs(start, target))

        return result

    def checkIfPrerequisite2(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """

        Pattern: Directed Graph, BFS, Reachability Precomputation

        In this implementation, we run BFS for each starting course, rather than adding every course to the same queue
        
        Run BFS once from each course and store all reachable nodes
        This allows us to answer subsequent queries in O(1) average time
        Precomputation of the queries
        V = courses
        E = prerequisites
        Q = queries

        Time: O(V(V + E) + Q)
        Space: O(V^2 + E + Q)
            Reachable Set can store O(V^2) entires
            adjList: O(V + E)
            results: O(Q)
        """
        
        adjList = defaultdict(list)
        for a, b in prerequisites:
            adjList[a].append(b)


        hashmap = defaultdict(set) # store results
        def bfs(start):
            queue = deque([start])
            while queue:
                node = queue.popleft()

                for neighbor in adjList[node]:

                    if neighbor in hashmap[start]:
                        continue

                    hashmap[start].add(neighbor)
                    queue.append(neighbor)

            return 

        for i in range(len(numCourses)):
            bfs(i)

        result = []
        for start, target in queries:
        
            if target in hashmap[start]:
                result.append(True)
            else:
                result.append(False)

        return result

    def checkIfPrerequisite3(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        """

        Topological Sort for this
            - Calculate Indegree of every node
            - Add nodes with 0 indegree to the queue
            - remove a node from queue and process it
            - decrease the indegree
            - add neighbors to the queue when their indegree reaches 0


        Time: O(V + E + VE + Q)

        Space: O(V^2 + E + Q)

        Invariant:
            When we process an node -> neighbor
                1. Node is a direct prerequisite of neighbor
                2. Every prerequisite of node is also an indirect prerequiste of neighbor

        With Topological Sorting
        - we turn the prerequisite's DIRECT relationships and populate a 
        prereqs: defaultdict(set) that also contains INDIRECT relationships

        What it boils down to
        Topological Sort gurantees that when we process a node, we've already accumulated all of its prerequisites
        
        
        """

        adjList = defaultdict(list)

        indegree = [0] * numCourses
        for a, b in prerequisites:
            indegree[b] += 1
            adjList[a].append(b)

        queue = deque()
        prereqs = defaultdict(set)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
 
        while queue:
            node = queue.popleft()

            for neighbor in adjList[node]:
                indegree[neighbor] -= 1

                # Accumulate prerequisite information
                prereqs[neighbor].add(node)
                prereqs[neighbor].update(prereqs[node])

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        result = []
        for a, b in queries:
            result.append(a in prereqs[b])
        return result

if __name__ == "__main__":
    sol = Solution()
    numCourses = 3
    prerequisites = [[1,2],[1,0],[2,0]]
    queries = [[1,0],[1,2]]
    result = sol.checkIfPrerequisite3(numCourses, prerequisites, queries)