# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k: int) :
        dummy = ListNode(0, head)
        node_before_sublist = dummy

        while True:
            initial_starting_node = node_before_sublist.next
            # Get the Kth node
            kth_node = self.getKth(node_before_sublist,k)
            if not kth_node:
                break
            node_after_sublist = kth_node.next # one node after our group
        
            # reverse group
            prev = None
            curr = node_before_sublist.next
            while curr != node_after_sublist:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            node_before_sublist.next = kth_node
            initial_starting_node.next = node_after_sublist
            node_before_sublist = initial_starting_node

        return dummy.next


    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    
        