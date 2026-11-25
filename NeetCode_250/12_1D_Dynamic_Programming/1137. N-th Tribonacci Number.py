"""
Pattern: 1D Dynamic Programming

State:
dp[i] = Tribonacci sequence at index i

Recurrence:
dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

Base Cases:
dp[0] = 0
dp[1] = 1
dp[2] = 1

Takeaway:
when recurrence depends on a fixed number of previous states you can
eliminate the DP array and maintain only the necessary states

"""

class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        prev1 = 1
        prev2 = 1
        prev3 = 0
        for _ in range(3, n + 1):
            result = prev3 + prev2 + prev1

            prev3 = prev2
            prev2 = prev1
            prev1 = result

        return result

    def tribonacciRecursion(self, n):
        memo = {
            0: 0,
            1: 1,
            2: 1
        }

        def dfs(i):
            if i in memo:
                return memo[i]

            dp = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)

            memo[i] = dp

            return dp
        dfs(n)
        return memo[n]

if __name__ == "__main__":
    n = 4
    sol = Solution()
    result = sol.tribonacciRecursion(n)
    print(result)