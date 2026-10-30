"""Transpose a rectangular list of rows; reject unequal row lengths."""
def solve(rows):
    if not rows:return []
    if any(len(r)!=len(rows[0]) for r in rows):raise ValueError('ragged')
    return [list(c) for c in zip(*rows)]
assert solve([[1,2],[3,4]])==[[1,3],[2,4]] and solve([])==[]
