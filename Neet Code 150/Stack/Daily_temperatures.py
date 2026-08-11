'''
Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to 
wait after the ith day to get a warmer temperature. If there 
is no future day for which this is possible, keep answer[i] == 0 instead.
'''


class Solution:
    def dailyTemperatures(self, temperatures):
        stack = [] # this will keep track of our temp pair [temp, index]
        result = [0] * len(temperatures) # default answers

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = (index - stack_index) # at the output, we want how many positions
            stack.append([temperature, index])
        return result

def main():
    print()
    test = Solution()
    temperatures = [30,40,50,60]
    print(test.dailyTemperatures(temperatures))

if __name__ == "__main__":
    main()
