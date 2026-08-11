class Solution:
    def partition(self, s):
        res = []
        path = []

        def dfs(index):
            if index >= len(s):
                res.append(path.copy()) # will continue changin ghte path
                return
            for i in range(index, len(s)):
                # for every letter in the string
                if self.isPalindrome(s, index, i): # start at index and end at index i
                    path.append(s[index:i + 1]) # we do + 1 since if we just do index:i i is not included 
                    dfs(i + 1) # look for additional palindromes # next character
                    path.pop() # backtrack, clean up, remove the additional 

        dfs(0)
        return res
    
    def isPalindrome(self, s, start, end):
        l = start
        r = end
        while l < r:
            if (s[l] != s[r]):
                return False
            l += 1
            r -= 1
        return True

def main():
    s = "aab"
    res = Solution().partition(s)
    print(res)

if __name__ == "__main__":
    main()