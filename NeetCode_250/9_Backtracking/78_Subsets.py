"""

Two Choices

1. Include the element in the current subset
2. Exclude the elemtn in the current subtree

Pattern: Backtracking (Subsets)

Time Complexity:

Factor 1: Number of subsets -> 2^n
Each element has two choices, include or exclude

nums = [1,2,3]
2^3 = 8 subsets

Factor 2: Copying each subset -> O(n)
- Copying each subset O(n) since at the base case a subset takes O(k) where k is its length

O(n x 2^n)
Intuition: We generate 2^n subsets and saving each one can require copying up to n elements

Space Complexity:

Auxiliary Space: O(n) since the subset can contain at most n elements

recursion can reach a maximum depth of n

Since we store 2^n subsets in result = []

O(n x 2^n)

"""

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        subset = []

        def dfs(index):
            if index == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            dfs(index + 1)

            subset.pop()
            dfs(index + 1)

            return 

        dfs(0)
        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3]
    result = sol.subsets(nums)
    print(result)