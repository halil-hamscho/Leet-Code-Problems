"""
Pattern: Bottom Up Recursion, Tree DP Problem

Takeaway:
- We use bottom up recursion, since we want to pass the 2 states to the parent
    (rob_current, skip_current)

Time: O(n)
Space: O(h) recursive call stack

Botom up DFS determines the information flow. DP states determine what information is returned.
State transitions determine how that information is calculated
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def dfs(node):

            if not node:
                return (0, 0)

            # Max Amount if we rob root vs. skip root
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # Calculate rob_current
            rob_current = node.val + left_skip + right_skip

            # Calculate skip_current
            skip_current = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob_current, skip_current)

        curr, skip = dfs(root)

        return max(curr, skip)


if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.right = TreeNode(1)

    sol = Solution()
    result = sol.rob(root)
    print(result)