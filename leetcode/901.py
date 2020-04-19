class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack += (price, span),
        return span

#     First Thought: O(1) for time but 2n for space
#     def __init__(self):
#         self.stack = []
#         self.stock = []

#     def next(self, price: int) -> int:
#         self.stock += price,
#         while self.stack and self.stock[self.stack[-1]] <= price:
#             self.stack.pop()
#         span = len(self.stock) - 1 - (self.stack[-1] if self.stack else -1)
#         self.stack += len(self.stock)-1,
#         return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
