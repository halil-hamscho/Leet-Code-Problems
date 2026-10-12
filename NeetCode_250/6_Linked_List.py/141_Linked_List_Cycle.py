"""
Floyds Detection Algorithm

Time: O(n) where n is the number of distinct nodes
O(L) = slow pointer n until entering cycle
O(C) = nodes in the cycle
O(L + C) = O(n)

With speeds 1 and 2, once we enter the cycle
Since the pointer gains one position per iteration
closing a gap of d positions requires at most d iterations

Python Concepts:
if fast is slow:
- is to compare node identity, not value

while fast and fast.next
- we need to gurantee fast.next since
3 -> None
^
fast

fast.next = None
fast.next.next = ERROR
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        slow = head
        fast = head.next
        
        while fast and fast.next:

            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next

        return False


if __name__ == "__main__":

    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2


    result = Solution().hasCycle(node1)