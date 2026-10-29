"""

Main Intuition:

A Trie is essentially a collection of nested dictionaries representing shared prefixes

Important Observations:

1. Characters are stored as dictionary keys

node.children[char] = TrieNode()

2. Nodes represent prefixes through their position in the tree

We do not need to store the entire prefix inside each node

3. is_end distinguishes complete words from prefixes

4. Insertion and searching follow one path

We don't need DFS or BFS because the input word determines exactly which child to visit

Pattern Recognition:

Main clue to consider a trie is:

You need to repeatedly store, search or query strings based on their prefixes

Mental Model

A Trie answers 2 different questions:

1. Does the path exist? This is what startsWith() checks
2. Does a complete word end at this path? This is what search() checks

Lesson:

A Trie node does not need to store its character explicitly.

The parent's dictionary key identifies the character, and the node maintains the information needed
to continue the path

"""
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:

        node = self.root
        
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]


        node.is_end = True


    def search(self, word: str) -> bool:

        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True if node.is_end else False

    def startsWith(self, prefix: str) -> bool:

        node = self.root

        for char in prefix:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True
        


# Your Trie object will be instantiated and called as such:
if __name__ == "__main__":
    
    trie = Trie()
    trie.insert("apple")
    trie.search("apple");   
    trie.search("app");    
    trie.startsWith("app")
    trie.insert("app")
    trie.search("app")   
