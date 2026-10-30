"""Chronological forecasting baselines and smoothing. Local synthetic teaching example; Python3.10+ standard library."""
import math,statistics
series=[20+.05*t+3*math.sin(2*math.pi*t/7) for t in range(84)]
errors={'naive':[],'seasonal':[]}
for origin in range(28,len(series)):
    history=series[:origin];actual=series[origin]
    errors['naive'].append(abs(actual-history[-1]));errors['seasonal'].append(abs(actual-history[-7]))
mae={name:statistics.mean(v) for name,v in errors.items()}
assert mae['seasonal']<mae['naive']
level=10;alpha=.25;level=alpha*14+(1-alpha)*level;assert level==11
print('One-step rolling-origin MAE:',{k:round(v,3) for k,v in mae.items()},'smoothed level:',level)
