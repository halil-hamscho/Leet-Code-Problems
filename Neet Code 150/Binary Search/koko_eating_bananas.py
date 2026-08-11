'''
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. 
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. 
Each hour, she chooses some pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, she eats all of them instead and will not eat any 
more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the 
bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

'''
import math

class Solution:
    def minEatingSpeed(self, piles, h: int) -> int: 
        l = 1
        r = max(piles) # max number in our piles
        result = r # Given answer of max pile of bananas per hour (fastest eating time)

        while l <= r:
            # Find the middle point
            k = (l + r) // 2 # Floor division
            hours = 0 # check this
            for p in piles:
                hours += math.ceil(p / k) # round up Ex. 3/6, 6/6, 7/6, 11/6 -> 1 + 1 + 2 + 2 = 6 hrs
            if hours <= h: # less than guard hours 
                result = min(result, k)
                r = k - 1 # search the left portion, update right pointer
            else:
                l = k + 1 # search the right portion
        return result
            
def main():
    print()
    
if __name__ == '__main__':
    main()