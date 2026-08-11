# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # First thing we want to do is find the middle
        slow, fast = head, head.next
        while fast and fast.next: # while fast is not null and it has not reached the end of the list
            slow = slow.next
            fast = fast.next.next
        # Now we have the list's split up
        second = slow.next # second half of the list (3)
        prev = slow.next = None # 1 -> 2 -> null
        
        # Now Reverse (same as reverse a linked list)
        while second:
            tmp = second.next # 4
            second.next = prev # null
            prev = second # 3 # this will be the last node (4)
            second = tmp # 4
        
        # Merge Lists
        first, second = head , prev # first node (1), last node (4)
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1 # inserting the second node
            first, second = tmp1, tmp2