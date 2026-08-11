from collections import deque
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: # empty BST
            return []
        q = deque()
        q.append(root)
        level = 0
        result = []
        while q: # While not empty q
            length_q = len(q) # tells us how many nodes in the curr level
            level_list = []
            for i in range(length_q):
                node = q.popleft()
                if node: # good node
                    level_list.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level_list:
                if level % 2 == 0: # even (right to left)
                    # ways to reverse is 
                    # list.reverse()
                    # list[::-1]
                    # reversed(list) <- this returns an iterator, which you need list() to convert it
                    result.append(level_list[::-1])
                else:
                    # odd (left to right)
                    result.append(level_list)
            level += 1
        return result

def main():
    root = [3,9,20,None,None,15,7]
    result = Solution()
    print(result.zigzagLevelOrder(root))

if __name__ == "__main__":
    main()
        


        