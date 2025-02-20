class LCG:
    def __init__(self, seed=1, a=1664525, c=1013904223, m=2**32):
        """Linear Congruential Generator (LCG)
        
        Parameters:
        - seed: Initial state (must be non-zero)
        - a: Multiplier (common choice: 1664525)
        - c: Increment (common choice: 1013904223)
        - m: Modulus (common choice: 2^32)
        """
        self.state = seed & 0xFFFFFFFF  # Ensure 32-bit state
        self.a = a
        self.c = c
        self.m = m

    def next(self):
        """Generate next random integer"""
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def random(self):
        """Generate a floating-point number in range [0,1)"""
        return self.next() / self.m

# Example usage
if __name__ == "__main__":
    lcg = LCG(seed=42)
    for _ in range(5):
        print(lcg.random())
