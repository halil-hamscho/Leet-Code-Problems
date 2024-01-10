'''
Given an integer array nums and an integer k, return 
the k most frequent elements.
You may return the answer in any order


Brainstom:
# - if it repeats then we return those?
# - the count for each number must be >= k

# - use a hashmap where key = number and value = 
# number of appearances
# - then compare the value to k and if it is >= then
# append to a list and return it

^^^ the logic was wrong
what it means by k most frequent is give the
2 most frequent numbers, not what repeats more than k
so then we have to
- we don't have to sort the entire thing, because
we only want the k value of elements

Steps (for heap):
1. count the max number of occurences
2. Pop k times from the max heap
- each pop takes log n
- heapify takes n
total run time O(klogn)

Steps for linear time (bucket sort):
bucket sort:
instead of having the usual key (number) = # of apperances
what we are going to do is

for every count of apperances, we will have a list
of values that have that count

Ex. [1,1,1,2,2,100]
i (count) = 0    1     2     3
values =       [100]  [2]   [1]

once we have taken every single input value
and added it to a list
then get the top K values that occur, most
frequenly

the most number


'''

class Solution:
    def topKFrequent(self, nums, k):
        hashmap = {} # count : values [list]
        sorted_list = [[] for i in range(len(nums) +1)]
        # create a hashmap with key (number) : value (# of appearences)
        for index, value in enumerate(nums):
            if value in hashmap:
                hashmap[value] += 1
            else:
                hashmap[value] = 1
        
        for number, count in hashmap.items():
            # [[]] list with lists that for each index (count)
            # describes a list for every number that has that count
            sorted_list[count].append(number)
        
        # go through discending order since we want k most frequent
        result = []
        for i in range(len(sorted_list) - 1, 0, -1):
            for n in sorted_list[i]: # iterate through the list of numbers with that count Ex. index 3 with a list of [1,4,5....]
                result.append(n)
                if len(result) == k: # once we have the k most frequent, return
                    return result # guranteed to return

def main():
    nums = [1,1,1,2,2,3,4,4,4,4,4,100,100,100,100,100]
    k = 2
    test_one = Solution()
    result = test_one.topKFrequent(nums,k)
    print(result)

if __name__ == '__main__':
    main()




