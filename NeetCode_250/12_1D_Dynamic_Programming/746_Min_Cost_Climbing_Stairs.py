"""
State: dp[i] = minimum cost to reach stair i + cost[i]
Decisions: i - 1, i - 2
Base Cases: dp[0] = cost[0], dp[1] = cost[1]
Recurrence: dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

Takeaway: Each state depends on the previous 2 states, choose the cheaper path
"""

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        n = len(cost)
        dp = [0] * (n)

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]

        return min(dp[n - 1], dp[n - 2])

    def minCostRecursive(self, cost):

        memo = {
            0: cost[0], 
            1: cost[1]
            }
        
        def dfs(i):
            if i in memo:
                return memo[i]

            dp = min(dfs(i - 1), dfs(i - 2)) + cost[i]

            memo[i] = dp

            return dp
        
        n = len(cost) - 1

        return min(dfs(n), dfs(n - 1))

if __name__ == "__main__":
    cost = [1,100,1,1,1,100,1,1,100,1]
    sol = Solution()
    result = sol.minCostRecursive(cost)