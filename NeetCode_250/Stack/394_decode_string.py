class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for string in s:
            if string != "]":
                stack.append(string)
                continue

            temp_s = []
            while stack[-1] != "[":
                temp_s.append(stack.pop())

            stack.pop()

            temp_n = []
            while stack and stack[-1].isdigit():
                temp_n.append(stack.pop())

            number = "".join(reversed(temp_n))
            decoded = "".join(reversed(temp_s))

            stack.append(int(number) * decoded)

        return "".join(stack)
