# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        current_node = root
        
        while current_node: # while it is not null
            if p.val > current_node.val and q.val > current_node.val:
                current_node = current_node.right # update pointer
            elif p.val < current_node.val and q.val < current_node.val:
                current_node = current_node.left
            else: # split occurs or we find the value
                return current_node
            


    # recursive solution
    def lowestCommonAncestor2(self,root, p,q):
        if not root:
            return TreeNode(-1)
        
        curr_node = root

        if p.val < curr_node.val and q.val < curr_node.val:
            return self.lowestCommonAncestor2(curr_node.left, p, q)
        elif p.val > curr_node.val and q.val > curr_node.val:
            return self.lowestCommonAncestor2(curr_node.right, p, q)
        else:
            return curr_node

