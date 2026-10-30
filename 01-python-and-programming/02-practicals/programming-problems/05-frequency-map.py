"""Count occurrences of hashable values."""
from collections import Counter
def solve(xs):return dict(Counter(xs))
assert solve('banana')=={'b':1,'a':3,'n':2} and solve([])=={}
