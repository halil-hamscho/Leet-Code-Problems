"""
Pattern: two pointers, opposite sides
Similar to Two Sum II where sorted array told us which pointer to move
in this case, start in the maximum width and after every height that is less, move it

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:

        result = min(height[0], height[1]) * 1

        if len(height) == 2:
            return result

        # left is our left side, r is our search
        l, r = 0, len(height) - 1
        while l < r:

            temp_r = min(height[l], height[r]) * (r - l)
            result = max(result, temp_r)

            if height[r] > height[l]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return result

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    result = Solution().maxArea(height)