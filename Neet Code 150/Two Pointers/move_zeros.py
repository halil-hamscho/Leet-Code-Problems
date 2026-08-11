"""
Given an integer array nums, 
move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Okay so since we want to do this in place, what I am thinking of doing
is utilizing indices to do this in place

basically, I will keep a pointer initially at the end of the array

1. lets implement the solution with an extra array


This is basically a stack, where we are not creating a new data structure but if we 
pop something we simpyl just add it back
"""

class Solution:
    def moveZeroes(self, nums):
# using a two pointer approach to partition
        l = 0
        for r in range(len(nums)):
            if nums[r]: # if not 0
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        return nums

def main():
    result = Solution()
    nums = [0,1,0,3,12]
    print(result.moveZeroes(nums))

if __name__ == "__main__":
    main()



        