# diehard_tests.py

import numpy as np
from collections import defaultdict
import math


class DiehardTests:
    @staticmethod
    def birthday_spacings(prng, n=512, m=2**24, trials=30):
        print("▶ Running Birthday Spacings Test...")
        collision_counts = []

        for _ in range(trials):
            values = [int(prng.random() * m) for _ in range(n)]
            values.sort()
            spacings = [values[i+1] - values[i] for i in range(n - 1)]

            spacing_count = defaultdict(int)
            collisions = 0
            for s in spacings:
                spacing_count[s] += 1
                if spacing_count[s] > 1:
                    collisions += 1
            collision_counts.append(collisions)

        mean_collisions = sum(collision_counts) / len(collision_counts)
        expected = (n ** 3) / (4 * m)

        print(f"    Avg Collisions: {mean_collisions:.2f}")
        print(f"    Expected (Poisson λ): {expected:.2f}")
        print()

    @staticmethod
    def runs_test(prng, n=10000):
        print("▶ Running Runs Test...")
        data = [prng.random() for _ in range(n)]
        median = np.median(data)
        runs = 1
        above = data[0] >= median

        for value in data[1:]:
            current = value >= median
            if current != above:
                runs += 1
                above = current

        expected = (2 * n - 1) / 3
        std_dev = math.sqrt((16 * n - 29) / 90)
        z = (runs - expected) / std_dev

        print(f"    Runs: {runs}")
        print(f"    Expected: {expected:.2f}")
        print(f"    Z-score: {z:.2f} {'(PASS)' if abs(z) < 2 else '(FAIL)'}")
        print()

    @staticmethod
    def monobit_test(prng, n=1000000):
        print("▶ Running Monobit Test...")
        bits = ""
        for _ in range(n // 32):
            value = int(prng.random() * (2**32))
            bits += f"{value:032b}"

        ones = bits.count("1")
        zeros = bits.count("0")
        s = ones - zeros
        test_stat = s / math.sqrt(n)

        print(f"    Ones: {ones}, Zeros: {zeros}")
        print(f"    Monobit Test Statistic: {test_stat:.2f} {'(PASS)' if abs(test_stat) < 3 else '(FAIL)'}")
        print()

    @staticmethod
    def run_all(prng):
        print(f"\n=== Diehard Tests for {prng.__class__.__name__} ===")
        DiehardTests.birthday_spacings(prng)
        DiehardTests.runs_test(prng)
        DiehardTests.monobit_test(prng)
