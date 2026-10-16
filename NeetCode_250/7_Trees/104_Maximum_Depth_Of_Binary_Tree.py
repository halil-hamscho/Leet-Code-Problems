"""
In this case when calculating the depth of the binary tree

Does the parent need information from its children to compute the answer?
Yes
In this case, we want to return the max height between the left and right subtree to the
parent node

the way we do that is

in our recursion
- Base Case
- Return the height that is passed back to the caller

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:

        def dfs(node):
            if not node:
                return 0

            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return 1 + max(left_height, right_height)

        height = dfs(root) 

        return height 
        

if __name__ == "__main__":
    sol = Solution()

    # Input: [4, 2, 7, 1, 3, 6, 9]
    # Expected: 3

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    result = sol.maxDepth(root)
    print(result)  # Expected: 3