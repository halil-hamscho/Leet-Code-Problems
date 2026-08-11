'''
Container with Most Water

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line
are i,0 and i, height[i]

Find two lines that together with the x-axis form a container, such that
the container contains the most water

Retuen the maximum amount of water a container can store

BrainStorm:
- start left = 0 right = n - 1
- each loop check if the area if biger

The trick here is keeping track of the max area
# also do where you compare the left and the right pointers
and whichever one is the lowest you move it
 
    Brute Force O(n^2)
    area = 0
    for l in range(len(height)):
        for r in range(l+1, len(height)):
            area = r - l * min(height[l],height[r])
            res = max(res, area)
            ^ every time it is a new max, it updates it
    return res    
'''

class Solution:
    def maxArea(self, height) -> int:
    
        left_p = 0
        right_p = len(height) - 1
        # Initial Max
        result = 0

        # Linear Time Solution
        while left_p < right_p:
            # The way we will update the pointer is which has the least height will move
            temp_area = (right_p - left_p) * min(height[right_p], height[left_p])
            result = max(result,temp_area)
            if height[left_p] < height[right_p]:
                left_p += 1
            elif height[left_p] > height[right_p]:
                right_p -= 1
            else: # if they are equal, just move the left
                left_p += 1
        return result

def main():
    print()
    height = [1,1]
    test = Solution()
    print(test.maxArea(height))

if __name__ == '__main__':
    main()
