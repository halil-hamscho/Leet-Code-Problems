"""
Pattern:
- Trie + DFS + Backtracking

Trie to store words
DFS to search for words


Python Concepts

- Dictionary Memberships
if char in node.children:

- Dictionary Values
for child in node.children.values():

Lessons:
1. Track both positions: The Trie node and the search word index represent different information
2. Advance both positions together: Every matches character consumes one Trie edge
3. Return recursive results directly: Avoid unnecessary flag variables
4. Be careful with early returns: Return True when any child succeeds, but return False onyl after all children fail
5. Check is_end: Matching every search character is not enough unless the path represents a complete stored word

Time:
- addWord() O(n)
- searchWord()
    - n is len of word
    - k is num of .
    - 26 possible children

        - no dots: O(n)
        - k dots: O(26^k * n)
        - 2 at most: O(26^2 * n) -> O(n)
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:

        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

    def search(self, word: str) -> bool:

        """
        word may contain dots '.' 
        where dots can be matched with any letter.

        There will be at most 2 dots in word for 
        search queries.

        Search is not prefix matching, has to be the entire word

        DFS is searching the constructed Prefix Tree

        One Dot:
        - Up to 26 possible branches

        and each branch performs additional work to match the remaining word

        O(26 * n) where n is the length of n

        Two Dots: up to 678 possible branches 
        O(26^2 * n)

        with k dots it is 
        O(26^k * n)
        if all characters can be dots,that can become exponential in n

        Space: O(n)
        since we explore each child one at a time and not simultaneously

        the max recursion depth is determined by the length of the word
        """

        def dfs(node, index):

            if index == len(word): # explored entire word and checking if the curr Trie node is the end of a complete word
                return node.is_end

            char = word[index]

            if char == ".":
                for child in node.children.values():
                    b = dfs(child, index + 1)
                    if b:
                        return True
                    
                return False

            if char in node.children:
                return dfs(node.children[char], index + 1)
            
            else:
                return False

        return dfs(self.root, 0)


if __name__ == "__main__":
    wordDictionary = WordDictionary();
    wordDictionary.addWord("bad")
    wordDictionary.addWord("dad")
    wordDictionary.addWord("mad")
    wordDictionary.search("pad") 
    wordDictionary.search("bad")
    wordDictionary.search(".ad")
    wordDictionary.search("b..")


        
            