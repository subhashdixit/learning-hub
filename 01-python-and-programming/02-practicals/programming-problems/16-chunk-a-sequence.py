"""Split into chunks of positive size; retain a final short chunk."""
def solve(xs,size):
    if size<=0:raise ValueError('positive size')
    return [xs[i:i+size] for i in range(0,len(xs),size)]
assert solve([1,2,3,4,5],2)==[[1,2],[3,4],[5]] and solve([],2)==[]
