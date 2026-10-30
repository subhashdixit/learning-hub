"""Keep the last record by ID while preserving first-ID appearance order."""
def solve(rows):
    out={}
    for row in rows:out[row['id']]=row.copy()
    return list(out.values())
assert solve([{'id':'a','v':1},{'id':'b','v':2},{'id':'a','v':3}])==[{'id':'a','v':3},{'id':'b','v':2}]
