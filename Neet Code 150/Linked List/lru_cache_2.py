# Creating Node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # map key:node
        # Dummy Nodes
        self.head, self.tail = Node(0, 0), Node(0,0)
        # we need to insert the head and tail
        # Head = LRU, Tail = MRU
        # Connect to Each other
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        if key not in self.cache:
            return -1

        # Remove the Node, then add it as MRU
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.value

    def put(self, key, value):
        if key in self.cache:
            # Remove from Doubly Linked List but not Cache, since we want to update it
            old_node = self.cache[key]
            self.remove(old_node)
        # Add Updated Note
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)

        # If adding this node cause a problem
        if len(self.cache) > self.capacity:
            # The way we get the node to delete is self.head.next
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.cache[node_to_delete.key]

    # Remove Node from List
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    # Insert Node at Right
    def add(self, node):
        # The way we get the past end is doing past_end = self.tail.prev
        past_end = self.tail.prev
        past_end.next = node
        node.prev = past_end
        node.next = self.tail
        self.tail.prev = node

def main():
    capacity = 10
    obj = LRUCache(capacity)
    param_1 = obj.get(key)
    obj.put(key,value)
if __name__ == "__main__":
    main()

# Your LRUCache object will be instantiated and called as such:
