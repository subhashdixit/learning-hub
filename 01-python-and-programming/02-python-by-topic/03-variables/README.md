# 03 — Variables

[Python learning path](../../README.md) · [Open the notebook](examples.ipynb)

Read the notes and examples below, or open the notebook to run them. These are extracted from the existing Python notes; they have not been rewritten or executed during organization.

# 3. Variables

```python
# Static Vs Dynamic Typing
# Static Vs Dynamic Binding
# stylish declaration techniques
```

```python
# C/C++
name = 'nitish'
print(name)

a = 5
b = 6

print(a + b)
```

Recorded output:
```text
nitish
11
```

```python
# Dynamic Typing
a = 5
# Static Typing
# int a = 5
```

```python
# Dynamic Binding
a = 5
print(a)
a = 'nitish'
print(a)

# Static Binding
# int a = 5

```

Recorded output:
```text
5
nitish
```

```python
a = 1
b = 2
c = 3
print(a,b,c)
```

Recorded output:
```text
1 2 3
```

```python
a,b,c = 1,2,3
print(a,b,c)
```

Recorded output:
```text
1 2 3
```

```python
a=b=c= 5
print(a,b,c)
```

Recorded output:
```text
5 5 5
```
