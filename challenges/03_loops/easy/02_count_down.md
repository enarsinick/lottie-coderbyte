# count_down

Given a non-negative integer `n`, return a **list** that counts down from `n`
to `1`. If `n` is `0`, return an empty list.

## Examples
| Call | Result |
| --- | --- |
| `count_down(5)` | `[5, 4, 3, 2, 1]` |
| `count_down(1)` | `[1]` |
| `count_down(0)` | `[]` |
| `count_down(3)` | `[3, 2, 1]` |

## Concepts exercised
- building a list inside a loop (`.append`)
- `range()` with a step argument
- the difference between an empty list and `None`

## Hints

<details><summary>Hint 1 — getting started</summary>

Start with an empty list. Loop through the numbers in descending order and
append each one to the list. Return the list at the end.
</details>

<details><summary>Hint 2 — counting backwards with `range`</summary>

`range` takes an optional third argument — the **step**. So
`range(n, 0, -1)` produces `n, n-1, n-2, ..., 1` (it stops before `0`).

For example, `range(5, 0, -1)` yields `5, 4, 3, 2, 1`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
make an empty list called result
for each i in range(n, 0, -1):
    append i to result
return result
```

When `n` is `0`, `range(0, 0, -1)` is empty, so the loop never runs and you
return `[]`. No special branch needed.
</details>
