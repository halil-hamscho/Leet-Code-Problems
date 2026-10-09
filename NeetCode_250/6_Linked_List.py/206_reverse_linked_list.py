"""

In this case, since we can do it in two ways
- Recursively
- Iteratively

Iteratively:
- we need to keep track of 3 pointers in this case

Recursively
- base case:
    when head or head.next is None

    then we switch
    Node 1 -> Node 2 -> None

    Node2.next -> Node 1
    Node1.next = None

Time for Recursive Approach is O(n)
Space is O(n) since the recursive solution
uses O(n) stack space because each node 
creates another function call
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:

        prev = None
        current = head

        while current:

            temp = current.next

            current.next = prev 

            prev = current

            current = temp

        return prev

    def reverseList2(self, head: ListNode | None) -> ListNode | None:
        # recursive solution

        # Base Case
        if not head or not head.next:
            return head

        # recursively reverse the remaining list
        new_head = self.reverseList2(head.next)

        node2 = head.next
        node2.next = head
        head.next = None

        return new_head



def print_list(head):

    current = head

    while current:
        print(current.val, end="->")
        current = current.next

    print("None")

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

    print_list(node1)

    result = Solution().reverseList(node1)
    print_list(result)