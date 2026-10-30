"""Count contiguous subarrays whose sum equals k, including negative inputs."""
from collections import defaultdict
def solve(xs,k):
    counts=defaultdict(int,{0:1});prefix=answer=0
    for x in xs:
        prefix+=x;answer+=counts[prefix-k];counts[prefix]+=1
    return answer
assert solve([1,1,1],2)==2 and solve([1,-1,0],0)==3 and solve([],0)==0
