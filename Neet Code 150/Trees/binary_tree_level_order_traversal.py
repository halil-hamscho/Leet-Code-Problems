# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        result = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = [] # refreshes in every iteration of the q
            # loop through every single value in q
            for _ in range(qLen): # going through level at a time
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # make sure it doesn't add any null nodes
                result.append(level)
        return result






        if not root:
            return []
        
        explored = []
        queue = deque([root])

        while deque:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            explored.append(current_level)
        
        return explored

def build_tree(values):
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        
        i += 1
    return root


def main():
    print()
    values = [3,9,20]
    root = build_tree(values)

    solution = Solution()
    result = solution.levelOrder(root)
    print(result)

if __name__ == "__main__":
    main()

            
        
        