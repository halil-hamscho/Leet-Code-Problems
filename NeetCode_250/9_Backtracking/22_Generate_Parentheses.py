"""

Pattern: Backtracking (Combinations)

1. Choice:
- open or close
2. State:
- # of pairs?, # of open?, # num of close?
3. Base:
if len(path) == n * 2

4. Recuperation:
- remove parenthesis

Pattern: Constrained sequence construction using backtracking

Invariant
0 <= close_count <= open_count <= n

Time:

Without prunning, since we have two choices at each position,
the sequence contains 2n characters, not n

2^2n = 4^n

Number of valid parentheses combinations is given by Catalan number

Cn = (1 / (n + 1)) * ( (2n) / n)

Each combination requires O(n) time to construct its string using "".join(path)

Time: O(n Cn)

Space: O(n Cn)
Auxiliary:
path: O(n)
stack: O(n)

output space: Cn strings, each contraining 2n characters
"""
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []
        path = []
        def dfs(open_count, close_count):
            if len(path) == n * 2:
                result.append("".join(path))
                return

            if open_count < n:
                path.append("(")
                dfs(open_count + 1, close_count)
                path.pop()

            if open_count > close_count:
                path.append(")")
                dfs(open_count, close_count + 1)
                path.pop()

            return
        
        dfs(0, 0)
        return result
        
if __name__ == "__main__":
    result = Solution().generateParenthesis(n = 3)
    print(result)

