"""Find maximum length with no repeated characters."""
def solve(text):
    last={};left=best=0
    for right,c in enumerate(text):
        left=max(left,last.get(c,-1)+1)
        last[c]=right;best=max(best,right-left+1)
    return best
assert solve('abba')==2 and solve('abcabcbb')==3 and solve('')==0
