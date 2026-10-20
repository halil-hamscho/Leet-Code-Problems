"""
Pattern: BST Guided Search using Iteration

Recognition: The BST ordering property allows us to eliminate entire subtrees without explorin gthem

Invariant: The LCA must be the current node or somewhere in its subtree

Python Takeaway: A simple while curr: loop can replace recursion when we only need one path

Time: O(h) since we only need to go down one path downward
Space: O(1) 
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        curr = root

        while curr:

            if p.val < curr.val and q.val < curr.val:
                # Move Left
                curr = curr.left

            elif p.val > curr.val and q.val > curr.val:
                # Move Right
                curr = curr.right

            else:
                return curr

        return curr

def main():
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)

    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)

    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left        # Node 2
    q = root.left.right.right # Node 5

    sol = Solution()
    result = sol.lowestCommonAncestor(root, p, q)

    print(result.val if result else None)


if __name__ == "__main__":
    main()

