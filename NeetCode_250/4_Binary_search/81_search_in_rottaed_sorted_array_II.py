"""
Similar to Rotated Sorted Array Part 1
- nums[l] <= nums[m] tells you which half is sorted
 with duplicates however, we need to evaluate boundary values as well
 since duplicatges can make the two halves visually indistiguishable

- Rotated Array means identify the sorted half.
Rotated Array with duplicates means first ask whether duplicates
are hiding which half is sorted

"""


class Solution:
    def search(self, nums: list[int], target: int) -> bool:


        l = 0
        r = len(nums) - 1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                return True

            if nums[l] <= nums[m]: # left side is sorted

                if nums[l] == nums[m]:
                    l += 1
                    continue

                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                # right side is sorted

                if nums[r] == nums[m]:
                    r -= 1
                    continue 

                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return False


        
if __name__ == "__main__":
    nums = [1, 0, 1, 1, 1]
    target = 0
    result = Solution().search(nums, target)