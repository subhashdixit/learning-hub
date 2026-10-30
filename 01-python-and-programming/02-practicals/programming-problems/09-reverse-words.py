"""Reverse whitespace-separated word order; normalize whitespace to single spaces."""
def solve(text):return ' '.join(text.split()[::-1])
assert solve('  learn   Python now ')== 'now Python learn'
assert solve('')==''
