"""

Observation: len(s1) determines a fixed window size in s2

Mental Model
    - Right pointer expands first
    - Left pointer repairs the window afterward

Because the target size is fixed, r adds exactly one character and l removes exactly 
one when necessary

Pattern: Fixed size sliding window plus frequency counts

Invariant: window always represents s2[l: r + 1]

Time: O(n) where n = len(s2), comparing maps is O(1) here because there are only
26 lowercase letters

Space: O(1) because each frequency map has at most 26 entries

Recognition: Fixed length contiguous substring plus comparing character frequncies usually
suggests fixed sliding window


"""

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        counter = defaultdict(int) # letter : count
        for s in s1:
            counter[s] += 1

        l = 0
        temp = defaultdict(int)
        for r in range(len(s2)):

            temp[s2[r]] += 1

            if r - l + 1 > len(s1):
                temp[s2[l]] -= 1

                if temp[s2[l]] <= 0:
                    del temp[s2[l]]

                l += 1

            if temp == counter:
                return True

        return False
    
if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    result = Solution().checkInclusion(s1, s2)