"""Cash flows, compound returns and drawdown arithmetic. Local synthetic teaching example; Python3.10+ standard library."""
import math
pv=110/1.05;npv=pv-100;assert math.isclose(npv,4.761904761904759)
wealth=100
for r in [.1,-.1]:wealth*=1+r
assert math.isclose(wealth,99)
path=[100,120,90,110];peak=path[0];drawdowns=[]
for value in path:
    peak=max(peak,value);drawdowns.append(value/peak-1)
assert min(drawdowns)==-.25
real_growth=1.1/1.05-1
print('Illustrative NPV:',round(npv,4),'wealth:',wealth,'max observed drawdown:',min(drawdowns),'real growth:',round(real_growth,6))
