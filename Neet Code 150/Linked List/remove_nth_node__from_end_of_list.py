'''
In this case, we would of reversed the list but it would of caused us to actually
have to reverse the list so instead we do the following

1. Initialize R at the head and and L at dummy node (1 prev to head)
2. Move it R from L by N
3. Move L and R by 1 until R hits null
4. L.next = L.next.next
5. Return dummy.next since we do not want to return the dummy node at the begining

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        # First Thing we have to do is create a dummy node (this is where L will be initialized)
        dummy = ListNode(0, head) # node.val = 0, node.next = head (1)
        left = dummy
        right = head

        # End of this will make the right pointer be in the position of n away from head
        while n > 0 and right:
            right = right.next
            n -= 1

        # Keep shifting left and right
        while right: # until right reaches the end of the list
            left = left.next
            right = right.next

        # delete the node
        # update the left node
        left.next = left.next.next
        # l 
        # 1 -> 2 -> 3
        # turns to 
        # 1 -> 3
        # Now, once we deleted, dummy.next is at the head
        return dummy.next # do not include 0, just the rest of the list