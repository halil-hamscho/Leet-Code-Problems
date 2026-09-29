"""
So this is what I am thinking,
- so we need sequential,
the thing that we can do that might take the longest is just 
1. check every letter at every index, and if it matches keep it going
sort of like a sliding window with all the strings in the array

but if I am understanding it correctly we are talking about a prefix here so should we only
care about the beginning of the strings?
Yes, examine one character position at a time across all strings


character loop
- word loop

We can either
- when any word runs out of characters, not necessarily the fird word
- use the shortest word as the limit
or use thefirst word as the limit

outer loop: s times
inner loop: n times
total comparisons: s x n

O(s) including the returned prefix, or O(a) auxiliary space because I am 
not creating any additional data structure that grows with the input

        prefix = ""

        smallest = min(strs, key=len) # O (n), also storing a reference
        # character index
        # each word
        # O (s x n)
        for i in range(len(smallest)):
            letter = smallest[i]
            for word in strs:
                if word[i] != letter:
                    return prefix
            prefix += letter
    
        return prefix

we do not actually have to build the prefix at all actually

smallest[:i], exclusive so takes everything before index i
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest = min(strs, key=len) # O (n), also storing a reference
        # character index
        # each word
        # O (s x n)
        for i in range(len(smallest)):
            letter = smallest[i]
            for word in strs:
                if word[i] != letter:
                    return smallest[:i]
        return smallest

if __name__ == "__main__":
    strs = ["flower","flow","flight"]
    output = "fl"
    result = Solution().longestCommonPrefix(strs)
    if result != output:
        print(f"bad")