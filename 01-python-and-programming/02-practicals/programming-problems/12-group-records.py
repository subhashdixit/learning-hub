"""Group order IDs by customer, retaining input order within each group."""
from collections import defaultdict
def solve(rows):
    out=defaultdict(list)
    for customer,order in rows:out[customer].append(order)
    return dict(out)
assert solve([('a',1),('b',2),('a',3)])=={'a':[1,3],'b':[2]}
