from MiddleSquare import MiddleSquare
from Xorshift import Xorshift
from mersenneTwister import MersenneTwister
from LCG import LCG
from diehard_tests import DiehardTests

generators = [
    MiddleSquare(seed=12345678),
    Xorshift(seed=42),
    MersenneTwister(seed=42),
    LCG(seed=42)
]

for gen in generators:
    DiehardTests.run_all(gen)