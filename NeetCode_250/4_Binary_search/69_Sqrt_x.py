"""
Intuition here is

mid * mid = x

sqrt(x) = y or y^2 = x or y * y = x

so we just need to find the smallest integer <= x

"""
class Solution:
    def mySqrt(self, x: int) -> int:

        l = 0
        r = x

        while l <= r:

            mid = (l + r) // 2

            if mid * mid == x:
                return mid

            elif mid * mid < x:
                l = mid + 1

            else:
                r = mid - 1

        # l > r
        return l - 1

if __name__ == "__main__":
    result = Solution().mySqrt(8)