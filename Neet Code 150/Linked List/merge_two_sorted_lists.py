


class Solution:
    def mergeTwoLists(self, list1, list2):
        # Create a Dummy Node:
        dummy = ListNode()
        tail = dummy

        # While both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                # Update
                list1 = list1.next
            else: # l2 is less than or equal
                tail.next = list2
                list2 = list2.next
            # tail is updated regardless of either
            tail = tail.next
        # What if one list is empty or not
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next
