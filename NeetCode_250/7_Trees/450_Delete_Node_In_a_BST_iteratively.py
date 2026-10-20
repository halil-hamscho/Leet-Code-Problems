"""

InOrder Predecessor:
- Largest Value in Left Subtree
- No Right Child

Inorder Successor:
- Smallest Value in Right Subtree
- No Left Child

Order of Steps
1. use BST to find node in O(h) time
2. Determine how many children it has
3. Reconnect tree
4. Return potentially updated root
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:

        if not root:
            return None

        prev = None
        curr = root

        while curr:

            if key < curr.val:
                prev = curr
                curr = curr.left

            elif key > curr.val:
                prev = curr
                curr = curr.right

            else:
                # Found Node

                # 0 Children
                if not curr.left and not curr.right:

                    if not prev: # Deleting Root with no children
                        return None

                    if prev.left is curr:
                        prev.left = None
                    elif prev.right is curr:
                        prev.right = None

                # 1 Child
                elif not curr.left:
                    # Only right child
                    if not prev:
                        return curr.right

                    if prev.left is curr:
                        prev.left = curr.right
                    elif prev.right is curr:
                        prev.right = curr.right

                elif not curr.right:
                    # Only left child
                    if not prev:
                        return curr.left
                    
                    if prev.left is curr:
                        prev.left = curr.left
                    elif prev.right is curr:
                        prev.right = curr.left

                else:
                # 2 Children, do Inorder Predecessor or Inorder Successor
                    prev = curr
                    successor = curr.right

                    while successor.left:
                        prev = successor
                        successor = successor.left

                    # Sucessor has a right child
                    curr.val = successor.val

                    if prev is curr:
                        prev.right = successor.right
                    else:
                        prev.left = successor.right

                break

        return root
                
if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(7)

    result = sol.deleteNode(root)
    print(result)
        