"""
Pattern: Bottom Up DFS where we pass the best complete path locally, but return only the best path that the parent can extend

Intuition:

3 Possibilities
1. Node alone: node.val
2. Node + One Child: Can be returned to the parent
3. Node + both Children: Can update the global maximum, but cannot be returned to the parent

Invariant:
A path can extend upward through one child, or connect two children at the current node.
It cannot do both simulataneously because that would create three branches

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        max_path = float("-inf")

        def dfs(node):
            nonlocal max_path
            if not node:
                return 0 

            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))

            max_path = max(max_path, node.val + left + right)

            return node.val + max(left, right)

        dfs(root)

        return max_path


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sol.maxPathSum(root)
    print(result)