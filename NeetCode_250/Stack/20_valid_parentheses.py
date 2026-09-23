class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hashmap = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        for p in s:
            if p in hashmap.keys():
                stack.append(p)
                continue

            if len(stack) == 0:
                return False

            temp = stack.pop()
            if hashmap[temp] != p:
                return False

        return not stack
