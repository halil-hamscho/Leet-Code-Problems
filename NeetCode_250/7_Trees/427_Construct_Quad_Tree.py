from typing import List
"""
# Definition for a QuadTree node.

val:
- 1 is grid of 1's
- 0 if grid of 0's

isLeaf:
- 1 if leaf
- 0 if 4 children

Given a square region of the grid, can I represent it as one node
or must I divide it further


Time: O(n^2 * log(n))
- O(n^2) work per level
- O(log n) since we divide the size by // 2 every time

Space:
Recursion Stack is divided by 2
- Auxiliary Space: O(log n)
- Quad Tree Space: O(n^2) 



Key Intuition: Each recursive call is responsible for constructing and returning the tree representing its current square

Base Case:
All values in the current region are identical. Return leaf node

Recursive Case:
Divide the reion into 4 quadrants, recursively construct their nodes, and return a parent containing those children

Pattern: Divide and Conquer
in this case we are dividing by 4 if the values are not the same
"""

class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        n = len(grid)

        def dfs(row, col, size):

            # 1. Check whether values match
            value = grid[row][col]

            # Base Case
            val_diff = False
            for r in range(row, row + size):
                for c in range(col, col + size):
                    if grid[r][c] != value:
                        # Values Differ
                        val_diff = True
                        break

                if val_diff:
                    break

            # 2. Match, return leaf
            if not val_diff:
                return Node(bool(value), True, None, None, None, None)        

            # 3. Divide by 4

            node = Node(True, False, None, None, None, None)

            half = size // 2

            node.topLeft = dfs(row, col, half)
            node.topRight = dfs(row, col + half, half)
            node.bottomLeft = dfs(row + half, col, half)
            node.bottomRight = dfs(row + half, col +  half, half)

            return node

        return dfs(0,0, n)

if __name__ == "__main__":
    sol = Solution()
    result = sol.construct([[0,1],[1,0]])            


        