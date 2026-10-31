"""

1. Choices: What can I decide at each step?
- pick number
- skip number

2. State: waht infromation represents my current progress
index of nums

3. Base Case: When have I completed a valid possibility?
- index == len(nums)

4. Restoartion:
what must I undo before exploriung another choice?
pop from path

Pattern: Backtracking with include and exclude decisions

Recognition Heuristic:
Since XOR was a repeatedly calculated value from the curr path,
consider whether that value can be maintained as a recursive state instead

In this case, we go from
dfs(index) -> dfs(index, current_xor)
as a way to save O(n) form the leaf calculation

Time: O(2^n)
since 2 decisions, n subsets

Space: O(n)
since we do not do copying and the n comes from the largest recursive stack

"""


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        result = 0
        def dfs(index, current_xor):
            nonlocal result
            if index == len(nums):
                result += current_xor
                return

            # Choose that number
            dfs(index + 1, current_xor ^ nums[index])

            # Skip number
            dfs(index + 1, current_xor)

            return

        dfs(0, 0)

        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1,3]
    result = sol.subsetXORSum(nums)
