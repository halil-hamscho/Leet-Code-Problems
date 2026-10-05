"""
Binary Search to find Insertion Point

"""

from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        l = 0
        r = len(arr) - 1
        starting_point = 0
        while l <= r:

            m = (l + r) // 2

            if arr[m] == x:
                starting_point = m
                break

            elif arr[m] < x:
                l = m + 1

            elif arr[m] > x:
                r = m - 1

        left = starting_point - 1
        right = starting_point

        while k > 0:

            k -= 1

            if left < 0:
                right += 1
                continue
            elif right > len(arr) - 1:
                left -= 1
                continue
                
            if abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1

            else:
                right += 1

        return arr[left : right + 1]

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    k = 4
    x = 3
    result = Solution().findClosestElements(arr, k, x)