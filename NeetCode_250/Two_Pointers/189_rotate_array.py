"""

Intuition here is that when we reverse the array, we aleady have it in order
"""


class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k % len(nums)
        
        left = 0
        right = len(nums) - 1

        self.reverse(nums, left, right) # reverse entire array

        self.reverse(nums, 0, k - 1)

        self.reverse(nums, k, right)

    def reverse(self, nums, left, right):

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1





if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7]
    k = 3
    result = Solution().rotate(nums, k)