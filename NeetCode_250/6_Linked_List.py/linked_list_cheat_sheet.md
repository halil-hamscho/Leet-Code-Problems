Linked List Cheat Sheet

1. Fast & Slow Pointers

Pattern: Cycle detection, middle node, duplicate number.

slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

* Cycle: If slow is fast, cycle exists (check after advancing).
* Middle: When fast reaches end, slow is at middle.
* Find cycle entrance: After meeting, reset slow = head; move both one step until they meet.

2. Reverse Linked List (3 Pointers)

Pattern: Reverse entire list or a portion.

prev, curr = None, head
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

* prev becomes the new head.
* Partial reversal: Initialize prev = right_boundary, stop at curr is right_boundary.
* Reconnect: left_boundary.next = prev.

3. Two Pointers With Gap

Pattern: Remove Nth node from end.

slow = fast = dummy
for _ in range(n):
    fast = fast.next
while fast.next:
    slow = slow.next
    fast = fast.next

* Maintain a gap of n nodes.
* slow.next = slow.next.next removes target.

4. Dummy Node

Pattern: Deletion, insertion, merging, reversal.

dummy = ListNode(0, head)
curr = dummy
return dummy.next

* Avoids special handling when the head changes.
* Mental rule: If the head might change, consider a dummy.

5. HashMap + Doubly Linked List

Pattern: LRU / LFU Cache.

cache = {}  # key → node

* HashMap: O(1) node lookup.
* Doubly linked list: O(1) removal/insertion.
* LRU: Most recent near tail, evict head.
* LFU: Frequency → doubly linked list, track min_freq.
* Mental rule: Fast lookup + fast ordering updates → HashMap + DLL.

6. Merge Linked Lists

Pattern: Merge Two Sorted Lists / Merge K Lists.

dummy = ListNode()
tail = dummy
tail.next = node
tail = tail.next

* Compare heads of sorted lists.
* Merge K: Pairwise merging reduces rounds to O(\log k).
* Total time: O(N\log k).

7. HashMap for Node References

Pattern: Copy List With Random Pointer.

old_to_new[old] = Node(old.val)
new.next = old_to_new.get(old.next)

* Use when pointers reference arbitrary nodes.
* Preserves relationships between original and copied nodes.

8. Essential Interview Heuristics

Clue	Consider
Cycle / Middle	Fast & slow
Nth from end	Two pointers with gap
Reverse nodes	prev, curr, nxt
Head might change	Dummy node
Fast lookup + reorder	HashMap + DLL
Merge sorted lists	Dummy + tail
Copy arbitrary pointers	HashMap old → new
Reverse groups	Count → reverse → reconnect

9. Common Mistakes

* Save nxt before reversing or lose the remaining list.
* Use is for node identity, not ==.
* Save original group head because it becomes the tail.
* Check fast and fast.next before advancing two steps.
* Keep references before unlinking nodes.
* Python: while curr: means while curr is not None.

Complexity: Most linked list traversals and reversals are O(n) time and O(1) auxiliary space. HashMap based designs typically use O(n) space.