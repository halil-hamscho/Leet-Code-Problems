"""
Pattern: Variable Size Sliding Window

In this case, we think so between r through l, how can we avoid
recomputing information from scratch

In this case, snce we want the summation, we can keep a current_sum variable

Movement: Expand r unitl valid, Once valid, shrink l as much as possible while recording 
the minimum length


Note here, we start the length in float("inf") and if it remains
after searching through the array, it means the full length of the array
never reached target

"""

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        current_sum = 0
        l = 0
        length = float("inf")
        for r, num in enumerate(nums):

            current_sum += num

            while current_sum >= target:

                length = min(length, r - l + 1)

                current_sum -= nums[l]

                l += 1

        if length == float("inf"):
            return 0

        return length

            

if __name__ == "__main__":

    target = 7
    nums = [2,3,1,2,4,3]
    result = Solution().minSubArrayLen(target, nums)