"""Determine primality for an integer; values below2are not prime."""
from math import isqrt
def solve(n):
    if n<2:return False
    return all(n%d for d in range(2,isqrt(n)+1))
assert solve(2) and solve(29) and not solve(1) and not solve(25)
