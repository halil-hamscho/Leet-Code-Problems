"""

Decisions:
- rob or skip

State:
    dp[i] = max amount robbed so far

Recurrence
    dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

Base Cases:
    - dp[0] = nums[0]
    - dp[1] = max(nums[0], nums[1])

State: the maximum amount of money that can be robbed from houses 0 to i without robbing adjacent houses

Rather than explicitly defining our base cases we can do
prev2 = 0
prev1 = 0
for num in nums:
....

Instead of explicitly initializing the first two DP states,
we can initialize the state before processing any elements
and allow the recurrence to establish the base cases naturally

"""

class Solution:
    def rob(self, nums: list[int]) -> int:

        prev2 = 0
        prev1 = 0
        for num in nums:
            result = max(prev1, prev2 + num)

            prev2, prev1 = prev1, result

        return result
            
    def robRecursion(self, nums):

        if len(nums) <= 2:
            return max(nums)

        memo = {
            0 : nums[0],
            1 : max(nums[0], nums[1])
        }

        def dfs(i):
            if i in memo:
                return memo[i]

            dp = max(dfs(i - 1), dfs(i - 2) + nums[i])
            memo[i] = dp
            
            return dp 

        return dfs(len(nums) - 1)


if __name__ == "__main__":
    nums = [2,1,1,2]
    sol = Solution()
    result = sol.robRecursion(nums)
