# 09 — Operators in Python

[Python learning path](../../README.md) · [Open the notebook](examples.ipynb)

Read the notes and examples below, or open the notebook to run them. These are extracted from the existing Python notes; they have not been rewritten or executed during organization.

# 9. Operators in Python

- Arithmetic Operators
- Relational Operators
- Logical Operators
- Bitwise Operators
- Assignment Operators
- Membership Operators

```python
# Arithmetric Operators
print(5+6)

print(5-6)

print(5*6)

print(5/2)

print(5//2)

print(5%2)

print(5**2)
```

Recorded output:
```text
11
-1
30
2.5
2
1
25
```

```python
# Relational Operators
print(4>5)

print(4<5)

print(4>=4)

print(4<=4)

print(4==4)

print(4!=4)
```

Recorded output:
```text
False
True
True
True
True
False
```

```python
# Logical Operators
print(1 and 0)

print(1 or 0)

print(not 1)
```

Recorded output:
```text
0
1
False
```

```python
# Bitwise Operators

# bitwise and
print(2 & 3)

# bitwise or
print(2 | 3)

# bitwise xor
print(2 ^ 3)

print(~3)

print(4 >> 2)

print(5 << 2)
```

Recorded output:
```text
2
3
1
-4
1
20
```

```python
# Assignment Operators

# = 
# a = 2

a = 2

# a = a % 2
a %= 2

# a++ ++a

print(a)
```

Recorded output:
```text
0
```

```python
# Membership Operators

# in/not in

print('D' not in 'Delhi')

print(1 in [2,3,4,5,6])
```

Recorded output:
```text
False
False
```

```python
# Program - Find the sum of a 3 digit number entered by the user

number = int(input('Enter a 3 digit number'))

# 345%10 -> 5
a = number%10

number = number//10

# 34%10 -> 4
b = number % 10

number = number//10
# 3 % 10 -> 3
c = number % 10

print(a + b + c)
```

Recorded output:
```text
Enter a 3 digit number
```
