"""

Intuition:
- We need to pass information down to children this is a Top Down Approach

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        output = 0

        def dfs(node, max_value):

            if not node:
                return 0

            if node.val >= max_value:
                nonlocal output
                output += 1

            left_value = dfs(node.left, max(max_value, node.val))
            right_value = dfs(node.right, max(max_value, node.val))

            return

        return dfs(root, root.val)


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1)
    root.left.left = TreeNode(3)

    root.right = TreeNode(4)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)

    result = sol.goodNodes(root)
    print(result)