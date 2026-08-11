"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

TIme Complexity: O(N) where N is the number of nodes in the given tree
We only traverse the tree once usign BFS which requires O(N)

Space Complexity O(W) where W is the width of the given tree
Since the given tree is a perfect binary tree, the width is given as W = (N+1)/2 = O(N)

"""
from collections import deque

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None # empty Binary Tree
        que = deque([root])
        while que: # while it is not empty
            rightNode = None
            for _ in range(len(q)):
                current = que.popleft()
                current.next = rightNode
                rightNode = current
                if current.right:
                    # extend adds multiple elements to a list
                    que.extend([current.right, current.left])
        return root