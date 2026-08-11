'''
Design a data structure that follows the constraint of
a LEAST RECENTLY USED (LRU) CACHE.

Implement the LRUCache class:

- LRUCache (int capacity) intialize the lru cache with positive size capacity
- int get(int key) return the value of the key if the key exists, otherwise return -1
- void put (int key, int value) Update the value of the key if the key exists
Otherwise, add the keyu-value pair to the cache. If the number of keys exceeds the capacity
fdrom this operation, evict the least recently used key

The functions get and put must each run in O(1) average time complexity


Design Problem

Intuition:
The intuition is to maintain a fixed-size cache of key-value pairs using a doubly linked list
and an unordered map. When accessing or adding a key-value pair, it moves the corresponding 
node to the front of the linked list, making it the most recently used item. 
This way, the least recently used item is always at the end of the list. 
When the cache is full and a new item is added, it removes the item at the end of the list 
(least recently used) to make space for the new item, ensuring the LRU property is 
maintained.


The Cache will store values
we want to be able to get specific values, based on a given key if it exists)
if we get values, we should also be able to put them

- Edge Cases:
1. if the key exists, update the key
2. If it doesn't, add the key value pair
3. If the number of keys exceeds the capacity, evict the least recently used key



Steps:
1. Keep track of capacity
2. Utilize a doubly linked list
3. Use hashmap to get the values of keys

Similar to browsers (chrome, google), if there are values not really used, they are removed

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
        # since we are inserting it all the way to the right
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

