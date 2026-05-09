# sum_to_n

Return the sum of all integers from 1 to `n` (inclusive).
If `n` is 0 or negative, return 0.

## Examples
| Call | Result |
| --- | --- |
| `sum_to_n(1)` | `1` |
| `sum_to_n(2)` | `3` |
| `sum_to_n(5)` | `15` |
| `sum_to_n(10)` | `55` |
| `sum_to_n(100)` | `5050` |
| `sum_to_n(0)` | `0` |
| `sum_to_n(-3)` | `0` |

## Concepts exercised
- `for` loops and `range`
- the **accumulator pattern** (a running total)
- handling edge cases (non-positive input)

## Hints

<details><summary>Hint 1 — getting started</summary>

You'll need a variable to hold a running total, plus a loop that walks through
the numbers from 1 up to `n` and adds each one to the total.
</details>

<details><summary>Hint 2 — the loop</summary>

`range(1, n + 1)` gives the integers `1, 2, ..., n`. Loop over those:

```python
for i in range(1, n + 1):
    ...
```

The `+ 1` is because `range` stops *before* its end value.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
set total to 0
for each number i from 1 to n (inclusive):
    add i to total
return total
```

For `n ≤ 0`, the loop body runs zero times and `total` stays `0` — which is
the answer we want, so no special branch is needed.
</details>
