# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:


        l = 0
        h = n

        while l <= h:

            m = (l + h) // 2

            g = self.guess(m)

            if g == -1:
                # higher
                h = m - 1
            elif g == 1:
                # lower
                l = m + 1
            else:
                return g

    def guess(self, number: int) -> int:
        pick = 6
        if number > pick:
            return -1
        elif number < pick:
            return 1
        else:
            return 0 

if __name__ == "__main__":
    result = Solution().guessNumber(10)