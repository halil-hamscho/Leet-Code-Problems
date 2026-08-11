'''
Brute Force: Consider every possible subarray within the given array and count the number of zeros and onces in each subarray

1. Maintain count variables for one and zero as you iterate through the array
2. Maintain a hashmap in which you store the leftmost index for each count value
3. As you iterate through the array, if the count equals, longest subarray we have seen
    else
PREFIX problem
'''

class Solution:
    def findMaxLength(self, nums):
        # will use a hashmap to map diff to index, and then once count = 1 - 0 -> 0
        zero, one = 0, 0
        result = 0
        # diff = count[1's] - count[0's]
        diff_index = {} # diff : ending index
        for index, num in enumerate(nums):
            if num == 0:
                zero += 1
            else: # num == 1
                one += 1
            # add diff in hashmap 
            if one - zero not in diff_index:
                diff_index[one - zero] = index
            # Two Cases
            if one == zero:
                result = one + zero # Longest Sub Array we have seen yet
            else:
                idx = diff_index[one - zero]
                result = max(result, index - idx)
        return result

def main():
    result = Solution()
    print(result.findMaxLength([0,1,0,0,0,0,1]))

if __name__ == "__main__":
    main()
