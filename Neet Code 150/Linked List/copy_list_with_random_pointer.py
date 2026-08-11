'''
This is a two pass algorithm where we create a hashmap to allow us to have a connection
between the original copy and the DEEp copy

Each pass is linear time so O(n) and pass is O(n) since we have to store every single value in our hashmap

'''


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        oldToCopy = {None : None} # map every old node to new node, also map null to null

        current = head
        while current: #iterate until current becomes null
            copy = Node(current.val)
            oldToCopy[current] = copy
            current = current.next

        current = head
        while current: # now set pointers since we populated a hashmap
            copy = oldToCopy[current]
            # Set pointers
            copy.next = oldToCopy[current.next]
            copy.random = oldToCopy[current.random]
            current = current.next
            
        return oldToCopy[head]