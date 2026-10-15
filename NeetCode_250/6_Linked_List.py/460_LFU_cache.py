from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.freq = defaultdict(DoublyLinkedList) # freq -> Doubly Linked List
        self.min_freq = 0
        
    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Update Frequency
        self.updateFrequency(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            # increase freq by 1
            self.updateFrequency(self.cache[key])
            node = self.cache[key]
            node = value
            return
        
        # cache is full
        if len(self.cache) >= self.capacity:

            
            # First do LFU
            

            # Second do LRU

    def updateFrequency(self, node):

        old_liked_list = self.freq[node.freq]
        old_liked_list.remove(node)

        if old_liked_list.isEmpty() and node.freq == self.min_freq:
            self.min_freq += 1

        node.freq += 1

        new_linked_list = self.freq[node.freq]
        new_linked_list.insert(node)

        return
        

class DoublyLinkedList:

    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = None
        node.next = None

    def insert(self, node):

        node.prev = self.tail.prev
        node.next = self.tail

        node.prev.next = node
        self.tail.prev = node

    def isEmpty(self):
        return self.head.next is self.tail


class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)