'''
We can solve this problem recursively or with pointers
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):

        # # Recurisive Solution T O(n), M O(n)
        # if not head:
        #     return None
        
        # newHead = head
        # if head.next:
        #     newHead = self.reverseList(head.next)
        #     head.next.next = head
        # # if the head is the first node in the list
        # head.next = None
        # return newHead

        node = None

        # Most Optimal Solution T O(n) O(1) Pointers, no data structures
        while head: # while it is not null
            temp = head.next
            head.next = node
            node = head
            head = temp
        return node # result is stored in node as it will be the last

def main():
    print()
    head = [1,2,3,4,5]
    test = Solution()
    print(test.reverseList(head))

if __name__ == "__main__":
    main()