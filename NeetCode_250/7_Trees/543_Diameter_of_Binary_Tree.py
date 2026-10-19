"""

Pattern: Bottom Up DFS + external variable tracking

Invariant: After processing a subtre, DFS returns its correct height
max_diameter includes the longest path discovered in that subtree

Python Takeaway: non local allows a nested function to modify a variable

Recognition Heuristic:
- When the answer could occur anywhere in the tree, but each node needs information
from its children, consider a bottom up DFS with a separate variable tracking the best answere

Remember:
- What a recursive function returns does not necessarily have to be the final answer you're looking for.

Another takeaway is that

after we finish the subtree calculations (left_height, right_height)

we can then find the max_diameter
"""


from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        max_diameter = 0

        def dfs(node):
            if not node:
                return 0

            nonlocal max_diameter

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            max_diameter = max(max_diameter, left_height + right_height)

            return 1 + max(left_height, right_height)

        dfs(root)

        return max_diameter

if __name__ == "__main__":
    
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = sol.diameterOfBinaryTree(root)

    print(result)


