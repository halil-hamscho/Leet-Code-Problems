'''
If the input is an array then the cheat code is 
        new_list = []
        for list in lists:
            for value in list:
                new_list.append(value)
        return sorted(new_list)

Okay so in this case, we need to use sort. This will decrease the time complexity
from O(n * klists) to O(n * logk) because every time we are dividing by 2
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        # merging k lists
        # edge cases
        if not lists or len(lists) == 0:
            return None
        
        # merge each linked list until there is only one
        while len(lists) > 1: # more linked lists to merge
            # keep cutting the list in half
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        # reduced the list of linked lists to one
        return lists[0]
        
    def mergeList(self, l1, l2):
            # todo
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next
                
def convert_to_linked_list(list):
    dummy = ListNode()
    tail = dummy
    for value in list:
        tail.next = ListNode(val=value)
        tail = tail.next
    return dummy.next

def main():
    lists = [[1,4,5],[1,3,4],[2,6]] 
    linked_lists = [convert_to_linked_list(lst) for lst in lists]
    
    solution = Solution()
    merged_list = solution.mergeKLists(linked_lists)

if __name__ == "__main__":
    main()