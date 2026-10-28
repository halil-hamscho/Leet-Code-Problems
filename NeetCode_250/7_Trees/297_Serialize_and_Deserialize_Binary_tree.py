from collections import deque

"""
Pattern: BFS + Queue

Serialization:
Record every node and its missing child positions

Deserialization: 
Process parents in BFS order, consuming two child positions per parent

Invariant:
- The queue maintains parent order, while null markets preserve the tree's structure

"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        queue = deque([root])

        while queue:

            node = queue.popleft()

            if node:
                result.append(str(node.val))

                queue.append(node.left)
                queue.append(node.right)

            else:
                result.append("null")


        print(",".join(result))

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")

        if data[0] == "null":
            return None
        
        root = TreeNode(int(data[0]))
        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()

            # Process Left Child
            if data[index] != "null":
                left = int(data[index])
                node.left = TreeNode(left)
                queue.append(node.left)
            index += 1

            # Process Right Child
            if data[index] != "null":
                right = int(data[index])
                node.right = TreeNode(right)
                queue.append(node.right)
            index += 1

        return root
        
                
# Your Codec object will be instantiated and called as such:
if __name__ == "__main__":
    
    ser = Codec()
    deser = Codec()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    serialize = ser.serialize(root)
    ans = deser.deserialize(serialize)