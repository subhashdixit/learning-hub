"""Return largest sum of a nonempty contiguous subarray."""
def solve(xs):
    if not xs:raise ValueError('empty')
    current=best=xs[0]
    for x in xs[1:]:current=max(x,current+x);best=max(best,current)
    return best
assert solve([-2,1,-3,4,-1,2,1,-5,4])==6 and solve([-3,-1])==-1
