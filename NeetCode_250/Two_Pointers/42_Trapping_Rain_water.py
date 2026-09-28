"""

Space O(n) Solution
- Build Left Max Array
- Build Right Max Array
- Reverse Right
- for every index min(l[i], r[i]) - height[i]

Space O(1) Solution
- 4 pointers
- l, r, left_max, right_max
- use two pointers, left_max, right_max, always process the side
with the smaller maximum because that boundary determines the water there, giving O(n) and O(1) space


"""

class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        left_max, right_max = 0,0 

        result = 0
        while l <= r:

            if left_max < right_max:
                left_max = max(left_max, height[l])
                result += left_max - height[l]
                l += 1

            else:
                right_max = max(right_max, height[r])
                result += right_max - height[r]
                r -= 1

        return result

if __name__ == "__main__":
    input = [4,2,0,3,2,5]
    result = Solution().trap(input)