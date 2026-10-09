"""
need a dummy node to remmeber where list starts

dummy node -> remembers beginning
tail => tracks the last attached node
p1, p2 -> tracks unprocessed nodes

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:

        p1 = list1
        p2 = list2
        dummy = ListNode()
        tail = dummy

        while p1 and p2:

            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next

            else:
                tail.next = p2
                p2 = p2.next
            
            tail = tail.next

        tail.next = p1 if p1 else p2

        return dummy.next

if __name__ == "__main__":

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(4)

    node1.next = node2
    node2.next = node3

    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)

    node4.next = node5
    node5.next = node6

    result = Solution().mergeTwoLists(node1, node4)
        