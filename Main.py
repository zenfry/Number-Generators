from middle_square import MiddleSquare
from xorshift import Xorshift
from mersenne_twister import MersenneTwister

print("Middle Square Method:")
ms = MiddleSquare(seed=12345678)
for _ in range(5):
    print(ms.random())

print("\nXorshift Algorithm:")
xs = Xorshift(seed=42)
for _ in range(5):
    print(xs.random())

print("\nMersenne Twister:")
mt = MersenneTwister(seed=42)
for _ in range(5):
    print(mt.random())
