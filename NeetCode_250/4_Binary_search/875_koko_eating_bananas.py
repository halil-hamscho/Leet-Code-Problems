"""

binary search through k speeds, not searching an array

- find the minimum value that satisfies a condition

if hours > h: # k is too small
    l = k + 1
else:
    r = k - 1
    result = k
"""

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l = 1
        r = max(piles)
        result = r
        while l <= r:

            k = (l + r) // 2

            hours = 0
            for p in piles:

                hours += math.ceil((p / k))

                if hours > h:
                    break

            if hours > h:
                l = k + 1
            else:
                result = min(result, k)
                r = k - 1
                

        return result


if __name__ == "__main__":
    piles = [30,11,23,4,20]
    h = 6
    result = Solution().minEatingSpeed(piles, h)