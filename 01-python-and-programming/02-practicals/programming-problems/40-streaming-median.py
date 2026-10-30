"""Return the median after each prefix of a numeric stream."""
import heapq
def solve(xs):
    low=[];high=[];out=[]
    for x in xs:
        heapq.heappush(low,-x);heapq.heappush(high,-heapq.heappop(low))
        if len(high)>len(low):heapq.heappush(low,-heapq.heappop(high))
        out.append(-low[0] if len(low)>len(high) else (-low[0]+high[0])/2)
    return out
assert solve([5,1,3,2])==[5,3,3,2.5] and solve([])==[]
