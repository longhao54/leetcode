class StockSpanner:

    def __init__(self):
        self.price = []
        self.count = []

    def next(self, price: int) -> int:
        count = 1
        while self.price:
            t = self.price[-1]
            if t <= price:
                count += self.count.pop()
                self.price.pop()
            else:
                break
        self.price.append(price)
        self.count.append(count)
        return count
