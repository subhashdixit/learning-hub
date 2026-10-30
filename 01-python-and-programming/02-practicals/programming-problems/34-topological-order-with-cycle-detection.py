"""Return a topological ordering of a directed graph containing all supplied vertices; raise on cycles."""
from collections import deque
def solve(graph):
    nodes=set(graph)|{v for values in graph.values() for v in values};degree={v:0 for v in nodes}
    for values in graph.values():
        for v in values:degree[v]+=1
    q=deque(sorted(v for v in nodes if degree[v]==0));out=[]
    while q:
        u=q.popleft();out.append(u)
        for v in graph.get(u,[]):
            degree[v]-=1
            if degree[v]==0:q.append(v)
    if len(out)!=len(nodes):raise ValueError('cycle')
    return out
assert solve({'a':['b'],'b':['c']})==['a','b','c']
try:solve({'a':['b'],'b':['a']})
except ValueError:pass
else:raise AssertionError('cycle missed')
