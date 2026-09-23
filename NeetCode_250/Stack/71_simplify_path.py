class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        i = 0
        while i < len(path):

            if path[i] == "/":
                i += 1
                continue
            else:
                temp = ""
                j = i

                while j < len(path) and path[j] != "/":
                    temp += path[j]
                    j += 1

                if temp == ".." and stack:
                    stack.pop()

                if temp not in ["..", "."]:
                    stack.append(temp)

                i += j - i

        return "/" + "/".join(stack)
