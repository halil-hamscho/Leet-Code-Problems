'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

Conditions:
nums[m] >= nums[L]
    search right
else
    serach left

'''

class Solution:
    def findMin(self, nums) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] < nums[r]: # sorted
                result = min(result, nums[l])
                break
            m = (l + r ) // 2
            result = min(result, nums[m])
            # Search Left or Right
            if nums[m] >= nums[l]:
                # Search right
                l = m + 1
            else:
                # Search Left
                r = m - 1
        return result
    
def main():
   print()
   test = Solution()
   nums = [3,4,5,1,2]
   result = test.findMin(nums)
   print(result)


if __name__ == '__main__':
    main()