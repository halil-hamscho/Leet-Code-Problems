class Solution:
    def validPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1

        while i < j:

            if s[i] != s[j]:

                l = self.is_palindrome(s, i + 1, j)
                r = self.is_palindrome(s, i, j - 1)

                if l or r:
                    return True
                
                return False

            i += 1
            j -= 1

        return True
        


    def is_palindrome(self, s: str, left:int, right:int):

        while left < right:

            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
        
            

if __name__ == "__main__":
    s = "ebcbbececabbacecbbcbe"
    result = Solution().validPalindrome(s)