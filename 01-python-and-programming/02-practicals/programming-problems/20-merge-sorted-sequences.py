"""Merge two ascending sequences, retaining duplicates."""
def solve(a,b):
    i=j=0;out=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:out.append(a[i]);i+=1
        else:out.append(b[j]);j+=1
    return out+a[i:]+b[j:]
assert solve([1,3],[2,3])==[1,2,3,3] and solve([],[1])==[1]
