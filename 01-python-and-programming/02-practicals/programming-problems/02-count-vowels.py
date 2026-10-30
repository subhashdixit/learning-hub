"""Count ASCII vowels in a string, ignoring case."""
def solve(text):return sum(c.lower() in 'aeiou' for c in text)
assert solve('Python AI')==3 and solve('')==0
