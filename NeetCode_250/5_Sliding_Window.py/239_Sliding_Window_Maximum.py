
"""

Brute Force Solution
O(n - k + 1)
result = []

r = 0
while r <= len(nums) - k:

    temp = nums[r]
    for i in range(k):
        temp = max(temp, nums[r + i])

    result.append(temp)
    r += 1

return result

Optimized Solution:

With Deque
- remove expired indices (front)
- remove smaller candidates (back)


Frequency map tracks quantities, while a monotonic deque
tracks useful candidates in an order that lets us access the maximum
efficiently

We don't need to remember every element. We only need to preserve
candidates that could become the maximum later

Fixed Window + maximum/minimum + elements expiring -> Monotonic Deque

Front Handles Expiration
Back Handles maintainign monotonic order

Monotonic Stack is commonly used to find the next greater or smaller element

Time: O(n) since elements can only be added and removed from the deque once
Space: O(k) since deque contains at most k elements

"""
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:

        dq = deque() # we are storing tuples(index, val)
        result = []

        r = 0
        while r < len(nums):

            while dq and dq[0][0] < r - k + 1:
                # remove expired candidates
                dq.popleft()

            while dq and dq[-1][1] < nums[r]:
                # remove smaller candidates
                dq.pop()

            dq.append((r, nums[r]))

            if r >= k - 1:
                result.append(dq[0][1])

            r += 1

        return result

if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = Solution().maxSlidingWindow(nums, k)