# Python practicals: ten small problems with solutions

[Subject home](../README.md) · [Theory](../01-theory/README.md)

Attempt each function before opening its answer. Run the assertions, then add an empty input, an unusual value and an invalid input. These examples use only Python's standard library.

## 1. Clean category names

Turn `[" AI ", "Data", "ai", ""]` into sorted unique nonempty lowercase labels.

<details><summary>Solution</summary>

```python
def clean_labels(values):
    return sorted({value.strip().lower() for value in values if value.strip()})
assert clean_labels([" AI ", "Data", "ai", ""]) == ["ai", "data"]
```

Set membership removes duplicates. Sorting makes the result deterministic.
</details>

## 2. Count frequencies

<details><summary>Solution</summary>

```python
from collections import Counter
assert dict(Counter(["a", "b", "a"])) == {"a": 2, "b": 1}
```

Use a count, rather than storing a separate list of every repeated item.
</details>

## 3. Sum only valid numeric entries

Accept numbers and numeric strings; skip `None`; raise a clear error for invalid text.

<details><summary>Solution</summary>

```python
def numeric_total(values):
    total = 0.0
    for value in values:
        if value is None:
            continue
        total += float(value)
    return total
assert numeric_total(["2", 3, None, "1.5"]) == 6.5
```

Skipping an invalid string silently would hide a data-quality problem.
</details>

## 4. Test primality

<details><summary>Solution</summary>

```python
from math import isqrt
def is_prime(n):
    if n < 2:
        return False
    return all(n % divisor for divisor in range(2, isqrt(n) + 1))
assert [n for n in range(10) if is_prime(n)] == [2, 3, 5, 7]
```

If a number has a factor above its square root, it also has one below it.
</details>

## 5. Flatten one level

<details><summary>Solution</summary>

```python
def flatten_once(groups):
    return [item for group in groups for item in group]
assert flatten_once([[1, 2], [], [3]]) == [1, 2, 3]
```

This deliberately flattens one level, not arbitrary nesting.
</details>

## 6. Aggregate revenue by city

<details><summary>Solution</summary>

```python
from collections import defaultdict
def revenue_by_city(rows):
    totals = defaultdict(float)
    for row in rows:
        totals[row["city"]] += row["price"] * row["quantity"]
    return dict(totals)
rows = [{"city": "East", "price": 10, "quantity": 2},
        {"city": "East", "price": 5, "quantity": 3}]
assert revenue_by_city(rows) == {"East": 35.0}
```

Before using this on real data, define returns, discounts, tax and currency.
</details>

## 7. Remove duplicate IDs while keeping the latest row

<details><summary>Solution</summary>

```python
def keep_latest(rows):
    latest = {}
    for row in rows:
        key = row["id"]
        if key not in latest or row["timestamp"] > latest[key]["timestamp"]:
            latest[key] = row
    return list(latest.values())
rows = [{"id": 1, "timestamp": "2025-01-01", "value": 10},
        {"id": 1, "timestamp": "2025-01-02", "value": 12}]
assert keep_latest(rows)[0]["value"] == 12
```

ISO dates sort here; real timestamps need normalized timezone/type and a tie rule.
</details>

## 8. Stream squares

<details><summary>Solution</summary>

```python
def squares_up_to(n):
    for value in range(n):
        yield value * value
stream = squares_up_to(4)
assert list(stream) == [0, 1, 4, 9]
assert list(stream) == []
```

The second pass is empty because the generator was consumed.
</details>

## 9. Avoid a mutable default

<details><summary>Solution</summary>

```python
def add_tag(tag, tags=None):
    result = [] if tags is None else list(tags)
    result.append(tag)
    return result
assert add_tag("ai") == ["ai"]
assert add_tag("sql") == ["sql"]
```

Each independent call gets an independent list; supplied input is copied deliberately.
</details>

## 10. Convert counts to proportions

<details><summary>Solution</summary>

```python
def proportions(counts):
    if any(value < 0 for value in counts.values()):
        raise ValueError("counts must be nonnegative")
    total = sum(counts.values())
    if total == 0:
        return {key: 0.0 for key in counts}
    return {key: value / total for key, value in counts.items()}
assert proportions({"a": 1, "b": 3}) == {"a": 0.25, "b": 0.75}
```

A zero-total policy is stated explicitly. For some applications an undefined rate should remain missing instead of zero.
</details>
