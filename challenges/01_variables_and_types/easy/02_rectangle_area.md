# area

Given a rectangle's `width` and `height` (both numbers), return the area —
that is, the product of the two.

## Examples
| Call | Result |
| --- | --- |
| `area(3, 4)` | `12` |
| `area(5, 5)` | `25` |
| `area(1, 1)` | `1` |
| `area(0, 10)` | `0` |
| `area(10, 7)` | `70` |

## Concepts exercised
- function parameters
- arithmetic operators (specifically `*`)
- returning a value

## Hints

<details><summary>Hint 1 — getting started</summary>

The area of a rectangle is `width × height`. You just need to multiply the
two parameters and return the result.
</details>

<details><summary>Hint 2 — Python's multiply operator</summary>

In Python, multiplication is `*` (not `×` or `x`). So `3 * 4` is `12`.
</details>

<details><summary>Hint 3 — full pseudo-code</summary>

```
return width times height
```

If either side is `0` the answer is `0` — that falls out automatically; you
don't need a special case.
</details>
