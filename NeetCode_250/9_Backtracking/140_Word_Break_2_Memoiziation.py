"""
With memoization, we are returning sub problems rather than constructing at the end in backtracking


Backtracking: Build the solution from the top down
- maintain a path representing decisions already made

The complete answer is assembled at the leaf

2. Memoization: Return solutions from smaller subproblems
Instead of maintaining a global path, each recursive call answers:
What are all the valid sentences I can construct from this index onward?

dfs(7) # ["dog"]
dfs(4) # ["and dog"]
dfs(3) # ["sand and dog"]
"""

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:

        wordSet = set(wordDict)
        memo = {}

        def dfs(index):

            if index == len(s):
                return [""]

            if index in memo:
                return memo[index]

            sentences = []

            for i in range(index, len(s)):

                word = s[index:i + 1]

                if word not in wordSet:
                    continue

                suffixes = dfs(i + 1)

                for suffix in suffixes:
                    # Construct a sentence using word and suffix
                    sentence = word + (" " + suffix if suffix else "")

                    # Append it to sentences
                    sentences.append(sentence)
            
            memo[index] = sentences
            return sentences

        return dfs(0)


if __name__ == "__main__":
    s = "catsanddog"
    wordDict = ["cat","cats","and","sand","dog"]
    sol = Solution()
    result =sol.wordBreak(s, wordDict)