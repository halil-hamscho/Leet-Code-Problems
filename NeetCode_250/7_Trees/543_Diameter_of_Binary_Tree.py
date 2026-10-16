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


