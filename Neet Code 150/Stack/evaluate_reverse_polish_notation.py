'''
Evaluate Reverse Polish Notation

You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer

Multiplication takes precedence
When you subtract ytou have to do b - a b is the first value Ex. a = 1 b = 2 in [2,1]

O(n) time complexity is just the length of the array
O(n) space complexity due to the stack

'''
class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = ['+','-','*','/']
        result = 0
        for index, value in enumerate(tokens):
            if value in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                if value == '+':
                    result = b + a
                elif value == '-':
                    result = b - a
                elif value == '*':
                    result = b * a
                elif value == "/":
                    result = int(b / a)
                stack.append(result)
            else:
                stack.append(int(value))
        return stack[0]
def main():
    print()
    test = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(test.evalRPN(tokens))


if __name__ == "__main__":
    main()