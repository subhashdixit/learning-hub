"""Rotate right by k, accepting negative k as left rotation."""
def solve(xs,k):
    if not xs:return []
    k%=len(xs)
    return list(xs[-k:]+xs[:-k]) if k else list(xs)
assert solve([1,2,3],1)==[3,1,2] and solve([1,2,3],-1)==[2,3,1] and solve([],2)==[]
