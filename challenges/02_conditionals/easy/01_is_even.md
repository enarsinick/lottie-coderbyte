# is_even

Given an integer `n`, return `True` if it is even and `False` if it is odd.

Zero counts as even. Negative numbers can be even or odd just like positive ones.

## Examples
| Call | Result |
| --- | --- |
| `is_even(0)` | `True` |
| `is_even(1)` | `False` |
| `is_even(2)` | `True` |
| `is_even(7)` | `False` |
| `is_even(-4)` | `True` |
| `is_even(-3)` | `False` |

## Concepts exercised
- the modulo operator `%` (remainder after division)
- comparison operators (`==`)
- returning a boolean (`True` / `False`)

## Hints

<details><summary>Hint 1 — getting started</summary>

A number is even if dividing it by 2 leaves no remainder. Python's `%`
operator gives you the remainder.
</details>

<details><summary>Hint 2 — comparing the remainder</summary>

`n % 2` is `0` when `n` is even and `1` (or `-1` for negatives, but still
non-zero) when `n` is odd. Compare it to `0` with `==`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return whether n modulo 2 equals 0
```

In Python that's a single line: `return n % 2 == 0`.

You don't need an `if`/`else` here — the comparison `n % 2 == 0` already
evaluates to `True` or `False`. (It's fine if you do use `if`/`else`; the
tests don't care which.)
</details>
