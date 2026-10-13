"""
Two Pointer Floyds Cycle Detection

Phase 1:
- Find meeting point

Phase 2:
- reset slow pointer and move fast & slow one at a time

Because the fast pointer moves twice as quickly , the first meeting
creates a mathematical relationship between distance to the cycle
entrance and the remaining distance around the cycle.

The thing is that, when we find the meeting point, that doesn't gurantee that
that is the duplicate value

Example:

nums = [3, 1, 3, 4, 2]

Cycle:
0 -> 3 -> 4 -> 2
     ^         |
     --------  |

- Meet at 2
- Duplicate is 3

Pigeonhole principle: More elemtns than possibel distinct values gurantees duplication
Two Phases:
- First detect cycle, then locate its entrace

Lesson: 

- Cycle Detection: think fast and slow pointers
- Array as linked list: When values represent valid indices, consider treating nums[i] as a pointer
"""

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        slow = 0
        fast = 0

        # Phase 1 detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2, reset slow and move 1 at a time
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return nums[slow]

if __name__ == "__main__":
    nums = [3,1,3,4,2]
    result = Solution().findDuplicate(nums)
    print(result)
