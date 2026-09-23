"""

Pattern: Monotonic Stack -> Stack keeps unresolved temperatures in decreasing order. A new warmer temperature resolves every colder temperature sitting on top of the stack

Time: O(n)
- have nested while, however no O(n^2) since each inded can enter the stack once and leave the stack once

Space: O(n)
stack can hold n entries at worse case

Recognition Rule:
You are looking for the next future element that satisfies a comparison, and unresolved elements can wait until something later resolves them

Python Concept:
- Store (temp, index) tuples and unpack them

"For each element, find the next element to the right that is greater -> monotonic stack

"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:

        result = [0] * len(temperatures)

        stack = []

        for index, temperature in enumerate(temperatures):

            while stack and stack[-1][0] < temperature:

                i = stack[-1][1]

                result[i] = index - i

                stack.pop()

            stack.append((temperature, index))

        return result
    
if __name__ == "__main__":
    temperatures = [73,74,75,71,69,72,76,73]
    result = Solution().dailyTemperatures(temperatures)
    if temperatures != [1,1,4,2,1,1,0,0]:
        print("bad")