"""

Problem: distinct ways can you climb to the top

Decisions:
    - climb 1 step
    - climb 2 steps

State:

    dp[i]: number of distinct ways to reach step i

Base Cases:

    dp[1] = 1
    dp[2] = 2 (1 + 1 or 2)

Recurrence:

    - count the number of paths so far

    dp[i] = dp[i - 1] + dp[i - 2]

    every path to step i must come from step i - 1 or step i - 2

Time: O(n)
Space: O(n)
"""
class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {1:1, 2:2}
        def dfs(i):
            if i in memo:
                return memo[i]

            memo[i] = dfs(i - 1) + dfs(i - 2)
            
            return memo[i]
        
        return dfs(n)

if __name__ == "__main__":
    sol = Solution()
    result = sol.climbStairs(n = 5)