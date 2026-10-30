"""Remove repeated hashable values while keeping the first-occurrence order."""
def solve(xs):return list(dict.fromkeys(xs))
assert solve([3,1,3,2,1])==[3,1,2] and solve([])==[]
