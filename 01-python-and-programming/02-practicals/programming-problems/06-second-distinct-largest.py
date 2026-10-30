"""Return the second distinct largest number, or None when absent."""
def solve(xs):
    values=sorted(set(xs),reverse=True)
    return values[1] if len(values)>1 else None
assert solve([5,5,3])==3 and solve([5,5]) is None and solve([]) is None
