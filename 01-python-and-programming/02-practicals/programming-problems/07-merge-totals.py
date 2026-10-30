"""Combine two amount dictionaries by summing amounts on shared keys without mutating inputs."""
def solve(a,b):
    out=a.copy()
    for key,value in b.items():out[key]=out.get(key,0)+value
    return out
a={'x':2};assert solve(a,{'x':3,'y':1})=={'x':5,'y':1} and a=={'x':2}
