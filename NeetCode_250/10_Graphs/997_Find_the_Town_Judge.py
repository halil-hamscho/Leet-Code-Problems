"""
Pattern: Graph degree counting

Recognition Clues:
- problem describes directed relationships
- you're looking for someone who receives relationships from everybody
- looking for a person with no outgoing relationships
- no path exploration or connectedness

- use adjacency list when you need to know which vertices are connected
- use degree counters when you only need to know how many edges enter or leave each vertex


Graphs:

Town Judge Vertex needs
- 0 outdegree
- n - 1 indegree

Turning the adjacency list into a hashmap of
Vertex: [Vertex1, Vertex2]
Outdegree is the len(list)

Adjacency List [a, b]
every pair represents an incoming edge for b

Algorithm:

1. Initialize Dictionaries: O(n)
2. Process the trust relationships: O(m)
3. Find the judge: O(n), examine every person

O(n + m + n) = O(n + m)
n = number of people (vertices)
m = number of trust relationships (edges)

Space: O(n + m)
- indegree dictionary: O(n) one count per person
- adjacency list: O(n + m) storing every vertex and trust relationship

Time: O(V + E)
Space: O(V + E)

we can also remove the adjacency list and instead just have an outdegree map as well


in that case we save on space complexity and go to O(V)
"""
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:

        hashmap = {num:[] for num in range(1, n + 1)} # adjacency list node:node
        indegree = {num: 0 for num in range(1, n + 1)}

        for pair in trust:
            a = pair[0]
            b = pair[1]
            hashmap[a].append(b)
            indegree[b] += 1

        for key in hashmap.keys():
            if not hashmap[key] and indegree[key] == n - 1:
                return key

        return -1

    def findJudge(self, n: int, trust: list[list[int]]) -> int:


        outdegree = {num: 0 for num in range(1, n + 1)} 
        indegree = {num: 0 for num in range(1, n + 1)}

        for pair in trust:
            a = pair[0]
            b = pair[1]
            outdegree[a] += 1
            indegree[b] += 1

        for i in range(1, n + 1):
            if not outdegree[i] and indegree[i] == n - 1:
                return i

        return -1


if __name__ == "__main__":
    sol = Solution()
    result = sol.findJudge(n=3, trust = [[1,2], [2,3]])
            
        