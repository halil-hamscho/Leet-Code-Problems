from collections import defaultdict, deque

"""
In this case the problem is constrained with the fact that
- if there are multiple answers, then return the answer that occurs last in the input

Find: Determine which component a node belongs to
Union: merge two components if they are not already connected

If we process each edge using union(a, b)

The key reason why we are able to get the last answer in the input is 
because Union Find processes edges in their original order while
maintaining connectivity informatin

Time: O(V + E x alpha(V))
- Initialization of parent and size O(V)
Processing Edges
- find and union each take O(alpha(V))
since we perform E Union operations -> E x alpha(V)

Space: O(V)

Pattern: Union Find
Recognition: Incrememtally connecting nodes and checking whether they already belong to the same component
"""

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:

        # Problem Gurantees n edges
        n = len(edges)

        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return False

            if size[rootA] < size[rootB]:
                parent[rootA] = rootB
                size[rootB] += size[rootA]
            else:
                parent[rootB] = rootA
                size[rootA] += size[rootB]

            return True

        for a, b in edges:
            if not union(a, b):
               return [a, b]

if __name__ == "__main__":
    sol = Solution()
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    result = sol.findRedundantConnection(edges)