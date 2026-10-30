"""Python expense-ledger capstone. Local synthetic teaching example; Python3.10+ standard library."""
import json
from collections import defaultdict

def summarize(records):
    seen=set(); totals=defaultdict(int)
    for record in records:
        key=record['id'];amount=record['amount_paise'];category=record['category']
        if key in seen:raise ValueError('duplicate expense ID')
        if isinstance(amount,bool) or not isinstance(amount,int) or amount<0:raise ValueError('invalid amount')
        if not isinstance(category,str) or not category.strip():raise ValueError('invalid category')
        seen.add(key);totals[category]+=amount
    return dict(totals)
records=json.loads('[{"id":"a","amount_paise":1200,"category":"food"},{"id":"b","amount_paise":800,"category":"travel"},{"id":"c","amount_paise":300,"category":"food"}]')
result=summarize(records);assert result=={'food':1500,'travel':800}
assert summarize([])=={}
for bad in [records+[records[0]],[{'id':'x','amount_paise':True,'category':'food'}]]:
    try:summarize(bad)
    except ValueError:pass
    else:raise AssertionError('invalid input accepted')
print('Category totals in paise:',result,'overall:',sum(result.values()))
