"""
Pattern: BFS with queue, utilizing level order traversal

Same pattern as 102 Binary Level Order Traversal

In this case, the last value in the queue is my default the right side view

the way we can do that is when we are doing the level order traversal
we check

if i == level_len - 1:
    result.append(node.val)

Time: O(n)
Space:
- O(w) for deque (longest diameter)
- O(h) for auxiliary since we keep track of a len of nodes since one value per level

"""

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:

        if not root:
            return []
        
        result = []
        queue = deque([root])
        while queue:
            level_len = len(queue)

            for i in range(level_len):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                if i + 1 >= level_len: # or i == level_len - 1
                    result.append(node.val)

        return result
                    
if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)

    result = sol.rightSideView(root)
    print(result)