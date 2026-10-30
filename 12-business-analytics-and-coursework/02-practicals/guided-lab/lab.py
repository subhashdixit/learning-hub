"""Business metrics, cohorts and decision arithmetic. Local synthetic teaching example; Python3.10+ standard library."""
from collections import defaultdict
import math
rows=[{'revenue':100,'profit':50},{'revenue':900,'profit':90}]
margin=sum(x['profit'] for x in rows)/sum(x['revenue'] for x in rows)
wrong=sum(x['profit']/x['revenue'] for x in rows)/len(rows)
assert math.isclose(margin,.14) and math.isclose(wrong,.30)
cohort_size=100;active_next=30;retention=active_next/cohort_size
assert retention==.3
start,view,purchase=1000,400,100
assert purchase/start==.1 and purchase/view==.25
print('Total margin:',margin,'unweighted row mean:',wrong,'retention:',retention,'start-to-purchase:',purchase/start)
