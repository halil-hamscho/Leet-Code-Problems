"""
Binary Search with insertion

if we never find target, l > r:
invariant is that, everything to the left is strictly smaller than target
so we can insert at index l

Edge case nums = [1,3,5,6] t = 0
r shrinks until it reaches r = mid - 1 where mid = 0 so r = -1
l stays at the startng position

"""

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l 

        

if __name__ == "__main__":
    nums = [1,3,5,6] 
    target = 7
    result = Solution().searchInsert(nums, target)