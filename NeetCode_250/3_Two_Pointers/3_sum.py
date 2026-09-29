class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        nums.sort()

        result = []
        for index, a in enumerate(nums):
        
             # a + l + r = 0
            l = index + 1
            r = len(nums) - 1

            if index > 0 and a == nums[index - 1]:
                continue

            while l < r:

                calculation = (a + nums[l] + nums[r])

                if calculation < 0: # increase it
                    l += 1
                    continue

                if calculation > 0: # lower it
                    r -= 1
                    continue

                if calculation == 0:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return result

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    result = Solution().threeSum(nums)