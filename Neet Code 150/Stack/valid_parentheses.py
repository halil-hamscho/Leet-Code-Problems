'''
Given a string s containing just the characters
() {} []
determine if the input string is valid.

An input string is valid if:
1. Open bracekts must be closed by the same type of brackets
2. Open brackets must be closed in the corect order
3. Every close bracket has a corresponding open bracket of the same type

BrainStorming:
- Using  a stack
What is a stack?
a stack is a linear data structure, LAST IN FIRST OUT

We have functions like, empty()
size()
top()/peek()
push(a)
pop(a)
LAST IN FIRST OUT


Answer:
we use a stack to append every opening character Ex. ( 
then when we reach a closing character Ex. )
if the value is a closing character (as a key in the hashmap)
we check if the stack is not empty and we check the last character of our stack
and if that last character matches the hashmap value, then we pop the ( and not append )

O(n) run time since we go through the array
O(n) space complexity since we are using a stack
'''


class Solution:
    def isValid(self, s: str) -> bool:
        # If it is odd, then you can't close
        if len(s) % 2 != 0:
            return False
        stack = []
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
            } # our three pairs
        for index, value in enumerate(s):
            if value in hashmap: # if the value is a closing character
                # make sure that our stack is not empty
                # stack[-1] is the last value
                if stack and stack[-1] == hashmap[value]:
                    # the last value would be the open character
                    stack.pop()
                else:
                    # if the stack is empty or don't match
                    return False
            else:
                stack.append(value)
        return True if not stack else False
def main():
    print()
    s = '[{()}]'
    test = Solution()
    print(test.isValid(s))

if __name__ == '__main__':
    main()
