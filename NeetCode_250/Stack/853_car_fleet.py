class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs = list(zip(position, speed))
        pairs = sorted(pairs, reverse=True)

        stack = []

        for p, s in pairs:
            arrival_time = (target - p) / s

            if not stack or arrival_time > stack[-1]:
                stack.append(arrival_time)

        return len(stack)
