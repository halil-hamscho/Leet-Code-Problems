"""
Decisions:
    - extend if increasing (i > i - 1)
    - start new

Base Case:
    - len(nums)

State:
    - dp[i] = longest increasing sequence ending at nums[i]

Recurrence:

    - dp[i] = max(eligible items)

Here:

    n states
        at every i state, we have to search through the eligible states and find the max
"""

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 1)


        for index in range(1, n):

            # Check Eligible Items
            curr_max = 0
            for i in range(1, index):
                if nums[index] > nums[i]:
                    curr_max = max(curr_max, dp[i])

            dp[index] += curr_max

        return dp[n]

if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    sol = Solution()
    result = sol.lengthOfLIS(nums)