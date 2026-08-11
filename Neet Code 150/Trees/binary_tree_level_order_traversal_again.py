from collections import deque

class Node:
    def __init__(self, val = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result = [] # append each [level]
        q = deque() # BFS is through a queue
        q.append(root) # initialize

        while q: # While not empty
            # Len of q, tells us the current number of nodes in the queue
            length_q = len(q)
            level = [] # Level List
            for i in range(length_q):
                node = q.popleft()
                if node: # Not Null
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level: # Not Empty
                result.append(level)
        return result

def main():
    pass

if __name__ == "__main__":
    main()
        