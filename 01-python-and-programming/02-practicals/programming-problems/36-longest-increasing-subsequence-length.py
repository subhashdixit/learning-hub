"""Return length of a strictly increasing subsequence."""
from bisect import bisect_left
def solve(xs):
    tails=[]
    for x in xs:
        i=bisect_left(tails,x)
        if i==len(tails):tails.append(x)
        else:tails[i]=x
    return len(tails)
assert solve([10,9,2,5,3,7,101,18])==4 and solve([2,2])==1 and solve([])==0
