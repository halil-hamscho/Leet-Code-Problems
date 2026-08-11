'''
Given a binary tree, determine if it is 
height-balanced


we will be using a two position array to help us keep track of T/F and also a height

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root) -> bool:

        def dfs(root):
            # return boolean and height
            if root is None:
                # empty tree
                return [True, 0]
            # determine left and right subtrees
            left, right = dfs(root.left), dfs(root.right)
            # from the root node is it balanced
            # is the tree balanced at all (left subtree, right subtree and from the root tree)
            # balanced is a boolean
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) # the index 1 is the height

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]

    
        