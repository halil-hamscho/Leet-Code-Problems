class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:

        result = []
        curr = root
        stack = []
        while curr or stack:
            if curr:
                result.append(curr.val)
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                curr = curr.right

        return result
    
if __name__ == "__main__":
    # Create Nodes
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    solution = Solution()
    result = solution.preorderTraversal(root)

    print(result)