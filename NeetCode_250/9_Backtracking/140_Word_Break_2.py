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