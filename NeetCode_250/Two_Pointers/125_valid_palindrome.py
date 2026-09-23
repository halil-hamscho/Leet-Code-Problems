"""

s = s.lower() # uppercase to lowercase

# filter out non alphanumeric numbers 
temp = []
for char in s:
    if char.isalnum():
        temp.append(char)

temp = "".join(temp)

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:


        i = 0
        j = len(s) - 1
        while i < j:

            if not s[i].isalnum():
                i += 1
                continue

            if not s[j].isalnum():
                j -= 1
                continue

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
                
if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    result = Solution().isPalindrome(s)