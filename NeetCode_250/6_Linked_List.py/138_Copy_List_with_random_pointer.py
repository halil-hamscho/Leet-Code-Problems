from typing import Optional
"""
The intuition here is that we cannot simply just copy next and random nodes since we need to have a deep copy

So in order to maintain the connections between objects and make sure they are copied correctly we need to use a hashmap

hashmap -> old_to_new = {}

First Pass:
- Create Nodes and Populate hashmap with old_to_new[curr] = Node(curr.val)

Second Pass:
- Connect the pointers
    - new = old_to_new.get(curr)
    - new.next = old_to_new.get(curr.next)
    - new.random = old_to_new.get(curr.random)

Time: O(n) two linked list traversals
Space: O(n) hashmap with n nodes

"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # First pass, create Nodes and populate hashmap
        old_to_new = {}
        curr = head
        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # Second Pass, connect the pointers
        curr = head
        while curr:
            # get the next
            new = old_to_new.get(curr)
            new.next = old_to_new.get(curr.next)
            new.random = old_to_new.get(curr.random)
            curr = curr.next

        return old_to_new.get(head)
    
if __name__ == "__main__":
    # Input: [[7,null],[13,0],[11,4],[10,2],[1,0]]

    values = [7, 13, 11, 10, 1]
    random_indices = [None, 0, 4, 2, 0]

    # Create all nodes
    nodes = [Node(val) for val in values]

    # Connect next and random pointers
    for i in range(len(nodes)):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]

        if random_indices[i] is not None:
            nodes[i].random = nodes[random_indices[i]]

    head = nodes[0]

    # Run solution
    result = Solution().copyRandomList(head)

    # Print copied list
    curr = result
    while curr:
        random_val = curr.random.val if curr.random else None
        print(f"Value: {curr.val}, Random: {random_val}")
        curr = curr.next