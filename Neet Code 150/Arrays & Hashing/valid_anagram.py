'''
Given two strings s and t, return True if t is an 
anagram of s and false otherwise

An anagram is a word or phrase formed by rearranging the letters 
of different word or phrase
typically using all the original letters exactly once
'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        for i,v in enumerate(s):
            if s[i] == t[i]:
                key = True
            else:
                return False # need to return early 
        return key
def main():
    print()
    test_one = Solution()
    s = 'aacc'
    t = 'ccac'
    result_one = test_one.isAnagram(s,t)
    print(result_one)


if __name__ == '__main__':
    main()