# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return result
        
        queue = deque([root])

        # will need to do BFS and get the rightmost node
        while queue:
            level_length = len(queue)
            for i in range(level_length):
                # first get the level length before you start using the nodes
                node = queue.popleft()
                if i == level_length - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result




        