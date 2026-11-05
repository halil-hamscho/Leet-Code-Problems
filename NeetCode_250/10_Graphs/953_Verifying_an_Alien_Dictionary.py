"""
- put the order in a hashmap to have O(1) loop up and put positional point as value

Takeway:
- when verifying a sequence is sorted, you only need to compare adjacent elements

Time: O(N * L)
N = number of words
L = max length of word

Space: O(1)
hashmap O(26)
"""


class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        hashmap = {} # letter:index
        for index, letter in enumerate(order):
            hashmap[letter] = index

        i = 0
        while i + 1 < len(words):
            a = words[i]
            b = words[i + 1]

            for j in range(len(a)):
                if j >= len(b):
                    return False
                elif hashmap[a[j]] > hashmap[b[j]]:
                    return False
                elif hashmap[a[j]] == hashmap[b[j]]:
                    continue
                elif hashmap[a[j]] < hashmap[b[j]]:
                    break

            i += 1

        return True
                        
if __name__ == "__main__":
    words = ["hello","leetcode"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    sol = Solution()
    result = sol.isAlienSorted(words, order)