'''

height = 1 + max(height of left, height of right)
diameter = height of left tree + height of right
keep track of the height and calculate its diameter for each node all the way to the root

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0 # instance variable

    def height_of_node(self,node):
        if node is None:
            return 0
        
        # FIND MAX SUBTREE
        left = self.height_of_node(node.left)
        right = self.height_of_node(node.right)

        # Update the maximum diameter
        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left,right)
    
    def diameterOfBinaryTree(self, root):
        # since we want the diameter ( # of edges between a node)
        # and since it does not have to pass through the root
        # the way we solve it is by taking the maxDepth of left and maxDepth of right and adding them, for each node
        self.height_of_node(root)
        return self.max_diameter