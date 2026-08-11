'''
Two Sum II the input array is sorted

Given a 1-indexed array of integers numbers that is already
sorted in non-decreasing order (increasing), find two numbers
such that they add up to a specific target number
Let these two numbers be
numbers[index1] and numbers[index2] where 1<= index1 < index2 <= numbers.length

return the indices of the two numbers, index1 and index 2
added by one as an integer array [index1,index2] of length 2

The test are generated such that there is only one solution
You may not use the same elemnt twice
Your solution must also use only constant extra space

'''





class Solution:
    def twoSum(self, numbers, target):
        # this solution works but uses extra memory space O(n)
        # hashmap = {} # value : index

        # for index, value in enumerate(numbers):
        #     result = target - value
        #     if result in hashmap:
        #         return [hashmap[result] + 1, index + 1]
        #     else:
        #         hashmap[value] = index

        # we will use a two pointer approach
        # add a left and right pointer and depending if
        # it is <, > or == then we will move the L or R pointer
        left_p = 0
        right_p = len(numbers) - 1
        while left_p < right_p: # use a while loop for pointers
            result = numbers[left_p] + numbers[right_p]
            if  result > target:
                right_p -= 1
            if result < target:
                left_p += 1
            if result == target:
                # the pointers are the indices
                return [left_p + 1, right_p + 1]

def main():
    print()
    numbers = [2,7,11,15] 
    target = 9
    test = Solution()
    print(test.twoSum(numbers, target))

if __name__ == '__main__':
    main()