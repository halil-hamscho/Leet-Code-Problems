from typing import List

"""
Right away
- if the value was not in equations, then -1
- if it is the same valueand exists then return 1.0

If we represent the variables as relationships
we can model the problem as a bidirectional weighted graph
a -> b is 2
b -> a is 0.5

We utilize BFS
Invariant:
the ratio stored alongside a node represents the starting variable divided by that node's variable

Pattern: Weighted Graph with BFS

Weight Represents
- Ratios (Multiplication)
- Costs (Addition)
- Probabilities (Multiplication)
- Distances (Addition)

- What do the weights represent?
- What is the problem asking?

a -> b is val
b -> a is reciprocal (1 / val)
"""
from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(list)
        for nodes, val in zip(equations, values):
            a = nodes[0]
            b = nodes[1]
            adjList[a].append((b, val))
            adjList[b].append((a, 1 / val))

        
        def bfs(start, stop):
            queue = deque([(start, 1)])
            visited = {start}

            while queue:
                n, current_ratio = queue.popleft()

                if n == stop:
                    return current_ratio

                for neighbor, weight in adjList[n]:
                    if neighbor in visited:
                        continue

                    visited.add(neighbor)
                    queue.append((neighbor, current_ratio * weight))

            return -1.0


        result = []
        for a, b in queries:
            
            if a not in adjList or b not in adjList:
                result.append(-1.0)
                continue

            result.append(bfs(a, b))

        return result

if __name__ == "__main__":
    sol = Solution()
    equations = [["a","b"],["c","d"]]
    values = [1.0, 1.0]
    queries = [["a","c"],["b","d"],["b","a"],["d","c"]]
    result = sol.calcEquation(equations, values, queries)