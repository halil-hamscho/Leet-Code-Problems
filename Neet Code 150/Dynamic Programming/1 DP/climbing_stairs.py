"""
Approach 1. fibonacci sequence solution (recursion)
def steps(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    return steps(n - 1) + steps(n - 2)

Approach 2. Using Memoization (cache)
        cache = {
            0:0,
            1:1,
            2:2
        }
        total = 0
        def steps(n):
            if n not in cache:
                cache[n] = steps(n - 1) + steps(n - 2)
            return cache[n]
        total += steps(n)
        return total 

Approach 3/4. Using a true dynamic approach
Two Variables: prev and curr. 
initilzie prev and curr to 1 since base case 0 and 1 steps
In each iteration, update prev and curr by shifting their values. 
Curr becomes the sum of the previous two values and prev stores the previous value of curr


Neetcode Solution:
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one
"""

class Solution:
    def climbStairs(self, n) -> int:
        # n = number of stairs
        # either 1 step or 2 steps
        # total = steps(x - 1) + steps(x - 2)
        if n == 0 or n == 1:
            return 1
        prev, curr = 1, 1
        for i in range(2, n + 1):
            temp = curr
            curr = prev + curr
            prev = temp
        return curr
            

def main():
    result = Solution()
    print(result.climbStairs(4))

if __name__ == "__main__":
    main()
            