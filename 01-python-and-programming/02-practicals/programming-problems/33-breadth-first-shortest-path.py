"""Return shortest unweighted path between vertices, or None."""
from collections import deque
def solve(graph,start,end):
    q=deque([start]);parent={start:None}
    while q:
        node=q.popleft()
        if node==end:
            path=[]
            while node is not None:path.append(node);node=parent[node]
            return path[::-1]
        for nxt in graph.get(node,[]):
            if nxt not in parent:parent[nxt]=node;q.append(nxt)
    return None
assert solve({'a':['b','c'],'b':['d'],'c':['d']},'a','d')==['a','b','d']
assert solve({},'a','z') is None
