'''
#need a node class
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map the key to nodes

        # Initialize Dummy Nodes
        # Left = LRU, Right = Most Recent
        self.left, self.right = Node(0,0), Node(0,0)
        # Connect the Nodes
        self.left.next, self.right.prev = self.right, self.left

    # helper function to update to the most recently used
    # remove node from list
    def remove(self, node): # passing the node that we want to remove from our doubly linked list
        # node will be the middle node
        prev, nxt = node.prev, node.next
        # removing middle node
        prev.next, nxt.prev = nxt, prev

    # helper function to insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev


    def get(self, key: int) -> int:
        # Straight Forward
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # if we have the same key, value, then remove the node before adding it again
            self.remove(self.cache[key])
        # create a new node
        self.cache[key] = Node(key, value)
        # insert the new value
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # if it does, then evict the least recently used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


'''

# Initialize the Node Class
class Node:
    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Map Key : Node

        # Before we start the cache, create LRU and MRU pointers
        # Left = LRU, right = Most Recent
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove from the list (pointer function)
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # Insert at MRU
    def insert(self, node):
        # prev, inserting node, right
        # the right is the right most pointer
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev


    def get(self, key: int):
        # Every time you get, you have to do most recent
        if key in self.cache:
            self.remove(self.cache[key])
            # re insert at the rightmost
            self.insert(self.cache[key])
            # self.cache[key] tells us the node, .val tells us the the actual value from the node
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int):
        # Node already exists, replace
        if key in self.cache:
            self.remove(self.cache[key])
            # create new node and insert
        self.cache[key] = Node(key, value) # key : node[key:value]
        self.insert(self.cache[key]) # inserting node[key:value]

        if len(self.cache) > self.cap:
            # remove from list and delete the LRU from the hashmap
            lru = self.left.next # always the LRU
            self.remove(lru) # remove from doubly linked list
            del self.cache[lru.key] # remove from cache


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

