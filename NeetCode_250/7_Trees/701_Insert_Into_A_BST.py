"""
Pattern: BST Traversal + Insertion

In this case, we utilize the property of the BST to tell us where to traverse to

if val < curr.left: -> go left
if val > curr.right -> go right

if at any point (left or right) the next node is None, then that means that is our insertion spot

Time: O(h) where h is the height of the tree (balanced)
Space: O(1)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:

        if not root:
            return TreeNode(val)

        curr = root
        while curr:

            if val < curr.val:
                if not curr.left:
                    curr.left = TreeNode(val)
                    return
                
                curr = curr.left

            elif val > curr.val:
                if not curr.right:
                    curr.right = TreeNode(val)
                    return
                
                curr = curr.right

        return root

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    result = sol.insertIntoBST(TreeNode(5))
