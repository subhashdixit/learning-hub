"""Return indices of two distinct occurrences adding to target, or None."""
def solve(xs,target):
    seen={}
    for i,x in enumerate(xs):
        if target-x in seen:return seen[target-x],i
        seen[x]=i
    return None
assert solve([3,3],6)==(0,1) and solve([1],2) is None
