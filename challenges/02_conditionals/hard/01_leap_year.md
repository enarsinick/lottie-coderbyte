# is_leap_year

Given a year (a positive integer), return `True` if it is a leap year and
`False` otherwise.

The rules:

1. A year divisible by **4** is a leap year, **except**
2. years divisible by **100** are *not* leap years, **except**
3. years divisible by **400** *are* leap years.

So `2000` is a leap year (divisible by 400), but `1900` is not (divisible by
100 but not 400). And `2024` is (divisible by 4, not by 100). And `2023` is
not (not divisible by 4 at all).

## Examples
| Call | Result | Why |
| --- | --- | --- |
| `is_leap_year(2000)` | `True` | divisible by 400 |
| `is_leap_year(2024)` | `True` | divisible by 4, not by 100 |
| `is_leap_year(1900)` | `False` | divisible by 100, not by 400 |
| `is_leap_year(2023)` | `False` | not divisible by 4 |
| `is_leap_year(2400)` | `True` | divisible by 400 |
| `is_leap_year(2100)` | `False` | divisible by 100, not by 400 |

## Concepts exercised
- combining boolean expressions with `and`, `or`, `not`
- `%` (modulo) for divisibility tests
- thinking about how rules with exceptions translate to logic

## Hints

<details><summary>Hint 1 — getting started</summary>

Each rule turns into a divisibility check using `%`:
- `year % 4 == 0` — divisible by 4
- `year % 100 == 0` — divisible by 100
- `year % 400 == 0` — divisible by 400
</details>

<details><summary>Hint 2 — combining the checks</summary>

Two ways to express the rule:

**Nested `if`s** (close to how the rules are written):

```
if divisible by 400 -> leap
else if divisible by 100 -> not leap
else if divisible by 4 -> leap
else -> not leap
```

**Single boolean expression**:

```
divisible by 4  AND (not divisible by 100  OR  divisible by 400)
```

Both are correct. Pick whichever feels clearer to you.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

Using the single-expression version:

```
return (year is divisible by 4)
       AND ((year is not divisible by 100) OR (year is divisible by 400))
```

In Python:

```python
return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
```

Walk through it for `1900`: `1900 % 4 == 0` is True, but `1900 % 100 != 0` is
False AND `1900 % 400 == 0` is False — so the second half is False, and
`True and False` is False. Correct.
</details>
