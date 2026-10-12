"""

In this case Python Concepts

val = l1.val if l1 else 0
^ Handle missing nodes

digit = total % 10 extract ones digit
carry = total // 10 extract tens digit

while l1 or l2 or carry: Continue while work remains

We do Linked List Traversal + Elementary Addition Simulation of Arithmetric

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:


        carry = 0
        dummy = ListNode() # need to do tail to preserve dummy as reference to the beginning
        tail = dummy

        while l1 or l2 or carry:

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            digit = total % 10 # 19 % 10 -> 9
            carry = total // 10 # 19 // 10 -> interger division 1

            node = ListNode(digit)
            tail.next = node
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next





        