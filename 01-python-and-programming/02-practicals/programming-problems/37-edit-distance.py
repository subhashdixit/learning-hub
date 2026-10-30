"""Compute insertion/deletion/substitution distance between two strings, each cost1."""
def solve(a,b):
    previous=list(range(len(b)+1))
    for i,x in enumerate(a,1):
        current=[i]
        for j,y in enumerate(b,1):current.append(min(current[-1]+1,previous[j]+1,previous[j-1]+(x!=y)))
        previous=current
    return previous[-1]
assert solve('kitten','sitting')==3 and solve('','abc')==3
