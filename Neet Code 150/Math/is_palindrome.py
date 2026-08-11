class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        # Edge Case, empty and len(1)
        if len(x) in (0,1):
            return True
        
        # Utilize the 2 pointer approach
        l, r = 0, len(x) - 1 
        while l <= r:
            if x[l] != x[r]:
                # Found Palindrome
                return False
            l += 1
            r -= 1
        return True

def main():
    x = 121
    result = Solution()
    print(result.isPalindrome(x))

if __name__ == "__main__":
    main()