"""

Two Independent Processes:

1. Traversal of Root: Find potential candidates

2. Comparison: For each candidate, check whether subtree matches subRoot


Time: O(n x m)
n = nodes in root
m = nodes in subroot

Space:
2 recursion stacks h1, h2
Balanced: O(log n + log m)
Skewed: O(n + m)

Pattern: Recursive DFS + Tree Comparison

Python Concept:
Boolean short cicuting
return traversal(node.left) or traversal(node.right)

Recursion explores the tree. Return values communicate results back to the patern.
Boolean operators combine those results

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:


        def traversal(node):

            if not node:
                return False

            if isSame(node, subRoot):
                return True
            
            left = traversal(node.left)
            right = traversal(node.right)

            return left or right

        def isSame(r, s):

            if not r and not s:
                return True

            if not r or not s:
                return False

            if r.val != s.val:
                return False

            return isSame(r.left, s.left) and isSame(r.right, s.right)

        return traversal(root)

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    subroot = TreeNode(4)
    subroot.left = TreeNode(1)
    subroot.right = TreeNode(2)

    result = sol.isSubtree(root, subroot)
    print(result)