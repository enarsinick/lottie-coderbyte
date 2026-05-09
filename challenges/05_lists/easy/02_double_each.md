# double_each

Given a list of numbers `nums`, return a **new** list where each number has
been multiplied by 2. The original list should not be modified.

## Examples
| Call | Result |
| --- | --- |
| `double_each([1, 2, 3])` | `[2, 4, 6]` |
| `double_each([0])` | `[0]` |
| `double_each([-1, -2, -3])` | `[-2, -4, -6]` |
| `double_each([])` | `[]` |
| `double_each([10, 20, 30, 40])` | `[20, 40, 60, 80]` |

## Concepts exercised
- iterating through a list with `for`
- **building** a new list inside a loop with `.append`
- (or, alternatively, list comprehensions)

## Hints

<details><summary>Hint 1 — getting started</summary>

Start with an empty list. Loop over each number in `nums`, multiply it by
two, and append the result. Return the new list at the end.
</details>

<details><summary>Hint 2 — two equivalent styles</summary>

**With a loop and `.append`** (most beginner-friendly):

```python
result = []
for x in nums:
    result.append(x * 2)
return result
```

**With a list comprehension** (more compact — try this once the loop version
clicks):

```python
return [x * 2 for x in nums]
```

Both produce the same result.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty list called result
for each number x in nums:
    append x times 2 to result
return result
```

For an empty input, the loop runs zero times and you return `[]`. No special
case needed.
</details>
