"""Compute n!for a nonnegative integer, rejecting bool and invalid inputs."""
def solve(n):
    if isinstance(n,bool) or not isinstance(n,int) or n<0:raise ValueError('nonnegative integer required')
    total=1
    for k in range(2,n+1):total*=k
    return total
assert solve(0)==1 and solve(5)==120
