"""

InOrder Predecessor:
- Largest Value in Left Subtree
- No Right Child

Inorder Successor:
- Smallest Value in Right Subtree
- No Left Child

Recursion Concepts:

1. Every recursive call returns the updated root of its subtree
2. Recursion eliminates the need for a parent pointer (prev)
    root.left = self.deleteNode(root.left, key)
3. Each recursive call has its own root variable
4. We can reuse recursion to delete the inorder successor
root.val = successor.val
root.right = self.deleteNode(root.right, successor.val)
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

        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        else:
            # Found node to delete
            if not root.left and not root.right:
                return None

            elif not root.right:
                # Left One Child
                return root.left

            elif not root.left:
                # Right One Child
                return root.right

            else:
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

                return root
            
        return root
                
if __name__ == "__main__":

    sol = Solution()

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)

    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    root.right.right = TreeNode(7)

    result = sol.deleteNode(root, 3)
    print(result)
        