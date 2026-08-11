'''
A phrase is a palindrome if,
after converting all uppercase letters
into lower case letters and removing all non-alphanumeric
characters, it reads the same forward and backward.
Alphanumeric characteristics include letters and numbers


Given a string s, return true if it is a palindrome
or false otherwise


Brainstorming:
- remove everything that is not ascii
- left pointer starts at the beginning
- right starts at the end
they move towards the middle

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: # empty string is always a palindrome
            return True

        # string with only lower case (take care of one edge case)
        new_string = ''
        for index, value in enumerate(s):
            if value.isalnum():
                new_string += value.lower()
        left_pointer = 0
        right_pointer = len(new_string) - 1

        while left_pointer < right_pointer:
            if new_string[left_pointer] != new_string[right_pointer]:
                return False
            left_pointer += 1
            right_pointer -= 1
        return True
def main():
    print()
    s = "A man, a plan, a canal: Panama"
    test = Solution()
    print(test.isPalindrome(s))

if __name__ == "__main__":
    main()



        # while left_pointer < (len(new_string)//2):
        #     if new_string[left_pointer] == new_string[right_pointer]:
        #         continue
        #     if not new_string[left_pointer].isalnum():
        #         left_pointer += 1
        #     if not new_string[right_pointer].isalnum():
        #         right_pointer += 1
            