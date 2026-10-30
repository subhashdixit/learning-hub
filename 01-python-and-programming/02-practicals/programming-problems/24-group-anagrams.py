"""Group lowercase-word anagrams, keeping first group appearance order."""
def solve(words):
    groups={}
    for word in words:groups.setdefault(''.join(sorted(word)),[]).append(word)
    return list(groups.values())
assert solve(['eat','tea','tan','ate'])==[['eat','tea','ate'],['tan']]
