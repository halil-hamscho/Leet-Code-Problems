# Definition for a binary tree node.
'''
Path in a binary tree
sequence of nodes where each pair of adjacent
nodes in the sequence has an edge connecting them
a node can only appear in a sequence at most once

The path sum of a path is the sum of the node's 
values in the path

Given the root of a binary tree, return the 
maximum path of sum of any non-empty path

Brute Force:
1. Count every single path
2. Return the max one 

We also need to find the most optimal path

path
node.val + node.val + node.val

How to count a path?
Single nodes count as paths
it is possible that negative values can still
be included in our path

A path cannot go back
a path cannot have a split
If we are starting at a node, we can only split once

WE Cannot split twice

Brute Force:
1. for every single node
what is the max is we do not 

Why start at the root when we can just
use the subproblem


SOLVE BOTTOM UP
O(n)
we prevent duplicate work by working upwards on the tree
we return values

What is the max value that we can
get from the left subtree if we never
end up splitting

Marking the max value we can get
if we do not split


What value do I want to return to parent?
what is teh max that we can get if we are not allowed to split?
1, 2, 3, null, null, 4, 5
3 -> 4, 5
we take 3 + 5 = 8 and we return 8 to the root (1)
Looking at 
Time O(n)
Space O(h) the height of the tree
max(l,r,0)



# with split
root.val + leftMax + rightMax

# without split
root.val + max(leftMax, rightMax)
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root) -> int:
        res = [root.val] # global variable
        # return max path sum without splitting
        def dfs(root):
            if root is None:
                return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            # take care of negative values
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # compute the max path sum WITH SPLIT from the current root
            # take root and add it with the left Max and the Right Max
            res[0] = max(res[0], root.val + leftMax + rightMax)
            
            # without the split
            return root.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]