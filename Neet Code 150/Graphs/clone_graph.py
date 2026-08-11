"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node] 
            
            copy = Node(node.val)
            oldToNew[node] = copy # mapping it Ex. 1:1
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy
        return dfs(node) if node else None
    
def main():
    adjList = [[2,4],[1,3],[2,4],[1,3]] 
    result = Solution()
    print(result.cloneGraph(adjList))

if __name__ == "__main__":
    main()