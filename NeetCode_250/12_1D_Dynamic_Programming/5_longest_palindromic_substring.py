"""
a larger substring is a palindrome if its inner substring is:
    - a palindrome
    - 2 outer characters match

Time: O(n^2)
Space: O(n) aux O(1), output O(n)

Intuition:
- every palindrome must have a center and every larger palindrome contains a smaller palindrome within it

2 Types of Palindromes
    - odd len
    - even len

Expand Around Center:
    - inner string is already a palindrome and matching outer characters preserve that property
"""

class Solution:

    def longestPalindrome(self, s: str) -> str:

        bestL, bestR = 0, 0
        for i in range(len(s)):
            
            oddL, oddR = self.helper(i, i, s)
            if oddR - oddL > bestR - bestL:
                bestL, bestR = oddL, oddR

            evenL, evenR = self.helper(i, i + 1, s)
            if evenR - evenL > bestR - bestL:
                bestL, bestR = evenL, evenR

        return s[bestL : bestR + 1]

    def helper(self, l, r, s):
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            r += 1
            l -= 1

        return l + 1, r - 1

    def longestPalindromeExample(self, s: str) -> str:

        length = 0
        for i in range(len(s)):
           length = max(length, self.helper(i, i, s))

           length = max(length, self.helper(i, i + 1, s))

        return length

    # def helper(self, l, r, s):
    #     max_length = 0
    #     while l >= 0 and r < len(s) and s[l] == s[r]:
    #         if (r - l + 1) > max_length:
    #             max_length = (r - l + 1)

    #         l -= 1
    #         r += 1

    #     return max_length

if __name__ == "__main__":
    sol = Solution()
    result = sol.longestPalindrome(s = "babad")

        