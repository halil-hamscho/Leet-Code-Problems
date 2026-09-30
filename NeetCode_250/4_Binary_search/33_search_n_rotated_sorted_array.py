class Solution:
    def search(self, nums: list[int], target: int) -> int:

        l = 0
        r = len(nums) - 1

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid

            # Which half is sorted

            if nums[l] <= nums[mid]: 

                # left hand sorted
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                # right hand sorted
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 2
    result = Solution().search(nums, target)