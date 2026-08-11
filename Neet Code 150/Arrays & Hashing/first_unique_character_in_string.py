'''
Given a string s
find the first non repeating hcaracter in it and return
its index
If it does not exist, return -1


'''



class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {} # key = 'string' and value = 'frequency
        for index, value in enumerate(s):
            if value in hashmap:
                hashmap[value] += 1 # increasing the frequency
            else:
                hashmap[value] = 1
        
        for index, value in enumerate(s):
            if hashmap[value] == 1:
                return index
        return -1

def main():
    print()
    s1 = 'leetcode' #0
    s2 = 'loveleetcode' #2
    s3 = 'aabb' # -1

    test_case_one = Solution()
    print(test_case_one.firstUniqChar(s2))

if __name__ == '__main__':
    main()
