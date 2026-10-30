"""Return largest sum of k consecutive values; require1≤k≤n."""
def solve(xs,k):
    if not 1<=k<=len(xs):raise ValueError('invalid window')
    current=sum(xs[:k]);best=current
    for i in range(k,len(xs)):
        current+=xs[i]-xs[i-k];best=max(best,current)
    return best
assert solve([2,-1,3,4,-2],2)==7 and solve([-5,-2],1)==-2
