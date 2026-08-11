class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        '''
        3 Scenarios here
        1. p and q are in different sub-trees (left and right of current node)
            -> curr is LCA
        2. q is in a sub-tree of p
            -> p is LCA
        3. p is in a sub-tree of q
            -> q is LCA
        '''
        # base case
        if not root:
            return None
        
        # Found p or q in the subtree
        if root.val == p.val or root.val == q.val:
            return root
        
        # check if p and q exist in left subtree or right subtree
        left = self.lowestCommonAncestor(root.left, p, q) # node or None
        right = self.lowestCommonAncestor(root.right, p, q) # node or None

        # return curr node, when p and q are in diff sub-trees
        if left and right:
            return root
        
        # else return l or r
        return left or right
    
    def lowestCommonAncestor_2(self, root, p, q):
        # time complexity, height of tree O(log n), memory O(1)
        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr




        
        