"""Interview invariants and adversarial examples. Local synthetic teaching example; Python3.10+ standard library."""
def two_sum(values,target):
    seen={}
    for i,value in enumerate(values):
        if target-value in seen:return (seen[target-value],i)
        seen[value]=i
    return None
assert two_sum([3,3],6)==(0,1)
assert two_sum([],6) is None
assert two_sum([1],2) is None

def second_distinct(values):
    unique=sorted(set(values),reverse=True)
    return unique[1] if len(unique)>=2 else None
assert second_distinct([5,5,3])==3 and second_distinct([5,5]) is None
print('Two-sum duplicate case:',two_sum([3,3],6),'second distinct:',second_distinct([5,5,3]))
