
"""
Pattern: Post Order DFS

Originally I was doing

- Check if leaf and target

node.left = dfs(node.left)
node.right = dfs(node.right)

return node

However, we need to travel through the children first before we process 

So instead we need to do PostOrder DFS

node.left = dfs(node.left)
node.right = dfs(node.right)

if not node.left and not node.right and node.val == target:
    return None

return node

Now the parent waits until both children have been processed before
decising whether it should be deleted
this allows deletions to propogate upward through the tree

PreOrder: Process current node before its children
Post Order: Process children before making a decision about the parent
Inorder: Process current node between its left and right subtrees

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:

        def dfs(node):
            if not node:
                return

            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if not node.left and not node.right and node.val == target:
                return None
            
            return node
        
        node = dfs(root)
        return node





if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(2)

    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)

    result = sol.removeLeafNodes(root, 2)
    