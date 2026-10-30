"""Local retrieval and authorized-tool simulation. Local synthetic teaching example; Python3.10+ standard library."""
import re
# Lexical retrieval is intentional here: no model, API key or vector service is called.
docs=[{'id':'old','year':2024,'text':'annual leave policy 20 days','allowed':True}, {'id':'new','year':2026,'text':'annual leave policy 24 days','allowed':True}, {'id':'private','year':2026,'text':'annual leave confidential','allowed':False}]
def retrieve(query,year):
    terms=set(re.findall(r'\w+',query.lower()));eligible=[d for d in docs if d['allowed'] and d['year']==year]
    return sorted(eligible,key=lambda d:len(terms & set(d['text'].split())),reverse=True)
assert retrieve('annual leave',2026)[0]['id']=='new'
assert all(d['id']!='private' for d in retrieve('leave',2026))
seen=set();store=[]
def save_once(key,payload,authorized):
    if not authorized:raise PermissionError('not authorized')
    if key in seen:return 'already saved'
    store.append(payload);seen.add(key);return 'saved'
assert save_once('x',{'amount':20},True)=='saved'
assert save_once('x',{'amount':20},True)=='already saved' and len(store)==1
try:save_once('y',{},False)
except PermissionError:pass
else:raise AssertionError('unauthorized write')
print('Eligible retrieved source:',retrieve('annual leave',2026)[0]['id'],'stored records:',len(store))
