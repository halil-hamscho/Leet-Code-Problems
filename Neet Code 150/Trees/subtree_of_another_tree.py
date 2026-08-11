'''
Time Complexity is the size of both trees
s is root
t is subroot
O(s * t)

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        # if T is empty, then it is a subtree regardless
        if not subRoot:
            return True
        # if the if statement did not trigger, we know T is NOT empty
        if not root: # order here matters
            return False
        # check current root and subroot
        if self.sameTree(root, subRoot):
            return True
        # not the same tree, but remember we have recursive functions
        # check if it is a subtree of either left or right
        # 
        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
# helper function
    def sameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))
        

    