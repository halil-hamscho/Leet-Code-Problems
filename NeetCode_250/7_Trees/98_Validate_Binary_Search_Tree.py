"""
Pattern: Top Down DFS with inherited boundaries


A BST requires more than checking immedaite children
Every node must respect the constraints establish by all its ancestors

Instead of validating entire subtrees and returnign their minimum 
and maximum values, we pass two boundaries downward

lower < node.val < higher

left subtree
lower < node.left < node.val

right subtree
node.val < node.right < higher

Python Intuition:
start the boundaries with
- negative inf
- postive inf

Time: O(n)
Space: O(h)
- Unskewed log(n)
- Skewed O(n)

Top Down DFS was a good pattern beacuse we can express
validity using contraints passed from ancestors
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def dfs(node, lower, higher):
            
            if not node:
                return True
                
            if not lower < node.val < higher:
                return False

            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, higher)
            
        return dfs(root, float("-inf"), float("inf"))
            
            