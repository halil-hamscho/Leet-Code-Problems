
/*
Function ReverseList(head)
    Initialize prev to NULL
    Initialize curr to head

    While curr is not NULL
        // Save the next node
        next = curr.next

        // Reverse the link
        curr.next = prev

        // Move prev and curr forward
        prev = curr
        curr = next

    // Return the new head of the reversed list
    Return prev
End Function
 */


package arrays_and_hashing.linked_list_example.reverse_linked_list;

public class ListNode {
    int val;
    ListNode next;
    ListNode() {};
    ListNode(int val) {this.val = val;}
    ListNode(int val, ListNode next) {this.val = val; this.next = next;}
}

public class Solution {


    // We start with three pointers
    // 1. prev: This will keep track of the previous node we processed (starts as null)
    // 2. next: This will keep track of the next node to process
    // 3. curr: this is the current node we are processing (starts at the head of the list)
    ListNode prev = null;
    ListNode next = null;
    ListNode curr = head;
    // LOoop through the linked list until we reach the end
    while (curr != null) {
        next = curr.next;

        curr.next = prev;

        prev = curr;

        curr = next;
    }
    return prev;
}

