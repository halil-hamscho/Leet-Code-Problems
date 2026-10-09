"""
Pattern: Sliding window with variable size and validity condition

Window Behavior: move r to expand, if replacements needed become greater than k, move l right
unitl the window is valid again

How do we know replacements have become greater than k?

window_size = r - l + 1
max_freq = mas(hashmap.values())

window_size - max_freq > k:
    decrement from hashmap[s[l]] -= 1
    move l right
"""

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        hashmap = defaultdict(int) # value : count
        l = 0
        result = 0

        for r in range(len(s)):

            hashmap[s[r]] += 1

            while (r - l + 1) - max(hashmap.values()) > k:
                # invalid
                hashmap[s[l]] -= 1
                l += 1

            # valid
            result = max(result, r - l + 1)

        return result            

if __name__ == "__main__":
    s = "AABABBA"
    k = 1    
    result = Solution().characterReplacement(s, k)