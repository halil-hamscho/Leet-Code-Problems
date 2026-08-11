'''
Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]]
such that 
i != j and i !=k
j != k
nums[i] + nums[j] + nums[k] == 0

Brainstorm:
- two pointer
- if we fix an x, then we have a two sum problem at hand
- we need to initialize a one pass hashmap
- iterate through an array and check if the target - val is there
- return indices
'''


class Solution:
    def threeSum(self, nums):
        result = []
        nums.sort()

        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue # we don't want the same value twice
                # two pointer solution
            left_p, right_p = index + 1, len(nums) - 1
            # While Loop Utilization for pointers
            while left_p < right_p:
                threeSum = value + nums[left_p] + nums[right_p]
                if threeSum > 0:
                    right_p -= 1
                elif threeSum < 0:
                    left_p += 1
                else:
                    result.append([value, nums[left_p], nums[right_p]])
# now that we have appended we want to now move to the left and see
# if there is any same numbers in order to skip them,
# the right pointer will take care of itself
                    left_p += 1
                    while nums[left_p] == nums[left_p - 1] and left_p < right_p:
                        left_p += 1
        return result

def main():
    print()
    nums = [-1,0,1,2,-1,-4]
    test = Solution()
    print(test.threeSum(nums))

if __name__ == '__main__':
    main()
