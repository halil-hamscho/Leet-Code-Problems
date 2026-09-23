class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            temp_price, temp_span = self.stack.pop()
            span += temp_span

        self.stack.append((price, span))

        return span
