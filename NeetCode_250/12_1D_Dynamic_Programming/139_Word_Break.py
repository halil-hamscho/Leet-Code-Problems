"""

Decisions:
    - s[i] extend
    - segment

Without memoization: O(2^n) decisions, and since we do string copy Upper Bound: O(n * 2^n)

Pattern: Dynamic Programming with Memoization

Base Case: when i == len(s), return True

Takeaway: different recursive branches reach the same remaining problem, memoization prevents you from solving
that problem repeatedly

Time: O(n^3) cubic time
- n unique recursive states O(n) (n starting indices)
- n decisions per state O(n) (for loop explores up to n possible endings for each index)
    Each state evaluates up to n possible word boundaries in the worst case.
- python cost of slicing O(n)

Space: O(n)
Auxiliary O(n)
failed set: O(n)
call stack: O(n)
substring: O(n)

"""
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        hashset = set(wordDict)
        failed = set()

        def dfs(index):
            if index == len(s):
                return True

            if index in failed:
                return False

            for i in range(index, len(s)):


                word = s[index : i + 1]
                if word in hashset:
                    if dfs(i + 1):
                        return True

            failed.add(index)
            return False

        return dfs(0)

if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet","code"]
    sol = Solution()
    result = sol.wordBreak(s, wordDict)