'''
Given an integer array nums representing the amount of money of each house
return the macimum amount of money you can rob tonight
You cannot rob two adjacent houses
'''

class Solution:
    def rob(self, nums) -> int:

        def f(index, nums, dp):
            if index == 0:
                return nums[index]
            if index < 0:
                return 0
            if (dp[index] != -1):
                return dp[index]
            
            pick = nums[index] + f(index - 2, nums, dp)
            nopick = 0 + f(index - 1, nums, dp)
            dp[index] = max(pick, nopick)
            return 

        