"""
Decisions:
    - pick letter
    - pick 2 letters

Base Cases:
    - if not in hashset:
        return
    if i == len(s):
        decode += 1

State:
    - we have a pointer in s that we keep moving

Recurrence:


"""

class Solution:
    def numDecodingsBacktracking(self, s: str) -> int:
        """
        TLE with Backtracking

        Time: O(2^n)
        Space: O(n)
        """
        hashset = set()

        for i in range(1, 27):
            hashset.add(str(i))

        decode = 0

        def dfs(i):
            nonlocal decode

            if i == len(s):
                decode += 1
                return

            if s[i] in hashset:
                dfs(i + 1)

            if i + 2 <= len(s) and s[i: i + 2] in hashset:
                dfs(i + 2)

            return

        dfs(0)
        return decode

    def numDecodingsRecursive(self, s):

        """
        Dynamic Programming Approach
        Top Down Memoization
        """

        hashset = {str(i) for i in range(1, 27)}

        memo = {}

        def dfs(i):

            if i == len(s):
                return 1

            if i in memo:
                return memo[i]

            memo[i] = 0

            if s[i] in hashset:
                memo[i] = dfs(i + 1) 

            if i + 2 <= len(s) and s[i:i + 2] in hashset:
                memo[i] += dfs(i + 2)

            return memo[i]

        return dfs(0)

    def numDecodings(self, s):
        """
        Bottom Up Tabulation
        - start with what we know

        To gurantee the states depend on already calculated values
        iterate right to left

        State:
            dp[i] = number of ways to decode the string

        Recurrence:
            dp[i] = dp[i - 1] + dp[i - 2]

        Base Cases:
            len(1) = 1

        """
        hashset = {str(i) for i in range(1, 27)}

        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1

        for i in range(n - 1, -1, -1):
            if s[i] in hashset:
                dp[i] += dp[i + 1] 

            if i + 2 <= len(s) and s[i:i + 2] in hashset: 
                print(s[i:i + 2])
                dp[i] += dp[i + 2]

        return dp[0]

if __name__ == "__main__":
    s = "226"
    sol = Solution()
    result = sol.numDecodings(s)