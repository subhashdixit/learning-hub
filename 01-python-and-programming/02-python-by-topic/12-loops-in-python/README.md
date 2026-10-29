# 12 — Loops in Python

[Python learning path](../../README.md) · [Open the notebook](examples.ipynb)

Read the notes and examples below, or open the notebook to run them. These are extracted from the existing Python notes; they have not been rewritten or executed during organization.

# 12. Loops in Python

- Need for loops
- While Loop
- For Loop

```python
# While loop example -> program to print the table
# Program -> Sum of all digits of a given number
# Program -> keep accepting numbers from users till he/she enters a 0 and then find the avg
```

```python
number = int(input('enter the number'))

i = 1

while i<11:
  print(number,'*',i,'=',number * i)
  i += 1
```

Recorded output:
```text
enter the number8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
8 * 6 = 48
8 * 7 = 56
8 * 8 = 64
8 * 9 = 72
8 * 10 = 80
```

```python
# while loop with else 

x = 1

while x < 3:
  print(x)
  x += 1

else:
  print('limit crossed')
```

Recorded output:
```text
1
2
limit crossed
```

```python
# Guessing game

# generate a random integer between 1 and 100
import random
jackpot = random.randint(1,100)

guess = int(input('guess karo'))
counter = 1
while guess != jackpot:
  if guess < jackpot:
    print('galat!guess higher')
  else:
    print('galat!guess lower')

  guess = int(input('guess karo'))
  counter += 1
  if counter ==5:
    break6
    
else:
  print('correct guess')
  print('attempts',counter)

  

```

Recorded output:
```text
guess karo4
guess karo4
galat!guess higher
galat!guess higher
guess karo5
galat!guess higher
guess karo6
galat!guess higher
guess karo5
```

```python
# For loop demo

for i in {1,2,3,4,5}:
  print(i)
```

Recorded output:
```text
1
2
3
4
5
```

```python
# For loop examples
```

### Program - The current population of a town is 10000. The population of the town is increasing at the rate of 10% per year. You have to write a program to find out the population at the end of each of the last 10 years.

```python
curr_pop = 10000

for i in range(10,0,-1):
  print(i,curr_pop)
  curr_pop = curr_pop - 0.1*curr_pop

```

Recorded output:
```text
10 10000
9 9000.0
8 8100.0
7 7290.0
6 6561.0
5 5904.9
4 5314.41
3 4782.969
2 4304.6721
1 3874.20489
```

### Sequence sum

1/1! + 2/2! + 3/3! + ...

```python
# code here
```

```python
# For loop vs While loops (When to use what?)
```
