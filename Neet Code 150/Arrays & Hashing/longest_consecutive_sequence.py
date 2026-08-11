'''
Given an unsorted array of integers nums, return the 
length of the longest consecutive elements sequence

YOU MUST write an algorithm that runs in O(n) time

consecutive elements: 0,1,2,3,4,5,6,7

Brainstorm:
- you need something that keeps counting +1 starting at 0

- you need a sorted hashmap?
- sort the array? and then compare?
- maybe use a set?



'''


class Solution:
    def longestConsecutive(self, nums) -> int:

        # Empty List
        if not nums: return 0

        # Sorting takes nlogn
        # Initialize a set to remove duplicates
        # In python, a set is implemented as a hash table
        # This causes us to expect to lookup/insert/delete in O(1) average
        numsSet = set(nums)
        longest_sequence = 0

    # set = 1 2 3 4 100 200
        for index, value in enumerate(numsSet):
            # check if it is the start of a sequence
            if (value - 1) not in numsSet: # it is a starting of a sequence # lookup O(1)
                length = 1
                # Now check how much longer it is
                while (value + length) in numsSet: # we can add by length as we are increasing by one
                    length += 1
                longest_sequence = max(longest_sequence,length)
        return longest_sequence

def main():
    print()
    nums = [9,1,4,7,3,-1,0,5,8,-1,6]
    test = Solution()
    print(test.longestConsecutive(nums))


if __name__ == '__main__':
    main()
