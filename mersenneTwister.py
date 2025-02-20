class MersenneTwister:
    def __init__(self, seed):
        self.n = 624
        self.index = self.n
        self.MT = [0] * self.n
        self.MT[0] = seed & 0xFFFFFFFF
        for i in range(1, self.n):
            self.MT[i] = (1812433253 * (self.MT[i - 1] ^ (self.MT[i - 1] >> 30)) + i) & 0xFFFFFFFF

    def twist(self):
        for i in range(self.n):
            y = (self.MT[i] & 0x80000000) + (self.MT[(i + 1) % self.n] & 0x7FFFFFFF)
            self.MT[i] = self.MT[(i + 397) % self.n] ^ (y >> 1)
            if y % 2 != 0:
                self.MT[i] ^= 0x9908B0DF
        self.index = 0

    def next(self):
        if self.index >= self.n:
            self.twist()

        y = self.MT[self.index]
        y ^= (y >> 11)
        y ^= (y << 7) & 0x9D2C5680
        y ^= (y << 15) & 0xEFC60000
        y ^= (y >> 18)

        self.index += 1
        return y & 0xFFFFFFFF

    def random(self):
        return self.next() / 0xFFFFFFFF  # Normalize to [0,1]

# Example usage
if __name__ == "__main__":
    mt = MersenneTwister(seed=42)
    for _ in range(5):
        print(mt.random())
