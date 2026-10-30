"""

Component:
Trie -> Discover valid word matches
DFS -> Evaluates the remaining substring
Dynamic Programming -> Selects the optimal result
Memoization -> Prevents repeated calculations

Trie traversal is iterative because each string character determines exactly which child to visit

The DP is recursive because we explore different ways of processing the remaining string


Let:
n = length of s
L = maximum dictionary word length
D = total number of characters across dictionary words

Time:

Trie Construction: O(D)
DP states: O(n)
Trie traversal per state: O(min(n, L))

Therefore:
O(D + n * min(n, L))

Space:
Trie: O(D)
Memoization: O(n)
Recursion Stack: O(n)

O(D + n)


Base Case:
- when is the problem already solved?

Optimization:
- how do I combine the possibilities?

Memoization:
- What results can I reuse


Python Concepts:

from functools import cache
@cache
def dfs(i):
    ...

@cache is a decorator that wraps the function 

Iterating from an index
for j in range(i, len(s)):
- allows us to examine all possibel dictionary words beginnign at index i

Lessons:

- 1. DP does not require a global tally
instead of accumulating extra characters using nonlocal, we define what each recursive call returns

dfs(i) -> minimum extra characters from index i onward

2. A DP problem can have more than two choices
At any index, we can skip the current character or match any dictionary word beginning there
3. Recursion and iteration can work together
- iterative Trie traversal inside recursive DP

learn to define dfs(i) as the optimal answer for the remaining input rather than trying to maintain a global running total
"""
from typing import List
from functools import cache


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        trie = Trie()
        for word in dictionary:
            trie.addWord(word)

        memo = {}

        @cache
        # dfs(i) returns the minimum number of extra characters in s[i:]
        def dfs(i):

            if i in memo:
                return memo[i]
            
            if i == len(s):
                return 0

            # 1. Treat curr char as extra, i + 1
            extra = 1 + dfs(i + 1)

            # 2. Match a completed dict word and continue immediately after that word
            node = trie.root

            for j in range(i, len(s)):
                char = s[j]

                if char not in node.children:
                    break

                node = node.children[char]

                if node.is_end:
                    extra = min(extra, dfs(j + 1))

            memo[i] = extra
            return extra

        return dfs(0)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True
        
if __name__ == "__main__":
    sol = Solution()
    s = "leetscode"
    dictionary = ["leet","code","leetcode"]
    result = sol.minExtraChar(s, dictionary)
    print(result)