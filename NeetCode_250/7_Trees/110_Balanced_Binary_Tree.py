"""
Pattern: Bottom Up DFS

Intuition:

Each node needs information from its children to determine its own height and whether it is balanced

We know how to calcualate the height of subtrees, but we can also
do comparisons that save us time and optimize

Condition:

A tree is balanced if 
1. Both child subtrees are balanced
2. Difference between heights is at most 1


In bottom up DFS you can return more information that you initially passed
into the function

You pass the current node down the recursion. Once the children have been processed, they return
information to their parent

104 Max Depth, each call returns subtree's height
110 Balanced Binary Tree each call returns both the height and whether the subtree is balanced

Mental Mode:

Pass a node down, gather information from children, and return the results needed by its parent
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:

        def dfs(node):

            if not node:
                return (0, True)

            left_height, left_balanced = dfs(node.left)
            right_height, right_balanced = dfs(node.right)

            if abs(left_height - right_height) > 1:
                return -1, False

            return 1 + max(left_height, right_height), True

        _, balanced = dfs(root)

        return balanced


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    root.right.right.left = TreeNode(200)

    sol = Solution()

    result = sol.isBalanced(root)
    print(result)