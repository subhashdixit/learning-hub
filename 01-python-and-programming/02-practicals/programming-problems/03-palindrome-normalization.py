"""Ignore nonalphanumeric characters and case; determine whether the resulting string is a palindrome."""
def solve(text):
    cleaned=''.join(c.casefold() for c in text if c.isalnum())
    return cleaned==cleaned[::-1]
assert solve('A man, a plan, a canal: Panama')
assert solve('') and not solve('python')
