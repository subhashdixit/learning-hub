"""Idempotent ingestion, quarantine and reconciliation. Local synthetic teaching example; Python3.10+ standard library."""
records=[{'id':'a','amount':20},{'id':'b','amount':30},{'id':'a','amount':20},{'id':'c','amount':-5}]
store={};rejected=[];duplicates=0
for row in records:
    if row['amount']<0:rejected.append((row,'negative amount'));continue
    if row['id'] in store:
        if store[row['id']]!=row:raise ValueError('conflicting duplicate')
        duplicates+=1;continue
    store[row['id']]=row.copy()
assert len(store)+len(rejected)+duplicates==len(records)
assert sum(r['amount'] for r in store.values())==50
print('Accepted unique:',len(store),'duplicate replays:',duplicates,'quarantined:',len(rejected),'total:',50)
