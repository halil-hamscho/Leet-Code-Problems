'''
Regular Expression Matching
Given an input string s and a pattern p
implement regular expression matching support for '.' and '*' where

- . matches any single character
- * matches zero or more of the preceding element (before)


- dynamic programming
with memoization
meat of the work is the cache
            if (j + 1) < len(p) and p[j + 1] == '*': # check for a star
                cache[(i,j)] =  (dfs(i, j + 2) or (match and dfs(i + 1, j)))
if i stays the same, j + 2 or j stays the same i + 1
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # TOP DOWN memoization
        cache = {}

        # do it recursively
        def dfs(i,j): # i and j are what position are in the input strings s and p
            if (i,j) in cache:
                return cache[(i,j)]
            if i >= len(s) and j >= len(p):
                return True # they match perfectly
            if j >= len(p):
                return False   
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j + 1) < len(p) and p[j + 1] == '*': # check for a star
                cache[(i,j)] =  (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                # do not use the star or use the * only if there is a match
                return cache[(i,j)]
            if match: # if the two characters match we simply increment
                cache[(i,j)] = (dfs(i + 1, j + 1))
                return cache[(i,j)]
            cache[(i,j)] = False
            return False
        return dfs(0,0)
        
def main():
    print()


if __name__ == '__main__':
    print()