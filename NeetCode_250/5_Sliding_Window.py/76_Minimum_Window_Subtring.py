"""
Recognition:
- Minimum contiguous window satisfying frequency requirements
- this usually means variable size slidign window with counts and validity tracker

Time: O(len(s) + len(t))
Space: O(len(t))


Remmember:
length: r - l + 1
defaultdict(int)

Structure:
expand right until valid
while valid:
    record the best window
    shrink left

t hashmap says what we need
current hashmap says what the window currentl has

when current[c] reaches t[c]:
    one requirement becomes satisfied
    have += 11

when have == need:
    the entire window is valid
"""



from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_hashmap = defaultdict(int)

        for letter in t:
            t_hashmap[letter] += 1

        current = defaultdict(int)
        have = 0
        need = len(t_hashmap)
        
        l = 0
        best = (0,0)
        best_length = float("inf")
        for r, letter in enumerate(s):

            if letter in t_hashmap:

                current[letter] += 1

            if letter in t_hashmap and current[letter] == t_hashmap[letter]:
                have += 1

            while have >= need:

                current_length = r - l + 1

                if current_length < best_length:
                    best_length = current_length
                    best = (l, r)

                removed = s[l]

                if removed in t_hashmap:

                    current[removed] -= 1

                    if current[removed] < t_hashmap[removed]:
                        have -= 1
        
                l += 1

        return s[best[0] : best[1] + 1] if best_length != float("inf") else ""

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    result = Solution().minWindow(s, t)