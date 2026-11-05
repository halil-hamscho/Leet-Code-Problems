"""

Word Search 1:
Pattern: Backtracking on a 2d board to find word

Word Search 2:
Pattern: Backtracking on a 2d board, but instead list of words

1. Choices:
up, down, left right

2. state:
current position row, col
current Trie node
path

3. base case:
- out of bounds or character is absent from Trie children

record answer when node.is_end = True

4. restoration:
return to previous position

The central concept here is we use a Trie since we have shared prefixes
The Trie determines which paths are worth exploring
Backtracking determines which paths can actually be formed on the board

Pattern: Trie + DFS + BackTracking

Time Complexity: O(S + RC * 3^L)
S = total characters across all words
R = rows
C = cols
L = length of word

Space: O(S + L)
stack: O(L)
path: O(L)
result: O(S)
trieL O(S)

"""


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:

        trie = Trie()
        for word in words:
            trie.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])

        result = []
        path = []

        def dfs(row, col, board, node):
            
            if not (0 <= row < ROWS and 0 <= col < COLS):
                return

            if board[row][col] not in node.children:
                return
            
            # Choose
            temp = board[row][col]
            board[row][col] = "#"
            path.append(temp)

            node = node.children[temp]

            if node.is_end:
                node.is_end = False
                result.append("".join(path))

            # Explore
            dfs(row - 1, col, board, node) # up 
            dfs(row + 1, col, board, node) # down
            dfs(row, col - 1, board, node) # left
            dfs(row, col + 1, board, node) # right

            # Return
            board[row][col] = temp
            path.pop()

            return            

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] in trie.root.children:
                    dfs(row, col, board, trie.root)
                    
        return result

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

if __name__ == "__main__":
    sol = Solution()
    board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words = ["oath","pea","eat","rain"]
    result = sol.findWords(board, words)
    print(result)