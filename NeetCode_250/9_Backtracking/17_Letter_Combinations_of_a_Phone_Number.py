"""

1. Choices:
- for the current digit, choose one of its corresponding letters
each choice creates a new branch in the decision tree

2. State:
- Index: which digit am I currently processing
- Path: which letters have I selected so far

3. Base Case:
When we have processed every digit

4. Backtrack:
- choose letter
- explore the next digit
- undo the choice

Time: O(n * 4^n)
since n digits, 4 possible letters
"".join(path) -> O(n)

Space: O(n * 4^n)
path: O(n)
stack: O(n)
result: O(4^n)
hashmap: O(1)
"""

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:

        if not digits:
            return []

        hashmap = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        result = []
        path = []

        def dfs(index):
            if index == len(digits):
                s = "".join(path)
                result.append(s)
                return

            key = digits[index]

            for char in hashmap[key]:
                path.append(char)
                dfs(index + 1)
                path.pop()

            return
        
        dfs(0)
        return result
    
if __name__ == "__main__":
    digits = "23"
    sol = Solution()
    result = sol.letterCombinations(digits)