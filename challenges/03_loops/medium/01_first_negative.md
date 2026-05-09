# first_negative

Given a list of numbers, return the **first** negative number in the list.
If there are no negative numbers (or the list is empty), return `None`.

## Examples
| Call | Result |
| --- | --- |
| `first_negative([1, 2, -3, 4, -5])` | `-3` |
| `first_negative([10, -2, -3])` | `-2` |
| `first_negative([1, 2, 3])` | `None` |
| `first_negative([])` | `None` |
| `first_negative([-1])` | `-1` |
| `first_negative([0, 0, 0, -7])` | `-7` |

Note: `0` is not negative.

## Concepts exercised
- iterating through a list with `for`
- combining a loop with an `if` condition
- **early return** — finishing the function as soon as you have the answer
- returning `None` when no answer is found

## Hints

<details><summary>Hint 1 — getting started</summary>

Walk through the list one element at a time. As soon as you find a negative
number, return it. If the loop finishes without finding one, return `None`.
</details>

<details><summary>Hint 2 — early return</summary>

You don't need a "found" flag or a special variable — you can just `return`
straight from inside the loop:

```python
for x in nums:
    if x < 0:
        return x
```

Once `return` runs, the function exits immediately. The code *after* the loop
only runs if the loop finished without returning.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
for each x in nums:
    if x is less than 0:
        return x
return None     # only reached if no negative was found
```

For an empty list, the loop body never runs, so you fall through to the final
`return None` — exactly what the tests expect.
</details>
