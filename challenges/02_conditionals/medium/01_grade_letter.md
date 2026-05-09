# grade

Given a numeric score from 0 to 100, return the corresponding letter grade as
a one-character string:

| Score | Grade |
| --- | --- |
| 90 – 100 | `"A"` |
| 80 – 89 | `"B"` |
| 70 – 79 | `"C"` |
| 60 – 69 | `"D"` |
| 0 – 59 | `"F"` |

## Examples
| Call | Result |
| --- | --- |
| `grade(100)` | `"A"` |
| `grade(90)` | `"A"` |
| `grade(85)` | `"B"` |
| `grade(70)` | `"C"` |
| `grade(60)` | `"D"` |
| `grade(59)` | `"F"` |
| `grade(0)` | `"F"` |

## Concepts exercised
- `if` / `elif` / `else` chains
- comparison operators
- the order in which conditions are checked

## Hints

<details><summary>Hint 1 — getting started</summary>

You'll need a chain of branches: one for each grade letter. Use `if`, then
`elif` for each follow-up, then a final `else` for the catch-all `"F"`.
</details>

<details><summary>Hint 2 — order matters</summary>

If you check `score >= 90` first, then `score >= 80` next, the second branch
only runs when the first failed — meaning `score < 90`. So `elif score >= 80`
already implies `80 <= score < 90` without you saying so explicitly.

This means **start from the highest grade and work down**, so each `elif` only
catches the range below the previous branch.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
if score is at least 90:
    return "A"
else if score is at least 80:
    return "B"
else if score is at least 70:
    return "C"
else if score is at least 60:
    return "D"
else:
    return "F"
```

Each branch returns immediately, so you don't need to worry about the upper
bound — by the time you reach the `"B"` branch, Python already knows the
score is less than 90.
</details>
