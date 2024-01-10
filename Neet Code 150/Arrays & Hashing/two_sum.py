'''
Given an array of integers nums and an integer target
return indices of two numbers such that
they add up to target

You may assume that each input would have one
solution, and may not use the same element twice

Brain storm
- Use linear search, where since there will only be
two integers, we simply traverse the list

- 

'''


def twoSum(nums, target):
    # First Method: Brute Force Approach 
    '''
    Time: O(n^2)
    for i in range(len(nums)):
    for j in range(i + 1 , len(nums)):
        if nums[j] == target - nums[i]:
            return [i , j]
    '''

    # Second Method, use binary search?, a dictionary? Use a HASHMAP or dictionary
    # Time = O(n) since it is a one pass 
    # Space = O(n) due to the hashmap possibly using all n memory for all the values in the array
    hashmap = {} # value : index
    for index, value in enumerate(nums): # using enumerate is much easier
        result = target - value
        if result in hashmap:
            #the reson why we return the hashmap[result] first is that, it is our first solution to the two sum
            # the second index is the second answer
            return [hashmap[result], index]
        else:
            hashmap[value] = index

def main():
    print()
    nums = [2,7,11,15]
    target = 9
    result = twoSum(nums,target)
    print(result)

if __name__ == '__main__':
    main()