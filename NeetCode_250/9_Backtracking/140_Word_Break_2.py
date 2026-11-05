"""

1. Choices
either add a space, or continue

2. State:
index for s
path that tells us the current string?

3. Base Case:
- index = len(s)
- return, we can or split the string with space " ".join() and add that space

4. Restoration:


Invariant:
check s[:i + 1] if the string is in wordDict, then we do recursion on everything else to the right

Pattern: Backtracking with String Partitioning

a | b | c | d
4 chars, 3 gaps
n - 1 gaps

Time: O(n * 2^n)
exponential partitioning O(2^n)
string copy O(n)
result append O(n)

Space: O(D + Sn)
stack O(n)
path O(n)
dictionary set O(D)
possible exponential partitions S = O(2^n)

REcognition: Find all the ways to partition a sequence into valid contigous pieces


"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        wordHashmap = set(wordDict)
        result = []
        path = []
        def dfs(index):

            if index == len(s):
                result.append(" ".join(path.copy()))
                return

            for i in range(index, len(s)):

                word = s[index:i + 1]

                if word not in wordHashmap:
                    continue
                
                # Choose
                path.append(word)

                # Explore
                dfs(i + 1)

                # Restore
                path.pop()

            return

        dfs(0)
        return result

if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    sol = Solution()
    result =sol.wordBreak(s, wordDict)