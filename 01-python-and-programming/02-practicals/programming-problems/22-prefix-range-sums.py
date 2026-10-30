"""Build prefix sums and answer an inclusive-left/exclusive-right range."""
def solve(xs,left,right):
    if not 0<=left<=right<=len(xs):raise ValueError('range')
    prefix=[0]
    for x in xs:prefix.append(prefix[-1]+x)
    return prefix[right]-prefix[left]
assert solve([2,3,4],1,3)==7 and solve([],0,0)==0
