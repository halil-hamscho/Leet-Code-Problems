"""
Biggest Takeaway is that we already know how to reverse a linked list with boundaries

in this case we need to reverse a fixed number of nodes while preserving connections 
to the rest of the LL

if we are in a group

we need to keep track of 
- left boundary
- right boundary
- starting value

self.reverse(left_boundary, left_value, curr.next)

Pattern
- Linked List Reversal
- Pointer Manipulation
- Group Processing

Reversal is the same except 

prev = right_boundary
curr = left value 
we do this at the beginning of the reversal so that the tail immediately points to the next value
1 -> 4

once we finish the reversal
it will be 
3 -> 2 -> 1 -> 4

so we just connect
left_boundary (dummy)
prev (3) the new reversed head
left_boundary.next = prev
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr:
            no_group = False
            left_boundary = curr

            for _ in range(k):

                curr = curr.next

                if curr is None:
                    no_group = True
                    break

            if no_group:
                return dummy.next

            original_first_value = left_boundary.next

            self.reverse(left_boundary, left_boundary.next, curr.next)

            curr = original_first_value # becomes the new last node of the reversed group

        return dummy.next
                
    def reverse(self, left_boundary, left_value, right_boundary):

        prev = right_boundary
        curr = left_value

        while curr is not right_boundary:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        left_boundary.next = prev

if __name__ == "__main__":

    head = [1,2,3,4,5]
    k = 2

    nodes = [ListNode(val) for val in head]

    for i in range(len(head)):
        if i + 1 < len(head):
            nodes[i].next = nodes[i + 1]

    result = Solution().reverseKGroup(nodes[0])