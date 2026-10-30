"""For each number, return the next strictly greater value to its right, or None."""
def solve(xs):
    out=[None]*len(xs);stack=[]
    for i,x in enumerate(xs):
        while stack and xs[stack[-1]]<x:out[stack.pop()]=x
        stack.append(i)
    return out
assert solve([2,1,2,4,3])==[4,2,4,None,None] and solve([])==[]
