"""
Main Pattern: Recursive Tree Construction using two traversal arrays

Need pre_order_index += 1 as a way to traverse the preorder array
preorder array tells us what we have built so far

left, right boundaries are the boundaries that define inorder array

Key Insight: Preorder identifies the next root, while in order determines the boundaries of its subtrees

Invariant:
- Each dfs(left, right) call builds the subtree represented by the
inorder interval [left, right)
The preorder index awlays points to the next unused element

Preorder -> construction order
Inorder -> boundary order

We use a hashmap of value: index for inorder_index since that is the 
boundaries that we need to utilize

Time: O(n)
- building hashmap O(n)
- constructing n tree nodes O(n)

Space: O(n)
- Hashmap Space: O(n)
- Recursive call stack O(h)


"""
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        inorder_index = {value: index for index, value in enumerate(inorder)}

        pre_order_index = 0
        def dfs(left, right):
            nonlocal pre_order_index

            if left >= right:
                return

            root = TreeNode(preorder[pre_order_index])
            pre_order_index += 1

            root.left = dfs(left, inorder_index[root.val])
            root.right = dfs(inorder_index[root.val] + 1, right)

            return root

            
        return dfs(0, len(preorder))

if __name__ == "__main__":
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)

    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    result = sol.buildTree(preorder, inorder)
    print(result)