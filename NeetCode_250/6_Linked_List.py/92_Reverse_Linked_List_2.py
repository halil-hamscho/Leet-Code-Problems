"""
Time: O(n) - traverse to find boundaries, then reverse

Need to find 4 boundaries
- before left
- left
- right
- after right

prev becomes the new head of the reverse
curr becomes after right

b_left.next = prev
left_node.next = curr

High Level
- Find 4 Boundaries
- Reverse
- Connect

Lessons:
- Use dummy node when head might change
- always preserve next_node before modifying curr.next
- reversing pointers is easy, correctly connecting boundaries is
the challenging part

When modifying a linked list portion
- preserve boundaries
- modify pointers
- reconnect boundaries


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        dummy = ListNode()
        dummy.next = head

        # Find Boundaries
        counter = -1
        curr = dummy
        before_left = left_node = right_node = after_right = None
        while counter != right:
            counter += 1

            if counter == left - 1:
                before_left = curr
                
            if counter == left:
                left_node = curr

            if counter == right:
                right_node = curr

            curr = curr.next

        after_right = curr

        print(f"Before Left: {before_left.val}")
        print(f"Left Node: {left_node.val}")
        print(f"Right Node: {right_node.val}")
        print(f"After Right: {after_right.val}")

        # Reverse Portion
        prev = None
        curr = left_node
        while curr is not after_right:
            print(f"Curr value: {curr.val}")
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # Reconnect
        before_left.next = prev
        left_node.next = curr

        return dummy.next

   
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    left = 2
    right = 4

    nodes = [ListNode(val) for val in values]

    for i in range(len(values)):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]

    head = nodes[0]

    result = Solution().reverseBetween(head, left, right)
    curr = result
    while curr:
        print(f"Value: {curr.val}")
        curr = curr.next