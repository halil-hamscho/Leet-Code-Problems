'''
Given an array of strngs (strs), group the anagrams
together. You can return the answer in any order

An anagram is a word or phrase
formed by rearranging the letters of a different
word or phrase, typically using all the original letters
exactly once
My Brain storm:
we Utilize a hashmap, where in each tuple, the key is a sorted and joined and then
if the key matches the current value, then we append the value to the list

'''


class Solution:
    def groupAnagrams(self, strs):
        hashmap = {} # sorted key : list
        for index, value in enumerate(strs):
            key = ''.join(sorted(value))
            if key in hashmap:
                hashmap[key].append(value)
            else:
                hashmap[key] = [value] # initialize the list
        return list(hashmap.values()) # return a list, to remove dict_values([...])

def main():
    print()
    test_one = Solution()
    strs = ['eat','tea','tan','ate','nat','bat']
    result_one = test_one.groupAnagrams(strs)
    print(result_one)

if __name__ == '__main__':
    main()