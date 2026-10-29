# 08 — Literals

[Python learning path](../../README.md) · [Open the notebook](examples.ipynb)

Read the notes and examples below, or open the notebook to run them. These are extracted from the existing Python notes; they have not been rewritten or executed during organization.

# 8. Literals

```python
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2 # 1.5 * 10^2
float_3 = 1.5e-3 # 1.5 * 10^-3

#Complex Literal 
x = 3.14j

print(a, b, c, d)
print(float_1, float_2,float_3)
print(x, x.imag, x.real)
```

Recorded output:
```text
10 100 200 300
10.5 150.0 0.0015
3.14j 3.14 0.0
```

```python
# binary
x = 3.14j
print(x.imag)
```

Recorded output:
```text
3.14
```

```python
string = 'This is Python'
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\U0001f600\U0001F606\U0001F923"
raw_str = r"raw \n string"

print(string)
print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)
```

Recorded output:
```text
This is Python
This is Python
C
This is a multiline string with more than one line code.
😀😆🤣
raw \n string
```

```python
a = True + 4
b = False + 10

print("a:", a)
print("b:", b)
```

Recorded output:
```text
a: 5
b: 10
```

```python
k = None
a = 5
b = 6
print('Program exe')
```

Recorded output:
```text
Program exe
```

```python
# Arithmetic
# Relational
# Logical
# Bitwise
# Assignment
# Membership
```

```python

```
