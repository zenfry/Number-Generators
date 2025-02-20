class Xorshift:
    def __init__(self, seed):
        self.state = seed if seed != 0 else 1  # Avoid zero state

    def next(self):
        self.state ^= (self.state << 13) & 0xFFFFFFFF
        self.state ^= (self.state >> 17) & 0xFFFFFFFF
        self.state ^= (self.state << 5) & 0xFFFFFFFF
        return self.state & 0xFFFFFFFF  # Ensure it's 32-bit

    def random(self):
        return self.next() / 0xFFFFFFFF  # Normalize to [0,1]

# Example usage
xorshift = Xorshift(seed=42)
for _ in range(5):
    print(xorshift.random())
