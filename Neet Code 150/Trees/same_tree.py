'''
Given two trees, how do we know if they are equal?

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            # if both trees are null
            return True
        if not p or not q:
            # only one of them is null
            return False
        if p.val != q.val:
            # values are no the same
            return False
        # will return true if both left and right are true
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        




        