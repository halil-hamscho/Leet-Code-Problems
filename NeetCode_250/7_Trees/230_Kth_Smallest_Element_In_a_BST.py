"""
Pattern: BST + In Order Traversal

For a BST, in order traversal gives
Left -> Node -> Right
which is in Ascending Order

in this case, since we want the kth smallest
we basically just iterate until k == 0

so we should use nonlocal/shared state to accomplish it

Time: O(h + k)
where
balanced tree -> h = log n
skewed  tree -> h = n

Space: O(h) for the recursive call stack
balanced: O(log n + k)
Skewed: O(n)

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        num = -1

        def dfs(node):
            nonlocal k, num

            if not node or k == 0:
                return

            dfs(node.left)

            if k == 0:
                return

            k -= 1

            if k == 0:
                num = num.val
                return
            
            dfs(node.right)

        dfs(root)

        return num 


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.left.left.left = TreeNode(1)

    result = sol.kthSmallest(root,3)
    print(result)