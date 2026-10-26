"""
Dynamic Programming Pattern:

1. STATE: What does dp[i] represent?
2. CHOICES: What decisions can I make?
3. TRANSITION: How do those decisions depend on smaller states?
4. BASE CASE: What do I already know?
5. ORDER: In what order can I calculate the states?

- Memoization (Top Down)
- Tabulation (Bottom Up)

We will keep dp[i] where 
dp[i] = max money we can rob from houses 0 thorugh i 
stores the optimla answer for each smaller subproblem

nums = [2, 7,  9,  3,  1]
dp   = [2, 7, 11, 11, 12]

In this answer, we use a bottom up approach (tabulation)
where we start with the smallest possible answers, the build up
"""


class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]
        
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

        return dp[-1]

if __name__ == "__main__":
    result = Solution().rob(nums = [2,7,9,3,1])