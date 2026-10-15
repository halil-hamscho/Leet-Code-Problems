"""
Pattern: Divide and Conquer + Merge Two Sorted Linked Lists

Heuristic:
- We already know how to merge two sorted linked lists
    - use dummy, tail = dummy, then append to tail as we iterate then return dummy.next

The complexity here is understanding what is the best way to solve this

- At first I thought of using a single merged array and iterating to the end of the array -> end

Instead, what we can do is merge adjacent pairs

self.mergeTwo(lists[i], lists[i + 1])

We then reduce the number of times each node gets processed from approximately k to log k

Sequential Merging:
L1 + L2 -> A
A +  L3 -> B
B  + L4 -> C

Time: O(Nk)

previously merged nodes are repeatedly traversed as the result grows

Balanced Merging: O(N log k)

8 lists -> 4 lists -> 2 lists -> 1 list

We are not reducing the number of pairwise merges. We just change how many times we revisit the same nodes

Divide and Conquer reduces the repeated work by organizing those operations more efficiently
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:

        while len(lists) > 1:

            merged_lists = []

            for i in range(0, len(lists), 2):
                # Merge Adjacent lists

                if i + 1 < len(lists):
                    merged = self.mergetwo(lists[i], lists[i + 1])

                else:
                    merged = lists[i]

                merged_lists.append(merged)

            lists = merged_lists

        return lists[0] if lists else None

    def mergetwo(self, list1, list2):

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

def buildLinkedList(values):
    dummy = ListNode()
    tail = dummy

    for val in values:
        tail.next = ListNode(val)
        tail = tail.next

    return dummy.next


if __name__ == "__main__":
    values = [[1,4,5],[1,3,4],[2,6]]

    lists = [buildLinkedList(arr) for arr in values]

    result = Solution().mergeKLists(lists)



