"""
Pattern: Binary Search on a partially ordered structure

Invariant: minimum remains between [l, r]

r serves as the anchor

if nums[m] > nums[r]:
    move l = mid + 1

if nums[m] < nums[r]:
    move r = mid, since mid can still be a valid number
"""
class Solution:
    def findMin(self, nums: list[int]) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            if l == r:
                break

            m = (l + r) // 2

            if nums[m] > nums[r]: # 5 > 1
                # answer is between mid + 1 to r
                l = m + 1
            else:
                # less than r
                r = m

        return nums[l]


if __name__ == "__main__":
    nums = [3,4,5,1,2]
    result = Solution().findMin(nums)