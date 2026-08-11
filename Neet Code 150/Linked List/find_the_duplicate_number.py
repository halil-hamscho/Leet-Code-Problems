'''
Two things about this problem
1. Notice that it is a Linked List problem
     then numbers are pointers (there will be a repeating cycle)
2. Use floyds algorithm(turtoise and hare)

Linear Time Solution
Constant Time

- Cycle detection
'''

class Solution:
    def findDuplicate(self, nums) -> int:
        # first part of the algorithm
        slow, fast = 0,0 # 0 is not part of the cycle
        while True: # go until they intercept
            slow = nums[slow]
            fast = nums[nums[fast]] # advance by 2
            if slow == fast: # found the first intercept
                break

        # Create a second slow pointer
        # Phase 2 of the algorithm
        slow_2 = 0
        while True:
            slow = nums[slow]
            slow_2 = nums[slow_2]
            if slow == slow_2:
                return slow
