'''
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations 
of well-formed parentheses.


Brainstorm:
We need to generate all combinations of well formed parentheses

we are going to utilize backtracking with three specific rules
- only add open parenthesis if open < n
- only add a closing parenthesis if closed < open
- valid if open == closed == n

The key for this problem is that we call the function and so
after completing the entire recursion call, it pops all the way back
to the starter ( and does the other combinations
'''
class Solution:
    def generateParenthesis(self, n):
        # best way to do it us to do it recursively

        # Global pariable
        stack = []
        result = []
        # Break the function into three conditions
        def backtrack(openN, closedN):
            if openN == closedN == n:
                # our stack is finished
                # join every character in the stack
                result.append(''.join(stack))
                return
            # if we want to add an open parenthesis:
            if openN < n:
                stack.append('(')
                backtrack(openN+1, closedN)
                # after the backtrack returns
                stack.pop()

            # if we want to add a closing parenthesis
            if closedN < openN:
                stack.append(')')
                backtrack(openN, closedN+1)
                stack.pop()
        # call the backtrack function
        backtrack(0,0)
        return result

def main():
    print()
    test = Solution()
    n = 3
    print(test.generateParenthesis(n))


if __name__ == "__main__":
    main()