"""Evaluate whitespace-separated integer operands and +,-,*operations; reject malformed stack structure."""
def solve(text):
    stack=[]
    for token in text.split():
        if token in {'+','-','*'}:
            if len(stack)<2:raise ValueError('missing operand')
            b=stack.pop();a=stack.pop();stack.append(a+b if token=='+' else a-b if token=='-' else a*b)
        else:stack.append(int(token))
    if len(stack)!=1:raise ValueError('malformed expression')
    return stack[0]
assert solve('2 3 + 4 *')==20 and solve('5 2 -')==3
