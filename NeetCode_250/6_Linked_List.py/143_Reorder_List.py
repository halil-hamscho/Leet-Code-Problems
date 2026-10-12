# Definition for singly-linked list.
"""

- Need to find the middle of a linked list
    - fast and slow pointers

- need to access nodes in reverse order 
    - reverse linked list

- need to combine two linked lists
    - linked list merging

- must modify in place
    - manipulate pointers instead of creating new nodes

Biggest Takeaway:

Save -> Rewire -> Advance

When merging, preseve both next1 and next2 before rewiring

Since a singly linked list only allows forward traversal, we cannot directly iterate backward from the tail


Instead of figuring out how to traverse backward, we can restructure the list so that
forward traversal gives us the order that we need
1. Find the middle to divide the list into two halves
2. Reverse the secodn half
3. Merge the halves by alternating nodes
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Find Middle Point
        fast = head
        slow = head

        while fast and fast.next:

            fast = fast.next.next
            slow = slow.next

        second_head = slow.next
        slow.next = None
               
        # Reverse Second Order
        prev = None
        curr = second_head
        while curr:

            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Prev is the new head
        # Combine two linked lists
        p1 = head
        p2 = prev
        while p2:

            # Save next nodes
            next1 = p1.next
            next2 = p2.next

            # Connect the two lists
            p1.next = p2
            p2.next = next1

            # Advance both pointers
            p1 = next1
            p2 = next2

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next= node5

    result = Solution().reorderList(node1)

            

