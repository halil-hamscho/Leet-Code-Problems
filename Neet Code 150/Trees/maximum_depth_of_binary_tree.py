'''
Can be solved 3 different ways
It can be solved DFS recursively, iteratively and BFS

in the recursive version what happens is that once we are in a node.val we count it as 1 and then we add the max(dfs(left), dfs(right))


Time Complexity: traversing the entire tree is O(N)
Memory Complexity: If it is not balanced then it is O(N)
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxDepth(self, root):
        # Every time base case
        if root is None:
            return 0 # max depth
        
        # Otherwise, find the max subtree 
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return 1 + max(left, right)

    def maxDepthv2(self, root):
        # BFS Approach
        if root is None:
            return 0
        
        level = 0
        q = deque([root])
        while q: # while it is not empty
            # take a snapshot of the q
            # range of current q, then pop the node, then append the children
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
     
    def maxDepthv3(self, root):
        # DFS Iteratively
        # uSE A CALL STACK
        if root is None:
            return 0
        
        stack = [[root, 1]] # use a pair of values
        result = 1
        while stack:
            node, depth = stack.pop() # getting node and depth
            if node: # prevents from using null nodes
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result

