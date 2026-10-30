"""Merge overlapping or touching intervals after sorting by start."""
def solve(intervals):
    out=[]
    for start,end in sorted(intervals):
        if start>end:raise ValueError('reversed interval')
        if out and start<=out[-1][1]:out[-1][1]=max(out[-1][1],end)
        else:out.append([start,end])
    return out
assert solve([[1,3],[2,6],[8,9]])==[[1,6],[8,9]] and solve([])==[]
