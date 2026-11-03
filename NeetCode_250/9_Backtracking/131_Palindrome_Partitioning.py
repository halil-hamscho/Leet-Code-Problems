"""

1. Choices
    - insert boundary
    - move on

2. State
    - index of string so s[start:i + 1]

3. Base Case
    - start == len(s)

4. Restoration


Fundamental Idea is:
- At each recursion level, explore every valid choice
- Advance the state according to what was consumed
- and undo the choice afterward

Combination Sum: Recursive Index controls which numbers can be selected next

Palindrome Partitioning: Your recursive index controls where the next substring begins

most important thing to recognize

we want the first recursive depth to be

"aab" so 
a, aa, aab to be the first depth

so in order to internalize that

for i in range(start, len(s)):
    substring = s[start: i + 1]

    # Choose, Explore, Undo

start = 0
s[start:i + 1]
i = 0 s[0:1]
i = 1 s[0:2]
i = 2 s[0:3]

Time:  O(n * 2^(n - 1))

palindrome check: O(n)
substring slicing: O(n)
copying path: O(n)

since partitions are gaps between characters
s = "aaaa"
s = a | a | a | a
4 characters, 3 possibel splits

Number of partitions = 2^(n - 1)

Space: O(n * 2^n)

path: O(n)
stack: O(n)
result output: O(2^n)
"""

class Solution:
    def partition(self, s: str) -> list[list[str]]:

        result = []
        path = []
        def dfs(start):

            if start == len(s):
                result.append(path.copy())
                return

            for i in range(start, len(s)):

                substring = s[start: i + 1]

                if not self.isPalindrome(substring):
                    continue

                # Choose
                path.append(substring)

                # Explore
                dfs(i + 1)

                # Undo
                path.pop()

            return

        dfs(0)
        return result
     
    def isPalindrome(self, s):
        l = 0
        r = len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome("aba"))
    result = sol.partition("aab")
    print(result)
    