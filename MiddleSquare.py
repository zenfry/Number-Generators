class MiddleSquare:
    def __init__(self, seed, n_digits=8):
        self.state = seed
        self.n_digits = n_digits
        self.max_value = 10**n_digits

    def next(self):
        self.state = (self.state ** 2 // 10**(self.n_digits//2)) % self.max_value
        return self.state

    def random(self):
        return self.next() / self.max_value  # Normalize to [0,1]

# Example usage
ms = MiddleSquare(seed=12345678)
for _ in range(5):
    print(ms.random())
