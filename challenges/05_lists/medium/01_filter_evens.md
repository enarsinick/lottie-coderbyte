# filter_evens

Given a list of integers, return a **new** list containing only the even
numbers from the input, in the same order they appeared.

Zero counts as even. Negative numbers can be even (e.g. `-2`) just like
positive ones.

## Examples
| Call | Result |
| --- | --- |
| `filter_evens([1, 2, 3, 4, 5, 6])` | `[2, 4, 6]` |
| `filter_evens([1, 3, 5])` | `[]` |
| `filter_evens([2, 4, 6])` | `[2, 4, 6]` |
| `filter_evens([-2, -1, 0, 1, 2])` | `[-2, 0, 2]` |
| `filter_evens([])` | `[]` |

## Concepts exercised
- iterating through a list
- combining a loop with an `if` condition
- the modulo operator `%` for divisibility tests
- building a new list with `.append`

## Hints

<details><summary>Hint 1 — getting started</summary>

This is similar to `double_each`, but with a filter step: only append a
number to the new list when it's even.
</details>

<details><summary>Hint 2 — checking even-ness</summary>

A number is even when it leaves no remainder when divided by 2:

```python
if x % 2 == 0:
    ...
```

This works for negatives too: `-2 % 2` is `0`, so `-2` is correctly even.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty list called result
for each number x in nums:
    if x is even:
        append x to result
return result
```

In Python, with a loop:

```python
result = []
for x in nums:
    if x % 2 == 0:
        result.append(x)
return result
```

Or as a one-liner with a list comprehension:
`return [x for x in nums if x % 2 == 0]`.
</details>
