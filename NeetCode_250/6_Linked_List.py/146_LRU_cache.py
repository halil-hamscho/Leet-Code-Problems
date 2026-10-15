"""

- Hashmap for Key Lookup
- Double Linked List for Usage Order
- LRU 
- MRU pointers


Lessons:

- Store node references, not just values in the hashmap
- A doubly linked list allows O(1) removal because each node knows its
predecessor
- Dummy nodes eliminate boundary edge cases
- Preserve pointer references before modifying connections
- Updating an existing key must not trigger eviction

Mental Rule:

When a hashmap gives fast access but cannot efficiently maintain the required order,
consider pairing it with a doubly linked list.
"""
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache = {} # key = node

    def get(self, key: int) -> int:

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Update to MRU
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:

        # put it in MRU
        # if capacity too large, remove LRU

        if key in self.cache:
            node = self.cache.get(key)
            self.remove(node)
            self.insert(node)
            node.value = value

            return

        new_node = Node(key, value)

        if len(self.cache) >= self.capacity:

            lru_node = self.head.next
            del self.cache[lru_node.key]
            self.remove(lru_node)

        self.insert(new_node)
        self.cache[key] = new_node

        return
        
    def remove(self, node):
        # Disconnect node from its neighbors
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = None
        node.prev = None

        return 

    def insert(self, node):
        # Insert node immediately before dummy tail

        node.next = self.tail
        node.prev = self.tail.prev

        node.prev.next = node
        self.tail.prev = node

        return
    
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)