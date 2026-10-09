"""
Binary Search to find Insertion Point

Recognition Heuristics:
- Sorted Array + Closests Values Around a target

Pattern: 
1. Search for Insertion where arr[i] <= x
2. Left = l - 1, Right = l
3. Repeat k times

Time: BS: O(log n) + O(k) since we do the loop k times
Space: O(1)

Lesson: Find the target's insertion boundary, then inspect outward from that boundary
"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        r = len(arr) - 1
        while l <= r:

            m = (l + r) // 2

            if arr[m] < x:
                l = m + 1
            else:
                r = m - 1

        # l is the first index where arr[l] >= x
        left = l - 1
        right = l

        while k > 0:

            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1

            k -= 1

        return arr[left + 1 : right]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    result = Solution().findClosestElements(arr, k, x)