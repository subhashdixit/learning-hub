"""Check (),[]and{}nesting; ignore other characters."""
def solve(text):
    pairs={')':'(',']':'[','}':'{'};stack=[]
    for c in text:
        if c in '([{':stack.append(c)
        elif c in pairs:
            if not stack or stack.pop()!=pairs[c]:return False
    return not stack
assert solve('a([])') and not solve('([)]') and not solve('(')
