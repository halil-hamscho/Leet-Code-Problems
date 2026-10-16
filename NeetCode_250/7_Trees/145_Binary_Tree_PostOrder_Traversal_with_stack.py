"""

Iteratively Post Order is trickier in the sense that

A node can only be processed once both subtrees are complete
- Left subtree: already completed by our traversal order
- Right subtree: complete if node.right is None or node.right is last_visited
- Otherwise: explore the right subtree before processing the parent

Key Intuition:

The Stack remembers parents waiting to be processed, while last_visited tracks
the most recently completed node
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        result = []
        curr = root
        stack = []
        last_visited = None
        while curr or stack:

            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                # inspect stack
                node = stack[-1]

                if node.right is None or node.right is last_visited:
                    # Process the completed node
                    node = stack.pop()
                    result.append(node.val)
                    last_visited = node

                else:
                    # explore the right subtree
                    curr = node.right

            return result

if __name__ == "__main__":
    # Create Nodes
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.postorderTraversal(root)

    print(result)
        