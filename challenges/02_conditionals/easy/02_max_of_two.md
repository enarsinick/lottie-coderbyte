# max_of_two

Given two numbers `a` and `b`, return the larger of the two. If they are equal,
returning either is fine.

**Don't use Python's built-in `max()` — write the comparison yourself.** The
point of the exercise is to practice `if`/`else`.

## Examples
| Call | Result |
| --- | --- |
| `max_of_two(3, 5)` | `5` |
| `max_of_two(10, 2)` | `10` |
| `max_of_two(7, 7)` | `7` |
| `max_of_two(-1, -5)` | `-1` |
| `max_of_two(0, 100)` | `100` |

## Concepts exercised
- comparison operators (`>`, `<`, `>=`)
- `if` / `else` to choose between two values
- `return` from inside a branch

## Hints

<details><summary>Hint 1 — getting started</summary>

Compare the two numbers. If `a` is bigger (or equal), return `a`. Otherwise
return `b`.
</details>

<details><summary>Hint 2 — return early</summary>

You can have two `return` statements — one inside the `if` branch and one
outside. The first `return` that runs will exit the function:

```python
if a > b:
    return a
return b
```

You don't even need an explicit `else`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
if a is greater than or equal to b:
    return a
otherwise:
    return b
```

Using `>=` (instead of `>`) handles the case where the two numbers are equal —
you'll return `a`, which equals `b`, so the test passes either way.
</details>
