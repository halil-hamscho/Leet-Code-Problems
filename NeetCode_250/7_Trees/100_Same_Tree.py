"""


In 110 Balanced SubTree
- we passed a node and returned two values

In 100 Same Tree
- We pass two nodes and return a single value

Intuition: a recursive function can carry as much information as necessary through its parameters

Parameters carry information downward
Return values carry information upward

Pattern: Recursive DFS, Top Down Approach

- We use information available at the current node to decide what happens next

DFS -> How we explore the tree
PreOrder -> When we process the current Node
Top Down -> How information flows through recursion
Bottom Up -> How results are computed using children's answers

Preorder and top down often appear togetherI s


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:


        def dfs(p, q):

            if not p and not q: # Structures Same
                return True

            if not p or not q: # Structures Differ
                return False

            if p.val != q.val: # Values 
                return False

            bool_l = dfs(p.left, q.left)
            bool_r = dfs(p.right, q.right)

            return bool_l and bool_r


        return dfs(p, q)

if __name__ == "__main__":
    sol = Solution()

    p = TreeNode(1)
    p.right = TreeNode(3)
    p.left = TreeNode(2)


    q = TreeNode(1)
    q.right = TreeNode(3)
    q.left = TreeNode(2)

    print(sol.isSameTree(p, q))
    

