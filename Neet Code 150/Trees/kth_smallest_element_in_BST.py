# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k: int) -> int:
        # because we want to find the kth smallest element
        # we should do in order travesal because it gives it to us sorted

        n = 0 # count for the number of nodes visited
        stack = []
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            # finished going all the way left
            curr = stack.pop()
            # processing val
            n += 1
            if n == k: # found the kth smallest
                return curr.val
            curr = curr.right