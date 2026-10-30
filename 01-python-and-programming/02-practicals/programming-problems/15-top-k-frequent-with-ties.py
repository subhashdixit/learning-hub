"""Return up to k values ordered by descending frequency, then ascending value; values must be mutually sortable."""
from collections import Counter
def solve(xs,k):
    if k<0:raise ValueError('negative k')
    counts=Counter(xs)
    return sorted(counts,key=lambda x:(-counts[x],x))[:k]
assert solve([2,1,2,1,3],2)==[1,2] and solve([],3)==[]
