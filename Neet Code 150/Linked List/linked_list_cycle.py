# Linear Time
# Constant Space


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        # Same position
        slow, fast = head, head

        # SHift slow and fast pointers
        while fast and fast.next: # are not null
            slow = slow.next
            fast = fast.next.next # shift by two
            if slow == fast: 
                return True
        return False # no cycle




def main():
    print()
    head = [3,2,0,-4]
    test = Solution()
    print(test.hasCycle(head))