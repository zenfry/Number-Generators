class LCG:
    def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
        self.state = seed
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random(self):
        return self.next() / self.m  # Normalize to range [0,1]

# Example usage
lcg = LCG(seed=42)
for _ in range(5):
    print(lcg.random())  # Generates pseudorandom numbers between 0 and 1
