"""Return F(n), with F(0)=0,F(1)=1,for a nonnegative integer."""
from functools import lru_cache
@lru_cache(None)
def solve(n):
    if n<0:raise ValueError('negative')
    return n if n<2 else solve(n-1)+solve(n-2)
assert solve(0)==0 and solve(10)==55
