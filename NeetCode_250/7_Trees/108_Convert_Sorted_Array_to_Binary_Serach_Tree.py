"""

Recursive Tree Construction means
determining the root, recursively constructing its children, and returning the root to its parent

In this case

Using the midpoint takes care of the balancing

Pattern: Divide and Conquer
1. Choose midpoint as root
2. Recursively construct left
3. Recursively construct right
4. Return root to parent

Time: O(n)
Space: O(log n) since tree cannot be skewed


Takeaway: Recursive Functions can return entire subtrees

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode | None:

        def dfs(left, right):

            if left >= right:
                return None

            mid = (left + right) // 2

            root = TreeNode(nums[mid])

            root.left = dfs(left, mid)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(nums))


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    sol = Solution().sortedArrayToBST(nums)
    result = sol.sortedArrayToBST(sol)
    
        