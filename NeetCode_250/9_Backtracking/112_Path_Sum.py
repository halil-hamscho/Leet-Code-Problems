"""

def modify(x):
    x -= 5
    print("Inside:", x)

x = 20
modify(x)
print("Outside:", x)

Inside: 15
Outside: 20

With strings and integers, since the change does not affect the parent (due to immutability)
we do not have to change back the state/undo the state after we recursively traverse


Shared State vs. Local State

It is preferred to use local state when possible, since it makes recursion easier to 
reason about and reduces the risk of backtracking mistakes

Use shared mutable state when necessary such as maintaing a path, visited set, or modifying a board
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:

        if not root:
            return False

        def dfs(node, remaining):
            if not node:
                return False

            remaining -= node.val

            if not node.left and not node.right:
                return remaining == 0

            if dfs(node.left, remaining):
                return True

            if dfs(node.right, remaining):
                return True
            
            return False 

        return dfs(root, targetSum)


if __name__ == "__main__":

    # Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1]
    # targetSum = 22

    root = TreeNode(5)

    root.left = TreeNode(4)
    root.right = TreeNode(8)

    root.left.left = TreeNode(11)

    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)

    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)

    root.right.right.right = TreeNode(1)

    targetSum = 22

    sol = Solution()
    result = sol.hasPathSum(root, targetSum)

    print("Result:", result)
    print("Expected:", True)