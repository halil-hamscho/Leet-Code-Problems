class Solution:
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = [] # pair (index, value)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index # push back the index to the pervious value of the stack
            stack.append((start, h))
        # values that are still in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        return maxArea
