'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.


This algorithm will be binary search
the way it works is that
you continue splitting up and checking if it is there
'''


class Solution:
    def search(self, nums, target) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            # we might encounter an overflow if the values are close to the 2^32 bit total
            # if they ask
            # left pointer + ((r - l) // 2)
            mid_point = (l + r) // 2
            if nums[mid_point] < target:
                l = mid_point + 1
            elif nums[mid_point] > target:
                r = mid_point - 1
            else: # when it equals the target
                return mid_point
        return -1      

def main():
    print()
    test = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(test.search(nums, target))

if __name__ == '__main__':
    main()