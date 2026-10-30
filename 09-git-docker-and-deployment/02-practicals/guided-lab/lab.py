"""Request validation and latency monitoring simulation. Local synthetic teaching example; Python3.10+ standard library."""
import statistics

def predict(request):
    if not isinstance(request,dict) or set(request)!={'distance_km'}:raise ValueError('schema')
    value=request['distance_km']
    if isinstance(value,bool) or not isinstance(value,(int,float)) or not 0<=value<=1000:raise ValueError('range/type')
    return {'estimated_minutes':10+2*value,'model_version':'teaching-v1'}
assert predict({'distance_km':5})['estimated_minutes']==20
for bad in [{},{'distance_km':-1},{'distance_km':True}]:
    try:predict(bad)
    except ValueError:pass
    else:raise AssertionError('invalid request accepted')
latencies=[10]*95+[200]*5
print('Mean latency:',statistics.mean(latencies),'maximum:',max(latencies),'valid response:',predict({'distance_km':5}))
