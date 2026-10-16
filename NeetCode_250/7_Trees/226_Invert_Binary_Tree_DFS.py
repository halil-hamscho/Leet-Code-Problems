# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:

        curr = root

        def dfs(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return root

if __name__ == "__main__":
    sol = Solution()

    # Input: [4, 2, 7, 1, 3, 6, 9]

    # Expected: [4, 7, 2, 9, 6, 3, 1]

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    result = sol.invertTree(root)

    # Level Order Traversal to verify output
    from collections import deque

    queue = deque([result])
    output = []

    while queue:
        node = queue.popleft()
        output.append(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    print(output)
