"""
Time Complexity: O(L)
Space: O(1)

Pattern: Two Pointers with a fixed gap
in 141 Linked List Cycle we needed to find a cycle
- Two Pointers with diff speeds

In this case, we want
- Two Pointers with a fixed gap

Lessons:
- Dummy Nodes simplify edge cases, especially removing head
- Reversing List works, but unecessarily modifies entire list
- To optimize operations, we do fixed gap 

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:

        dummy = ListNode()

        dummy.next = head

        slow = dummy
        fast = dummy

        for _ in range(n):
                fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = Solution().removeNthFromEnd(node1, 2)