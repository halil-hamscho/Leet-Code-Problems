"""

A transformation sequence from word beginWord to word endWord 

using a dictionary wordList is a sequence such that

beginWord -> s1 -> s2 -> ... -> sk

- shortest transformation sequence -> BFS?

each index of the word is a position technicallly

can we compile a list of letters?

can I do something like

okay h i t positions
we populate a dic of positiions of letters right

^^^ These were all the right questions
- shortest -> BFS was correct
- index of char of a word is a position that we can check -> also correct 

This problem was similar to 752 Open the Lock
Pattern: Shortest Path Problem with no Explicit Graph (unweighted graph)

Recognition: minimum transformations between states

Invariant: the first time BFS discovers a word, it has found shortest path to it

- Each combination is a node, and changing one position is a potential neighbor 
- in word latter, each word is a node, and changing one character creates a potential neighbor

in Both Cases:
    1. each position can be modified indepdently
    2. modifying one position generates a candidate neighbor
    3. we check whether that neighbor is valid
    4. we use BFS because every transformation costs on estep
    5. we track visited states to avoid processing the same state repeatedly


Time Complexity: O(N * L^2)
- N be the number of words
- L be the length of each word

BFS visits at most N words, plus the starting word
For every word, we iterate throguh L positions, each position has at most 26 characters, constructing a new string takes O(L) time

- wordSet O(NL)
- hashmap O(NL)
- each candidate transformation requires O(L) time to construct (list(word) and "".join(word))
O(N x L x 26 x L)

Space: O(NL)
- wordSet: O(N) storing string references
- hashmap: O(L) storing L positions, each position at most 26 characters
- queue: O(N)
- visited: O(N)
- Generated Strings O(NL)

"""
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return 0

        hashmap = defaultdict(set) # position : char
        for word in wordList:
            for i in range(len(word)):
                hashmap[i].add(word[i])

        # Iterate through the letters?
        queue = deque([(beginWord, 1)])
        visited = set()
        while queue:
            word, count = queue.popleft()

            for i in range(len(word)):

                for option in hashmap[i]:
                    edit_word = list(word)

                    edit_word[i] = option
                    joined_word = "".join(edit_word)

                    if joined_word not in wordSet:
                        continue

                    if joined_word in visited:
                        continue

                    if joined_word == endWord:
                        return count + 1
                    
                    visited.add(joined_word)
                    queue.append((joined_word, count + 1))

        return 0

if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    sol = Solution()
    result = sol.ladderLength(beginWord, endWord, wordList)
    print(result)