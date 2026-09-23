from typing import List;

"""
First Solution was just simply using two for loops 
for index, number in enumerate(nums):
            ans.append(number)

The answer here was Modulo

Modulo takes an ever increasing number and wraps it into a fixed range

so for example

% 3
0 % 3 = 0
1 % 3 = 1
2 % 3 = 2
3 % 3 = 0
4 % 3 = 1

x % length
x is the len(ans) so 
0, 1, 2, 3, ...

we essentially use the modulo to wrap around

x % length produces 0 through length - 1, so length = 3 
is 0, 1, 2

the 3rd way to solve it would be
nums + nums in the pythonic way, under the hood it is just a for loop

or literally nums * 2 which creates an original list just twice 
"""

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []
        length = len(nums)

        while len(ans) < 2 * length:
            index = len(ans) % length
            ans.append(nums[index])

        return ans

if __name__ == "__main__":
    nums = [1,2,1]
    output = [1,2,1,1,2,1]
    result = Solution().getConcatenation(nums)
    if result != output:
        print("Wrong result")
        print(f"Output: {output} Result: {result}")
    else:
        print("good job")
        print(f"Output: {output} Result: {result}")


