class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result = [0] * len(temperatures)

        stack = []

        for index, temp in enumerate(temperatures):

            while stack and stack[-1][0] < temp:
                i = stack[-1][1]
                result[i] = index - i

                stack.pop()

            stack.append((temp, index))

        return result
