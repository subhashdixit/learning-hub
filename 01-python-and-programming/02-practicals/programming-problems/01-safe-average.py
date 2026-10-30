"""Return the average of a nonempty numeric sequence; raise ValueError for empty input."""
def solve(xs):
    if not xs:raise ValueError('empty')
    return sum(xs)/len(xs)
assert solve([2,4])==3
try:solve([])
except ValueError:pass
else:raise AssertionError('empty accepted')
