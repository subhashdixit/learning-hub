"""For sorted numbers, return the first matching index or−1."""
def solve(xs,target):
    lo,hi=0,len(xs)
    while lo<hi:
        mid=(lo+hi)//2
        if xs[mid]<target:lo=mid+1
        else:hi=mid
    return lo if lo<len(xs) and xs[lo]==target else -1
assert solve([1,2,2,3],2)==1 and solve([],2)==-1
