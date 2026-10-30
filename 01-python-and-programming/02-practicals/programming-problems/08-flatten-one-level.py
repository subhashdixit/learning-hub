"""Flatten a sequence of sequences exactly one level."""
def solve(rows):return [v for row in rows for v in row]
assert solve([[1,2],[],[3]])==[1,2,3] and solve([])==[]
