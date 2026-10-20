"""
Pattern: BFS with Queue

The difficulty here is grouping the levels
the way we do it is by tracking the len of the queue and grouping by that length

at the beginnign of each level, the queue contains the nodes belonging to that level

level_len = len(queue)
for _ in range(level_len):

Time: O(n)
Space: O(w)
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:

        queue = deque([root])
        result = []
        while queue:
            level_length = len(queue)

            list = []
            for _ in range(level_length):
                node = queue.popleft()
                list.append(node.val)
                queue.append(node.left) if node.left else _
                queue.append(node.right) if node.right else _

            result.append(list)
    
        return result

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sol.levelOrder(root)