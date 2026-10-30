"""Return consecutive value/count pairs, preserving runs rather than global counts."""
from itertools import groupby
def solve(xs):return [(value,sum(1 for _ in run)) for value,run in groupby(xs)]
assert solve('aaabbca')==[('a',3),('b',2),('c',1),('a',1)]
assert solve('')==[]
