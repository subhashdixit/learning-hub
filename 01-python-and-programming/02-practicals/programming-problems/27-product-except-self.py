"""Return product of all other values for each index without division."""
def solve(xs):
    out=[1]*len(xs);prefix=1
    for i,x in enumerate(xs):out[i]=prefix;prefix*=x
    suffix=1
    for i in range(len(xs)-1,-1,-1):out[i]*=suffix;suffix*=xs[i]
    return out
assert solve([1,2,3,4])==[24,12,8,6] and solve([0,2,3])==[6,0,0]
