'''
Given n non-negative integers representing an elevation map
where the width of each bar is 1, compute how muc water it can trap after
raining


my thoughts:
- need two points
- one for the left of the current block
- one for the right of the current block
- we compare the heights to get the minimum of the left and right
the min gives us the solution to know how much water can be stored


Edge Cases:
- if the left is less than current
Ex. Left = 1 current = 2 max = 3, min of left,right min(1,3) = 1
1 - 2 = - 1, we cannot trap negative water
min(height) - current(height)

'''


class Solution:
    def trap(self, height) -> int:
        # Edge Case if the height is 0
        if not height: return 0
        # Initialize Pointers
        left_pointer, right_pointer = 0, len(height) - 1
        #Initialize the maxes
        left_max, right_max = height[left_pointer], height[right_pointer]
        result = 0 # total the water

        while left_pointer < right_pointer:
            # compare the maxes
            if left_max < right_max:
                left_pointer += 1
                left_max = max(left_max, height[left_pointer])
                result += left_max - height[left_pointer]
            else:
                right_pointer -= 1
                right_max = max(right_max, height[right_pointer])
                result += right_max - height[right_pointer]

        return result
    
def main():
    print()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    test_case = Solution()
    print(test_case.trap(height))


if __name__ == '__main__':
    main()

